@echo off
setlocal
cd /d "%~dp0"
python -m pip install -r requirements.txt
if errorlevel 1 exit /b 1
python scripts\fetch_data.py
if errorlevel 1 exit /b 1
python scripts\preprocess_data.py
if errorlevel 1 exit /b 1
python scripts\train_model.py
if errorlevel 1 exit /b 1
python scripts\evaluate_model.py
exit /b %errorlevel%
