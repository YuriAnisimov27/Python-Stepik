import xlrd

trekking = xlrd.open_workbook('trekking3.xlsx')
sheet = trekking.sheet_by_index(1)
valrow = [sheet.row_values(rownum) for rownum in range(1, sheet.nrows)]

sheetInfo = trekking.sheet_by_index(0)
inforow = [sheetInfo.row_values(rownum) for rownum in range(1, sheetInfo.nrows)]

total = dict()
for element in inforow:
    total[element[0]] = [element[1], element[2], element[3], element[4]]

days = dict()
for day in valrow:
    days[day[0]] = [0, 0, 0, 0]

for element in valrow:
    if element[1] in total:
        if total[element[1]][3] == '':
            total[element[1]][3] = 0
        days[element[0]][0] += total[element[1]][0] * element[2] / 100
        days[element[0]][1] += total[element[1]][1] * element[2] / 100
        days[element[0]][2] += total[element[1]][2] * element[2] / 100
        days[element[0]][3] += total[element[1]][3] * element[2] / 100
for i in days:
    print(*list(map(int, days[i])))



