from collections import defaultdict

with open('my.txt', 'w') as file:
    file.write('3423423')

# a = {i:i*2 for i in range(1, 4)}
# print(a)
# import json
# from pprint import pprint
# import openpyxl

# with open('my.json', 'r') as file:
#     data = json.load(file)
# pprint(data)

# book = openpyxl.open('file2.xlsx', read_only=True)
#
# sheet = book.worksheets
# print(sheet[0])
# sheet_main = sheet[0]
#
# for row in sheet_main:
#     print(row[0].value, row[1].value)
# # cells = sheet['A1':'B20']
# # # for name, count in cells:
# # #     print(f'{name.value}: {count.value}')
# #
# # for row in sheet.iter_rows(min_row=2, max_row=50, min_col=1, max_col=2):
# #     print(row[0].value, row[1].value)

# book = openpyxl.Workbook()
# sh = book.active
# sh['A1'] = 'ID'
# sh['B1'] = 'TITLE'
# sh['C1'] = 'YEAR'
# sh['D1'] = 'RUNTIME'
# sh['E1'] = 'ACTORS'
#
#
# with open('db.json') as db_file:
#     data = json.load(db_file)
#
# ROW = 2
# for mov in data['movies']:
#     sh[ROW][0].value = mov['id']
#     sh[ROW][1].value = mov['title']
#     sh[ROW][2].value = mov['year']
#     sh[ROW][3].value = mov['runtime']
#     sh[ROW][4].value = mov['actors']
#     ROW += 1
#
# book.save('file2.xlsx')
# book.close()