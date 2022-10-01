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


# class Initialization:
#     def __init__(self, capacity, food):
#         if type(capacity) is not int:
#             print('Количество людей должно быть целым числом')
#             return None
#         self.capacity = capacity
#         self.food = food
#
#
# class Vegetarian(Initialization):
#     def __init__(self, c, f):
#         super().__init__(c, f)
#
#     def __str__(self):
#         return f'{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}'
#
#
# class MeatEater(Initialization):
#     def __init__(self, c, f):
#         super().__init__(c, f)
#
#     def __str__(self):
#         return f'{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}'
#
#
# class SweetTooth(Initialization):
#     def __init__(self, c, f):
#         super().__init__(c, f)
#
#     def __str__(self):
#         return f'Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}'
#
#     def checker(self, o):
#         if isinstance(o, (int, Vegetarian, MeatEater)):
#             return 'right'
#         else:
#             return f'Невозможно сравнить количество сладкоежек с {o}'
#
#     def __eq__(self, other):
#         if self.checker(other) == 'right':
#             if type(other) is int:
#                 return self.capacity == other
#             else:
#                 return self.capacity == other.capacity
#         else:
#             return self.checker(other)
#
#     def __lt__(self, other):
#         if self.checker(other) == 'right':
#             if type(other) is int:
#                 return self.capacity < other
#             else:
#                 return self.capacity < other.capacity
#         else:
#             return self.checker(other)
#
#     def __gt__(self, other):
#         if self.checker(other) == 'right':
#             if type(other) is int:
#                 return self.capacity > other
#             else:
#                 return self.capacity > other.capacity
#         else:
#             return self.checker(other)

# class CustomButton:
#     def __init__(self, t, **kwargs):
#         self.text = t
#         for key, val in kwargs.items():
#             setattr(self, key, val)
#
#     def config(self, **kwargs):
#         for key, val in kwargs.items():
#             setattr(self, key, val)
#
#     def click(self):
#         try:
#             self.command()
#         except AttributeError:
#             print('Кнопка не настроена')
#         except TypeError:
#             print('Кнопка сломалась')

# class Customer:
#     def __init__(self, name, balance = 0):
#         self.name = name
#         self.balance = balance
#
#     @staticmethod
#     def check_type(val):
#         if not isinstance(val, (int, float)):
#             raise TypeError('Банк работает только с числами')
#
#     def withdraw(self, val):
#         Customer.check_type(val)
#         if self.balance >= val:
#             self.balance -= val
#         else:
#             raise ValueError('Сумма списания превышает баланс')
#
#     def deposit(self, add):
#         Customer.check_type(add)
#         self.balance += add

########################################
# class ZodiacSign:
#     def __init__(self):
#         self.day = int(input('enter the date: '))
#         self.month_dict = ['Январь', 'Февраль', 'Март', 'Апрель',\
#                              'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
#         self.month = ''
#         while self.month not in self.month_dict:
#             self.month = input('enter correct Month: ').capitalize()
#
#         self.month = self.month_dict.index(self.month) + 1
#         print(f"Your sign is: {self.sign}")
#
#     @property
#     def sign(self):
#         if(self.day >= 21 and self.day <= 31 and self.month == 3) or (self.month == 4 and self.day >= 1 and self.day <= 19):
#             sign = "Овен"
#         elif (self.day >= 20 and self.day <= 30 and self.month == 4) or (self.month == 5 and self.day >= 1 and self.day <= 20):
#             sign = "Телец"
#         elif (self.day >= 21 and self.day <= 31 and self.month == 5) or (self.month == 6 and self.day >= 1 and self.day <= 21):
#             sign = "Близнецы"
#         elif (self.day >= 22 and self.day <= 30 and self.month == 6) or (self.month == 7 and self.day >= 1 and self.day <= 22):
#             sign = "Рак"
#         elif (self.day >= 23 and self.day <= 31 and self.month == 7) or (self.month == 8 and self.day >= 1 and self.day <= 22):
#             sign = "Лев"
#         elif (self.day >= 23 and self.day <= 31 and self.month == 8) or (self.month == 9 and self.day >= 1 and self.day <= 22):
#             sign = "Дева"
#         elif (self.day >= 23 and self.day <= 30 and self.month == 9) or (self.month == 10 and self.day >= 1 and self.day <= 23):
#             sign = "Весы"
#         elif (self.day >= 24 and self.day <= 31 and self.month == 10) or (self.month == 11 and self.day >= 1 and self.day <= 22):
#             sign = "Скорпион"
#         elif (self.day >= 23 and self.day <= 30 and self.month == 11) or (self.month == 12 and self.day >= 1 and self.day <= 21):
#             sign = "Стрелец"
#         elif (self.day >= 22 and self.day <= 31 and self.month == 12) or (self.month == 1 and self.day >= 1 and self.day <= 20):
#             sign = "Козерог"
#         elif (self.day >= 21 and self.day <= 31 and self.month == 1) or (self.month == 2 and self.day >= 1 and self.day <= 18):
#             sign = "Водолей"
#         elif (self.day >= 19 and self.day <= 29 and self.month == 2) or (self.month == 3 and self.day >= 1 and self.day <= 20):
#             sign = "Рыбы"
#         return sign
###############################################


# def package_size_generator(width=15, length=50, height=20):
#     if length > 200:
#         print("Упаковка для лыж")
#     elif width <= 15 and length <= 15 and  height <= 15:
#         print("Коробка №1")
#     elif 15 < width <= 50 or\
#         15 < length <= 50 or\
#         15 < height <= 50:
#         print("Коробка №2")
#     else:
#         print("Стандартная коробка №3")
#
# package_size_generator()
################################################
# def check_luck(num):
#     print("Lucky" if sum(map(int, list(str(num)[0:3]))) == sum(map(int, list(str(num)[3:7]))) else "unlucky")
####################################################
# class Triangle:
#     def __init__(self):
#         self.f_side = int(input("first side: "))
#         self.s_side = int(input("second side: "))
#         self.t_side = int(input("third side: "))
#
#     def area(self):
#         p = float((self.f_side + self.s_side + self.t_side) / 2)
#         print(f"Area is {(p * (p - self.f_side) * (p - self.s_side) * (p - self.t_side)) ** 0.5}")
#
#
# class Circle:
#     def __init__(self):
#         self.radius = int(input("Radius: "))
#
#     def area(self):
#         print(f"Area is {3.14 * (self.radius ** 2)}")
#
#
# class Rectangle:
#     def __init__(self):
#         self.f_side = int(input("first side: "))
#         self.s_side = int(input("second side: "))
#
#     def area(self):
#         print(f"Area is {self.f_side * self.s_side}")
#
#
# def area_calculator():
#     """Please enter Triangle, Rectangle or Circle"""
#     try:
#         shape = eval(input('enter shape: '))()
#         shape.area()
#     except NameError:
#         print('error name')
#
#
# area_calculator()
##############################
# def word_cutter(word):
#     if len(word) % 2 == 0:
#         print(word[int(len(word)/2-1):int(len(word)/2+1)])
#     else:
#         print(word[int((len(word)-1)/2)])
#
# word_cutter('abba')
################################
# def sum_digits():
#     arr = []
#     while True:
#         digit = int(input('enter the number: '))
#         if digit:
#             arr.append(digit)
#         else:
#             print(f'total sum: {sum(arr)}')
#             break
#
#
# sum_digits()
#################################################
# class Dating:
#     def __init__(self, boys, girls):
#         self.boys = boys
#         self.girls = girls
#         self.county_check()
#
#     def county_check(self):
#         if len(self.boys) != len(self.girls):
#             raise Exception('Внимание, кто-то может остаться без пары!')
#         else:
#             self.mating()
#
#     def mating(self):
#         mates = list(zip(sorted(self.boys), sorted(self.girls)))
#         print('Ideal')
#         for pair in mates:
#             print(f'{pair[0]} : {pair[1]}')
#
#
# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
# girls = ['Kate', 'Liza', 'Kira', 'Emma']
# Dating(boys, girls)
##############################################
# def average_temperature(countries):
#     def temperature_mid(t_list):
#         return round((sum(t_list)/len(t_list) - 32) * 5 / 9, 1)
#     print('Average temp in countries:')
#     for country in countries:
#         print(f'{country[0]} - {temperature_mid(country[1])} C')
#
#
# countries_temperature = [
# ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
# ['Germany', [57.2, 55.4, 59, 59, 53.6]],
# ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
# ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
# ]
# average_temperature(countries_temperature)
###########################################
# def counter(user_dict):
#     print(f'Average view count: {round(sum(list(user_dict.values()))/len(user_dict), 2)}')
#
#
# def modify(stream):
#     user_dict = {}
#     for line in stream:
#         row = line.split(',')
#         if row[1] in user_dict.keys():
#             user_dict[row[1]] += int(row[2])
#         else:
#             user_dict[row[1]] = int(row[2])
#     return counter(user_dict)
#
#
# stream = [
# '2018-01-01,user100,150',
# '2018-01-07,user99,205',
# '2018-03-29,user1001,81'
# ]
# modify(stream)
####################################################
# def unique_digits():
#     digits_str = input('Enter digits with space separator: ')
#     digits_list = sorted(digits_str.split(' '))
#     digits_set = set()
#     not_unique = set()
#     for x in digits_list:
#         if x in digits_set:
#             not_unique.add(x)
#         else:
#             digits_set.add(x)
#
#     print(*sorted(list(not_unique)), sep='')
#
# unique_digits()
################################################

