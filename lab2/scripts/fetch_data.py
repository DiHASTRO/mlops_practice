"""
Скачивание датасет balance-scale с интернета (UCI / архив).
Этап конвейера: получение сырых данных.
"""
from __future__ import annotations

import urllib.request
from pathlib import Path

# Прямая ссылка на копию new-thyroid (UCI new-thyroid, 178 строк)
new_thyroid_URL = ("https://raw.githubusercontent.com/jbrownlee/Datasets/master/new-thyroid.csv")

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
OUTPUT = RAW_DIR / "new-thyroid.csv"


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Скачивание: {new_thyroid_URL}")
    urllib.request.urlretrieve(new_thyroid_URL, OUTPUT)
    print(f"Сохранено: {OUTPUT} ({OUTPUT.stat().st_size} байт)")


if __name__ == "__main__":
    main()
