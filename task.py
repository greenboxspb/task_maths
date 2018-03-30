'''
Даны три числа.
Найдите те два из них, сумма которых наибольшая.
'''

num = input('Введите 3 числа через пробел: ').split(' ')

a, b, c = int(num[0]), int(num[1]), int(num[2])
sum1, sum2, sum3 = a + b, a + c, b + c

if sum1 > sum2 and sum1 > sum3:
    print(a, b, '"1"')
elif sum2 > sum1 and sum2 > sum3:
    print(a, c, '"2"')
elif sum3 > sum1 and sum3 > sum2:
    print(b, c, '"3"')
elif sum1 == sum2:
    print('Суммы равны', '"4"')
elif sum2 == sum3:
    print('Суммы равны', '"5"')
elif sum1 == sum3:
    print('Суммы равны', '"6"')