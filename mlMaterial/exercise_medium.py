import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
# print(df.drop_duplicates(subset='A'))
# print(df.loc[df['A'].shift() != df['A']])
# print(help(pd.DataFrame.diff))
# print(df.diff(periods=2, axis=0))
# print(df - df.shift(periods=2, axis=0))
df = pd.DataFrame(np.random.random(size=(5, 3)))
# print(df)
# print(df.mean(axis = 1))

# print(df.sub(df.mean(axis=1), axis=0))

print(help(df.drop_duplicates))
