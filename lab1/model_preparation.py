#!/usr/bin/env python3
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import glob
import pickle

train_files = glob.glob('train/processed/data_*.csv')

X_train_list = []
y_train_list = []

for file in train_files:
    df = pd.read_csv(file)
    X = df[['day_of_year', 'month', 'day_of_week']].values
    y = df['temperature'].values
    
    X_train_list.append(X)
    y_train_list.append(y)

X_train = np.vstack(X_train_list)
y_train = np.concatenate(y_train_list)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

y_pred = model.predict(X_train)
mae = mean_absolute_error(y_train, y_pred)
rmse = np.sqrt(mean_squared_error(y_train, y_pred))
r2 = r2_score(y_train, y_pred)

print(f"Модель обучена и сохранена")
print(f"Train MAE: {mae:.2f}")
print(f"Train RMSE: {rmse:.2f}")
print(f"Train R2: {r2:.3f}")
