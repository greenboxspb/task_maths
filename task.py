'''
Даны три числа.
Найдите те два из них, сумма которых наибольшая.
'''

num = input('Введите 3 числа через пробел: ').split(' ')

a, b, c = int(num[0]), int(num[1]), int(num[2])
sum1, sum2, sum3 = a + b, a + c, b + c

if sum1 > sum2 and sum1 > sum3:
    print(a, b)
elif sum2 > sum1 and sum2 > sum3:
    print(a, c)
elif sum3 > sum1 and sum3 > sum2:
    print(b, c)
else:
    print("числа не были определены", '"4"')

