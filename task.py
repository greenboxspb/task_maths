'''
Дано две даты, каждая из которых состоит из трех чисел (день, месяц и год).
Вывести yes, если первая дата раньше второй, иначе вывести no.
'''

date1 = input('Введите дату №1 через пробел (12-01-1992, например): ').split(' ')
dn1, dn2, dn3 = int(date1[0]), int(date1[1]), int(date1[2])
date2 = input('Введите дату №2 через пробел (25-06-1995, например): ').split(' ')
dan1, dan2, dan3 = int(date2[0]), int(date2[1]), int(date2[2])

if dn3 < dan3:
    print('yes 1')
elif dn3 == dan3 and dn2 < dan2:
    print('yes 2')
elif dn3 == dan3 and dn2 == dan2 and dn1 < dan1:
    print('yes')
else:
    print('no')


