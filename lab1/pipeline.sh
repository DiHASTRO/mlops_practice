#!/bin/bash
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1"
}

handle_error() {
    echo ""
    echo "=================================================="
    echo "ОШИБКА на этапе: $1"
    echo "Код ошибки: $2"
    echo "Вывод ошибки:"
    if [ -f /tmp/pipeline_error.log ]; then
        cat /tmp/pipeline_error.log
    else
        echo "Нет дополнительной информации"
    fi
    echo ""
    echo "Конвейер прерван."
    echo "=================================================="
    exit $2
}

if [ ! -f "requirements.txt" ]; then
    echo "Ошибка: Файл requirements.txt не найден!"
    echo "Убедитесь, что вы запускаете скрипт из папки lab1"
    exit 1
fi

# log "=== Запуск конвейера машинного обучения из $(pwd) ==="

export PYTHONIOENCODING=utf-8
export LANG=en_US.UTF-8

# log "Шаг 0: Установка зависимостей из requirements.txt..."
pip install -r requirements.txt > /tmp/pipeline_output.log 2>&1
PIP_EXIT_CODE=$?
if [ $PIP_EXIT_CODE -ne 0 ]; then
    cat /tmp/pipeline_output.log
    handle_error "Установка зависимостей" $PIP_EXIT_CODE
fi
# log "Зависимости успешно установлены"

# log "Шаг 1: Создание данных (data_creation.py)..."
python data_creation.py > /tmp/pipeline_output.log 2>&1
PYTHON_EXIT_CODE=$?
if [ $PYTHON_EXIT_CODE -ne 0 ]; then
    cat /tmp/pipeline_output.log
    handle_error "Создание данных" $PYTHON_EXIT_CODE
fi
# cat /tmp/pipeline_output.log
# log "Данные успешно созданы"

if [ -d "train" ] && [ -d "test" ]; then
    # log "Найдены директории: train, test"
    :
else
    log "Директории train/test не найдены"
fi

# log "Шаг 2: Предобработка данных (data_preprocessing.py)..."
python data_preprocessing.py > /tmp/pipeline_output.log 2>&1
PYTHON_EXIT_CODE=$?
if [ $PYTHON_EXIT_CODE -ne 0 ]; then
    cat /tmp/pipeline_output.log
    handle_error "Предобработка данных" $PYTHON_EXIT_CODE
fi
# cat /tmp/pipeline_output.log
# log "Данные успешно предобработаны"

# log "Шаг 3: Обучение модели (model_preparation.py)..."
python model_preparation.py > /tmp/pipeline_output.log 2>&1
PYTHON_EXIT_CODE=$?
if [ $PYTHON_EXIT_CODE -ne 0 ]; then
    cat /tmp/pipeline_output.log
    handle_error "Обучение модели" $PYTHON_EXIT_CODE
fi
# cat /tmp/pipeline_output.log
# log "Модель успешно обучена"

# log "Шаг 4: Тестирование модели (model_testing.py)..."
python model_testing.py > /tmp/pipeline_output.log 2>&1
PYTHON_EXIT_CODE=$?
if [ $PYTHON_EXIT_CODE -ne 0 ]; then
    cat /tmp/pipeline_output.log
    handle_error "Тестирование модели" $PYTHON_EXIT_CODE
fi
# cat /tmp/pipeline_output.log
# log "Модель успешно протестирована"

FINAL_METRIC=$(grep -E "^(MAE|Test MAE|MAE:)" /tmp/pipeline_output.log | tail -1)

# echo ""
# echo "=================================================="
# echo "ИТОГОВЫЙ РЕЗУЛЬТАТ:"
# echo "=================================================="
if [ ! -z "$FINAL_METRIC" ]; then
    echo "$FINAL_METRIC"
else
    echo "Внимание: финальная метрика не найдена"
    echo "Последние строки вывода:"
    tail -3 /tmp/pipeline_output.log
fi
# echo "=================================================="

rm -f /tmp/pipeline_output.log

# log "=== Конвейер успешно завершен ==="
