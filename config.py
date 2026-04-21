# parsing di config.txt, validazione parametri, gestione errori

from dotenv import dotenv_values
from dataclasses import dataclass, field
from typing import Optional
import os


class ConfigError(Exception):
    """raises when configuration file is invalid"""
    pass


@dataclass
class MazeConfig:
    """Data container for maze generation parameters."""
    width: int
    height: int
    entry: tuple[int, int]
    exit_: tuple[int, int]
    output_file: str
    perfect: bool
    seed: Optional[int] = None
    algorithm: Optional[str] = None


REQUIRED_KEYS = {"WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"}


def load_config(path: str) -> dict[str, str]:
    """""Legge il file config e ritorna un dizionario grezzo KEY->VALUE."""
    if not os.path.exists(path):
        raise ConfigError(f"Config file not found")
    try:
        raw = dotenv_values(path)
    except Exception as exc:
        raise ConfigError(f"Can't read config file '{path}': {exc}") from exc
    return dict(raw)


def validate_int(value: str, key:str) -> int:
    """Valida WIDTH e HEIGHT: interi strettamente positivi."""
    try:
        result = int(value)
    except ValueError:
        raise ConfigError(f"{key} must be an integer, got {value}")
    
    if result <= 0:
        raise ConfigError(f"{key} must be positive, got {result}")
    return result


def validate_coord(value: str, key:str) -> tuple[int, int]:
    """Valida ENTRY e EXIT: coppia di interi non negativi in formato 'x,y'."""
    parts = value.split(",")

    if len(parts) != 2:
        raise ConfigError(f"{key} must be in 'x,y' format, got {value}")

    try:
        x, y = int(parts[0]), int(parts[1])
    except ValueError:
        raise ConfigError(f"{key} coordinates must be integers, got {value}")
    
    if x < 0 or y < 0:
        raise ConfigError(f"{key} coordinates must be positive, got {x}, {y}")
    return x, y


def validate_bool(value: str, key:str) -> bool:
    """Valida PERFECT: deve essere 'True' o 'False' (case-insensitive)."""
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    raise ConfigError(f"'{key}' mus be 'True'/'False', got {value}")


def validate_output_file(value: str) -> str:
    """Valida OUTPUT_FILE: non deve essere vuoto."""
    if not value or not value.strip():
        raise ConfigError("'OUTPUT_FILE' must not be empty")
    return value.strip()


def validate_bounds(entry, exit_, width, height) -> None:
    """Controlla che ENTRY ed EXIT siano dentro i bounds del labirinto."""
    if entry[0] >= width or entry[1] >= height:
        raise ConfigError(
            f"ENTRY {entry} is outside maze bounds ({width}x{height})."
        )
    if exit_[0] >= width or exit_[1] >= height:
        raise ConfigError(
            f"EXIT {exit_} is outside maze bounds ({width}x{height})."
        )


def validate_entry_exit(entry, exit_) -> None:
    """Controlla che ENTRY e EXIT siano celle diverse."""
    if entry == exit_:
        raise ConfigError(f"ENTRY and EXIT must be different, both are {entry}")


# chiama tutto quanto sopra
def parse_config(path: str) -> MazeConfig:
    """Legge, valida e ritorna la configurazione del labirinto."""
    
    raw = load_config(path)  # dizionario grezzo

    missing = REQUIRED_KEYS - raw.keys()
    if missing:
        raise ConfigError(
            f"Missing mandatory key(s): {missing}"
        )
    
    # valido i valori
    width = validate_int(raw["WIDTH"], "WIDTH")
    height = validate_int(raw["HEIGHT"], "HEIGHT")
    entry = validate_coord(raw["ENTRY"], "ENTRY")
    exit_ = validate_coord(raw["EXIT"], "EXIT")
    output_file = validate_output_file(raw["OUTPUT_FILE"])
    perfect = validate_bool(raw["PERFECT"], "PERFECT")

    validate_bounds(entry, exit_, width, height)
    validate_entry_exit(entry, exit_)

    # optional
    seed: Optional[int] = None
    if "SEED" in raw:
        seed = validate_int(raw["SEED"], "SEED")

    algorithm: Optional[str] = raw.get("ALGORITHM")

    return MazeConfig(
        width=width,
        height=height,
        entry=entry,
        exit_=exit_,
        output_file=output_file,
        perfect=perfect,
        seed=seed,
        algorithm=algorithm,
    )