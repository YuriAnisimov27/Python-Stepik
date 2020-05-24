import xlrd
from statistics import median

salariesTable = xlrd.open_workbook('salaries.xlsx')
sheet = salariesTable.sheet_by_index(0)

valrow = [sheet.row_values(rownum) for rownum in range(1, sheet.nrows)]
valcol = [sheet.col_values(colnum) for colnum in range(1, sheet.ncols)]

cities = []
for i in range(len(valrow)):
    cities.append([median(valrow[i][1:]), i])

prof = []
for i in range(len(valcol)):
    prof.append([median(valcol[i][1:]), i])

print(valrow[max(cities)[1]][0], valcol[max(prof)[1]][0])

# import pandas as pd
#
# a = pd.read_excel('salaries.xlsx', index_col=0)
# print(a.median(axis=1).idxmax(), a.mean(axis=0).idxmax())
