# Локальный запуск этапов конвейера lab2 (Windows, без Jenkins)
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root
python -m pip install -r requirements.txt
python scripts/fetch_data.py
python scripts/preprocess_data.py
python scripts/train_model.py
python scripts/evaluate_model.py
