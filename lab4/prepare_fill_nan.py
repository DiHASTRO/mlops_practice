import pandas as pd

df = pd.read_csv('titanic.csv')
mean_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age)
df.to_csv('titanic.csv', index=False)
