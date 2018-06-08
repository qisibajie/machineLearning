import pandas as pd
import numpy as np

# 1
# print(pd.__version__)
# 2
# pd.show_versions()
# 4
import numpy as np

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, index=labels)

# print(df['animal'])

# print(df.loc[df.index[[3,4,8]], ['animal', 'age']])
# print(df.iloc[[3,4,8], [2,3]])
# print(df[df['age'].between(2,4)])
# print(df['animal'].value_counts())
# print(df.sort_values(by=['age', 'visits'], ascending=[False, True]))
# df['priority'] = df['priority'].map({'yes': True, 'no': False})
# df['animal'] = df['animal'].replace('snake', 'python')
print(df.pivot_table(index='animal', columns='visits', values='age', aggfunc='mean'))
