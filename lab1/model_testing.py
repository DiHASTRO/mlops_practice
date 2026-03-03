#!/usr/bin/env python3
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import glob
import pickle


with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

test_files = glob.glob('test/processed/data_*.csv')

X_test_list = []
y_test_list = []

for file in test_files:
    df = pd.read_csv(file)
    X = df[['day_of_year', 'month', 'day_of_week']].values
    y = df['temperature'].values

    X_test_list.append(X)
    y_test_list.append(y)

X_test = np.vstack(X_test_list)
y_test = np.concatenate(y_test_list)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)


print(f"Тестирование модели завершено")
print(f"Test MAE: {mae:.2f}")
print(f"Test RMSE: {rmse:.2f}")
print(f"Test R2: {r2:.3f}")

print(f"MAE: {mae:.2f}")
