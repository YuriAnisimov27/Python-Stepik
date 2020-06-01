import xlrd
f = open('answer.txt', 'w', encoding='utf-8')

catalog = []
for i in range(1, 1001):
    file = xlrd.open_workbook(f'./rogaikopyta/{i}.xlsx')
    sheet = file.sheet_by_index(0)
    valname = sheet.row_values(1)[1]
    valcash = int(sheet.row_values(1)[3])
    catalog.append([valname, valcash])

catalog.sort()
for name in catalog:
    print(name[0], name[1], file=f)
f.close()