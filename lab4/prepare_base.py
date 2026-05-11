import pandas as pd
from catboost.datasets import titanic

train, _ = titanic()
df = train[['Pclass', 'Sex', 'Age']]
df.to_csv('titanic.csv', index=False)

