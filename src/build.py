lazy from pathlib import Path

lazy from build_enumerables import build

if __name__ == "__main__":
    ENUMERABLES_PATH = Path("./python_linq")
    build(ENUMERABLES_PATH, ENUMERABLES_PATH / "enumerable.py")
