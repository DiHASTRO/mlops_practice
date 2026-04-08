"""
Скачивание датасет Wine с интернета (UCI / архив).
Этап конвейера: получение сырых данных.
"""
from __future__ import annotations

import urllib.request
from pathlib import Path

# Прямая ссылка на копию Wine.data (UCI Wine, 178 строк)
Wine_URL = (
    "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/Wine.csv"
)

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
OUTPUT = RAW_DIR / "Wine.csv"


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Скачивание: {Wine_URL}")
    urllib.request.urlretrieve(Wine_URL, OUTPUT)
    print(f"Сохранено: {OUTPUT} ({OUTPUT.stat().st_size} байт)")


if __name__ == "__main__":
    main()
