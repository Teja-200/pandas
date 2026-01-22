import pandas as pd

data = pd.Series([10, 20, 30, 40, 50])

result = data.agg(['sum', 'mean', 'max', 'min', 'std'])

print(result)

print(data.sum())

print(data.mean())

print(data.cumsum())

