import pandas as pd

data = pd.Series([45,32,67,89,12])

tripled = data.map(lambda x:x**3)

print(tripled)
#sorting the series
print(data.sort_values())
#dropping an element
print(data.drop(0))

