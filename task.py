'''
Дана дата из трех чисел (день, месяц и год).
Вывести yes, если такая дата существует (например, 12 02 1999 - yes, 22 13 2001 - no).
Считать, что в феврале всегда 28 дней.
'''

num = input('Введите дату из трех чисел (день (1-31), месяц (1-12) и год(1 - ~): ').split(' ')
n1, n2, n3 = int(num[0]), int(num[1]), int(num[2])
print(n1, n2, n3)

if n1 <= 31 and (n2 == 1 or n2 == 3 or n2 == 5 or n2 == 7 or n2 == 9 or n2 == 11 or n2 == 12) and n3 > 0:
    print('yes 1')
    print(n1)
elif n1 <= 30 and (n2 == 4 or n2 == 6 or n2 == 8 or n2 == 10) and n3 > 0:
    print('yes 2')
elif n1 <= 28 and n2 == 2 and n3 > 0:
    print('yes 3')
else:
    print('no')

