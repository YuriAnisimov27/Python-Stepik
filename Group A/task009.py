import xlrd
import math

trekking = xlrd.open_workbook('trekking2.xlsx')
sheet = trekking.sheet_by_index(1)
valrow = [sheet.row_values(rownum) for rownum in range(1, sheet.nrows)]

sheetInfo = trekking.sheet_by_index(0)
inforow = [sheetInfo.row_values(rownum) for rownum in range(1, sheetInfo.nrows)]

sum1, sum2, sum3, sum4 = 0, 0, 0, 0

total = dict()
for element in inforow:
    total[element[0]] = [element[1], element[2], element[3], element[4]]
for element in valrow:
    if element[0] in total:
        if total[element[0]][3] == '':
            total[element[0]][3] = 0
        sum1 += total[element[0]][0] * element[1] / 100
        sum2 += total[element[0]][1] * element[1] / 100
        sum3 += total[element[0]][2] * element[1] / 100
        sum4 += total[element[0]][3] * element[1] / 100

print(math.floor(sum1), math.floor(sum2), math.floor(sum3), math.floor(sum4))
