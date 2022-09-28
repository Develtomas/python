from collections import defaultdict

# with open('my.txt', 'w') as file:
#     file.write('3423423')

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


class Initialization:
    def __init__(self, capacity, food):
        if type(capacity) is not int:
            print('Количество людей должно быть целым числом')
            return None
        self.capacity = capacity
        self.food = food


class Vegetarian(Initialization):
    def __init__(self, c, f):
        super().__init__(c, f)

    def __str__(self):
        return f'{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}'


class MeatEater(Initialization):
    def __init__(self, c, f):
        super().__init__(c, f)

    def __str__(self):
        return f'{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}'


class SweetTooth(Initialization):
    def __init__(self, c, f):
        super().__init__(c, f)

    def __str__(self):
        return f'Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}'

    def checker(self, o):
        if isinstance(o, (int, Vegetarian, MeatEater)):
            return 'right'
        else:
            return f'Невозможно сравнить количество сладкоежек с {o}'

    def __eq__(self, other):
        if self.checker(other) == 'right':
            if type(other) is int:
                return self.capacity == other
            else:
                return self.capacity == other.capacity
        else:
            return self.checker(other)

    def __lt__(self, other):
        if self.checker(other) == 'right':
            if type(other) is int:
                return self.capacity < other
            else:
                return self.capacity < other.capacity
        else:
            return self.checker(other)

    def __gt__(self, other):
        if self.checker(other) == 'right':
            if type(other) is int:
                return self.capacity > other
            else:
                return self.capacity > other.capacity
        else:
            return self.checker(other)