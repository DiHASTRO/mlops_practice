import pandas as pd

df = pd.read_csv('titanic.csv')
dummies = pd.get_dummies(df['Sex'], prefix='Sex')
df = pd.concat([df, dummies], axis=1)
df.drop('Sex', axis=1, inplace=True)
df.to_csv('titanic.csv', index=False)
