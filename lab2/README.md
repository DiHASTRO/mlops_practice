# Лабораторная работа 2 (Module 2)

Конвейер MLOps: загрузка данных из сети, предобработка, обучение, оценка модели. Описание Jenkins — в `Jenkinsfile` и дубликате `jenkins_pipeline`.

## Структура

- `requirements.txt` — зависимости Python
- `scripts/fetch_data.py` — скачивание датасета
- `scripts/preprocess_data.py` — масштабирование, train/test, сохранение CSV и scaler
- `scripts/train_model.py` — обучение, `models/model.joblib`
- `scripts/evaluate_model.py` — метрики на тесте
- `Jenkinsfile` — декларативный пайплайн для Jenkins (SCM)
- `run_pipeline_local.bat` / `run_pipeline_local.ps1` / `run_pipeline_local.sh` — локальный прогон без Jenkins

Артефакты (`data/`, `models/`) по умолчанию не коммитятся (см. `.gitignore`).

## Локальный запуск

### Windows (CMD — без политики выполнения PowerShell)

```cmd
cd lab2
run_pipeline_local.bat
```

### Windows (PowerShell)

Если при запуске `.\run_pipeline_local.ps1` появляется ошибка про **execution policies**, используйте один из вариантов:

- разово обойти политику:

```powershell
cd lab2
powershell -ExecutionPolicy Bypass -File .\run_pipeline_local.ps1
```

- или разрешить скрипты для вашего пользователя (один раз):

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

После этого обычный запуск:

```powershell
cd lab2
.\run_pipeline_local.ps1
```

### Linux / macOS

```bash
cd lab2
chmod +x run_pipeline_local.sh
./run_pipeline_local.sh
```

### Вручную

```bash
cd lab2
python -m pip install -r requirements.txt
python scripts/fetch_data.py
python scripts/preprocess_data.py
python scripts/train_model.py
python scripts/evaluate_model.py
```

На Windows вместо `python3` используйте `python`, если так настроена система.

## Jenkins

1. Установите на агенте (или master): Python 3, `pip`, Git.
2. Создайте Pipeline job: **New Item** → **Pipeline** → **Pipeline script from SCM**.
3. Укажите репозиторий Git и **Script Path**: `lab2/Jenkinsfile`.
4. Сохраните и запустите **Build Now**.

Пайплайн выполняет `checkout scm`, установку зависимостей из `lab2/requirements.txt` и четыре Python-этапа. Для агента на Windows шаги `sh` нужно заменить на `bat` / PowerShell (отдельная настройка job).

## Требования к сети

Этап `fetch_data.py` скачивает CSV по HTTPS; агент Jenkins должен иметь доступ в интернет.
