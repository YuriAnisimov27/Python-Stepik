import xlrd

trekking = xlrd.open_workbook('trekking1.xlsx')
sheet = trekking.sheet_by_index(0)

valrow = [sheet.row_values(rownum) for rownum in range(1, sheet.nrows)]

kkal = []
for i in valrow:
    kkal.append([i[1], i[0]])
kkal.sort(key=lambda item: (-item[0], item[1]))
for i in kkal:
    print(i[1])
