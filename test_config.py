import pytest
from config import parse_config, ConfigError, Algorithm


# -------------------------
# ✔️ TEST VALIDO BASE
# -------------------------
def test_valid_config(tmp_path):
    file = tmp_path / "config.txt"
    file.write_text("""
WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=True
SEED=42
ALGORITHM=dfs
""")

    cfg = parse_config(str(file))

    assert cfg.width == 20
    assert cfg.height == 15
    assert cfg.entry == (0, 0)
    assert cfg.exit_ == (19, 14)
    assert cfg.output_file == "maze.txt"
    assert cfg.perfect is True
    assert cfg.seed == 42
    assert cfg.algorithm == Algorithm.dfs


# -------------------------
# ❌ WIDTH NON VALIDO
# -------------------------
def test_invalid_width(tmp_path):
    file = tmp_path / "config.txt"
    file.write_text("""
WIDTH=abc
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=True
""")

    with pytest.raises(ConfigError):
        parse_config(str(file))


# -------------------------
# ❌ HEIGHT NEGATIVO
# -------------------------
def test_negative_height(tmp_path):
    file = tmp_path / "config.txt"
    file.write_text("""
WIDTH=20
HEIGHT=-5
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=True
""")

    with pytest.raises(ConfigError):
        parse_config(str(file))


# -------------------------
# ❌ ENTRY FORMATO SBAGLIATO
# -------------------------
def test_invalid_entry_format(tmp_path):
    file = tmp_path / "config.txt"
    file.write_text("""
WIDTH=20
HEIGHT=15
ENTRY=0;0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=True
""")

    with pytest.raises(ConfigError):
        parse_config(str(file))


# -------------------------
# ❌ ENTRY FUORI BOUNDS
# -------------------------
def test_entry_out_of_bounds(tmp_path):
    file = tmp_path / "config.txt"
    file.write_text("""
WIDTH=5
HEIGHT=5
ENTRY=10,10
EXIT=1,1
OUTPUT_FILE=maze.txt
PERFECT=True
""")

    with pytest.raises(ConfigError):
        parse_config(str(file))


# -------------------------
# ❌ ENTRY == EXIT
# -------------------------
def test_same_entry_exit(tmp_path):
    file = tmp_path / "config.txt"
    file.write_text("""
WIDTH=10
HEIGHT=10
ENTRY=1,1
EXIT=1,1
OUTPUT_FILE=maze.txt
PERFECT=True
""")

    with pytest.raises(ConfigError):
        parse_config(str(file))


# -------------------------
# ❌ BOOLEAN NON VALIDO
# -------------------------
def test_invalid_bool(tmp_path):
    file = tmp_path / "config.txt"
    file.write_text("""
WIDTH=10
HEIGHT=10
ENTRY=0,0
EXIT=9,9
OUTPUT_FILE=maze.txt
PERFECT=maybe
""")

    with pytest.raises(ConfigError):
        parse_config(str(file))


# -------------------------
# ❌ MISSING KEY
# -------------------------
def test_missing_key(tmp_path):
    file = tmp_path / "config.txt"
    file.write_text("""
WIDTH=10
HEIGHT=10
ENTRY=0,0
EXIT=9,9
PERFECT=True
""")  # manca OUTPUT_FILE

    with pytest.raises(ConfigError):
        parse_config(str(file))


# -------------------------
# ✔️ OPTIONAL SEED EMPTY
# -------------------------
def test_optional_seed_empty(tmp_path):
    file = tmp_path / "config.txt"
    file.write_text("""
WIDTH=10
HEIGHT=10
ENTRY=0,0
EXIT=9,9
OUTPUT_FILE=maze.txt
PERFECT=True
SEED=
""")

    cfg = parse_config(str(file))
    assert cfg.seed is None