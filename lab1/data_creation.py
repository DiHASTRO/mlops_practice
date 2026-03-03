#!/usr/bin/env python3
import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
import sys
import traceback

def main():
    try:
        print("=" * 50)
        print("НАЧАЛО: Создание датасетов")
        print("=" * 50)
        
        # Создаем директории train и test
        os.makedirs('train', exist_ok=True)
        os.makedirs('test', exist_ok=True)
        
        print("✓ Директории созданы")
        
        # Генерируем данные: изменение дневной температуры в течение года
        np.random.seed(42)
        
        # Создаем 5 различных наборов данных
        for i in range(5):
            # Количество дней
            days = 365
            
            # Базовый тренд: сезонность температуры
            time = np.linspace(0, 2*np.pi, days)
            base_temp = 15 + 10 * np.sin(time - np.pi/2)  # От -5 до 25 градусов
            
            # Добавляем шум
            noise = np.random.normal(0, 2, days)
            temperature = base_temp + noise
            
            # Добавляем аномалии в некоторые наборы
            if i >= 3:  # В последних двух наборах добавляем аномалии
                # Аномально жаркие дни
                anomaly_days = np.random.choice(days, 5, replace=False)
                temperature[anomaly_days] += np.random.uniform(10, 15, 5)
                # Аномально холодные дни
                anomaly_days = np.random.choice(days, 5, replace=False)
                temperature[anomaly_days] -= np.random.uniform(10, 15, 5)
            
            # Создаем даты
            dates = pd.date_range(start='2023-01-01', periods=days, freq='D')
            
            # Создаем признаки: день года, месяц, день недели
            df = pd.DataFrame({
                'date': dates,
                'day_of_year': range(1, days + 1),
                'month': dates.month,
                'day_of_week': dates.dayofweek,
                'temperature': temperature
            })
            
            # Разделяем на train/test (80/20)
            train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
            
            # Сохраняем в соответствующие папки
            train_path = f'train/data_{i+1}.csv'
            test_path = f'test/data_{i+1}.csv'
            
            train_df.to_csv(train_path, index=False)
            test_df.to_csv(test_path, index=False)
            
            print(f"✓ Набор {i+1}: {len(train_df)} тренировочных, {len(test_df)} тестовых образцов")
        
        print("=" * 50)
        print("УСПЕХ: Все датасеты успешно созданы")
        print("=" * 50)
        
    except Exception as e:
        print("\n" + "=" * 50)
        print("ОШИБКА в data_creation.py:")
        print("=" * 50)
        print(f"Тип ошибки: {type(e).__name__}")
        print(f"Описание: {str(e)}")
        print("\nПолный стек вызова:")
        traceback.print_exc()
        print("=" * 50)
        sys.exit(1)

if __name__ == "__main__":
    main()
