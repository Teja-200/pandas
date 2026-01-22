import pandas as pd

data  = pd.Series([45,34,76,87,33])

print(data)

print(data.iloc[0])

print(data.iloc[-1])

print(data.loc[0])

print(data.loc[3])

print(data.iloc[0:-1])

filtered = data[data > 50]

print(filtered)