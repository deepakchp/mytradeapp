import pandas as pd

mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000 },
          {'a': 10000, 'b': 20000, 'c': 30000, 'd': 40000 }
          ]

df = pd.DataFrame(mydict)
print(df.iloc[0])
print(df.iloc[0].shift(1))