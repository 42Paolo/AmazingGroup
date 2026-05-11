# parsing di config.txt, validazione parametri, gestione errori

from typing import Optional
from enum import Enum
from typing_extensions import Self
from pydantic import BaseModel, Field, model_validator


class ConfigError(Exception):
    """raises when configuration file is invalid"""
    pass


class Algorithm(Enum):
    dfs = "dfs"
    recursive_backtracker = "recursive_backtracker"
    prim = "prim"


class MazeConfig(BaseModel):
    """Data container for maze generation parameters."""
    width: int = Field(..., gt=0)
    height: int = Field(..., gt=0)
    entry: tuple[int, int]
    exit_: tuple[int, int]
    output_file: str = Field(..., min_length=1)
    perfect: bool
    seed: Optional[int] = Field(default=None, gt=0)
    algorithm: Optional[Algorithm] = None

    @model_validator(mode='after')
    def validate_maze(self) -> Self:
        # ENTRY e EXIT devono essere dentro i bounds
        if self.entry[0] >= self.width or self.entry[1] >= self.height:
            raise ConfigError(
                f"ENTRY {self.entry} is outside maze bounds "
                f"({self.width}x{self.height})"
            )
        if self.exit_[0] >= self.width or self.exit_[1] >= self.height:
            raise ConfigError(
                f"EXIT {self.exit_} is outside maze bounds "
                f"({self.width}x{self.height})"
            )

        # ENTRY e EXIT devono essere celle diverse
        if self.entry == self.exit_:
            raise ConfigError(
                f"ENTRY and EXIT must be different, both are {self.entry}"
            )

        return self


def load_config(path: str) -> dict[str, str]:
    raw = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, value = line.split("=", 1)
            raw[key.strip()] = value.strip()
    return raw


def parse_bool(value: str, key: str) -> bool:
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    raise ConfigError(f"'{key}' must be 'True' or 'False', got '{value}'")


def parse_config(path: str) -> MazeConfig:
    raw = load_config(path)

    def parse_coord(value: str, key: str) -> tuple[int, int]:
        parts = value.split(",")
        if len(parts) != 2:
            raise ConfigError(f"{key} must be in 'x,y' format, got {value}")
        try:
            return int(parts[0]), int(parts[1])
        except ValueError:
            raise ConfigError(f"{key} coordinates must be integers, got {value}")

    try:
        return MazeConfig(
            width=int(raw["WIDTH"]),
            height=int(raw["HEIGHT"]),
            entry=parse_coord(raw["ENTRY"], "ENTRY"),
            exit_=parse_coord(raw["EXIT"], "EXIT"),
            output_file=raw["OUTPUT_FILE"],
            perfect=parse_bool(raw["PERFECT"], "PERFECT"),
            seed=int(raw["SEED"]) if raw.get("SEED") else None,
            algorithm=raw.get("ALGORITHM"),
        )
    except ConfigError:
        raise  # rilancia ConfigError senza wrappare
    except Exception as e:
        raise ConfigError(f"Configuration error: {e}") from e


