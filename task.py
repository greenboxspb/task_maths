'''
Дана дата из трех чисел (день, месяц и год).
Вывести yes, если такая дата существует (например, 12 02 1999 - yes, 22 13 2001 - no).
Считать, что в феврале всегда 28 дней.
'''

'''
Вариант №1
'''
num = input('Введите дату из трех чисел (день (1-31), месяц (1-12) и год(1 - ~): ').split(' ')
day, month, year = int(num[0]), int(num[1]), int(num[2])
month_1, month_2 = [1, 3, 5, 7, 9, 11, 12], [4, 6, 8, 10]
days_1 = list(range(1, 32))
days_2 = list(range(1, 31))

if year < 0:
    print('no')
elif day in days_1 and month in month_1:
    print('yes 1_1')
elif day in days_2 and month in month_2:
    print('yes 2_2')
elif 1 <= day <= 28 and month == 2:
    print('yes 3')
else:
    print('no')

'''
Вариант №2
'''

# print('yes') if n3 > 0 and ((1 <= n1 <= 31 and n2 in month1) or (1 <= n1 <= 30 and n2 in month2) or (1 <= n1 <= 28 and n2 == 2)) else print('no')


'''
Вариант №3 (СТАС)
'''

date = input('Введите дату из трех чисел (день (1-31), месяц (1-12) и год(1 - ~): ').split(' ')
day, month, year = int(date[0]), int(date[1]), int(date[2])
months_1, months_2 = [1, 3, 5, 7, 9, 11, 12], [4, 6, 8, 10]

if (year > 0 and day >= 1) and \
   (day <= 31 and month in months_1 or
   day <= 30 and month in months_2 or
   day <= 28 and month == 2):
    print('yes 1')
else:
    print('no')