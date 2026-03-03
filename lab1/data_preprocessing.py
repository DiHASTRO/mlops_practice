#!/usr/bin/env python3
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import os
import glob
import pickle


train_files = glob.glob('train/data_*.csv')
test_files = glob.glob('test/data_*.csv')

os.makedirs('train/processed', exist_ok=True)
os.makedirs('test/processed', exist_ok=True)

scaler = StandardScaler()
all_train_data = []

for file in train_files:
    df = pd.read_csv(file)
    features = df[['day_of_year', 'month', 'day_of_week']].values
    all_train_data.append(features)

all_train_data = np.vstack(all_train_data)
scaler.fit(all_train_data)

with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

for file in train_files:
    df = pd.read_csv(file)
    features = df[['day_of_year', 'month', 'day_of_week']].values
    scaled_features = scaler.transform(features)
    
    df_scaled = df.copy()
    df_scaled[['day_of_year', 'month', 'day_of_week']] = scaled_features
    
    filename = os.path.basename(file)
    df_scaled.to_csv(f'train/processed/{filename}', index=False)

for file in test_files:
    df = pd.read_csv(file)
    features = df[['day_of_year', 'month', 'day_of_week']].values
    scaled_features = scaler.transform(features)
    
    df_scaled = df.copy()
    df_scaled[['day_of_year', 'month', 'day_of_week']] = scaled_features
    
    filename = os.path.basename(file)
    df_scaled.to_csv(f'test/processed/{filename}', index=False)

print("Данные успешно предобработаны и масштабированы")
