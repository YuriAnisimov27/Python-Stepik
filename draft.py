import xlrd

f = open('answer.txt', 'w', encoding='utf-8')

catalog = []
for i in range(1, 1001):
    file = xlrd.open_workbook(f'./rogaikopyta/{i}.xlsx').sheet_by_index(0)
    catalog.append([file.row_values(1)[1], int(file.row_values(1)[3])])

catalog.sort()
for name in catalog:
    print(name[0], name[1], file=f)
f.close()
