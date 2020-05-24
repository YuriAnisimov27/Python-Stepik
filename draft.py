import pandas as pd

a = pd.read_excel('salaries.xlsx', index_col=0)
print(a.median(axis=1).idxmax(), a.mean(axis=0).idxmax())
