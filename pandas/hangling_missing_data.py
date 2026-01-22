import pandas as pd
import numpy as np

data=pd.Series([1, 2, np.nan, 4, np.nan, 6])

print(data.isnull())

print(data.notnull())

print(data.fillna(9999))