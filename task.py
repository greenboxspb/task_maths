'''
Даны три числа. Написать "yes", если среди них есть одинаковые.
'''

num = input('Введите три числа через пробел: ').split(' ')
n1, n2, n3 = int(num[0]), int(num[1]), int(num[2])

if n1 == n2 or n2 == n3 or n3 == n1:
    print('yes')
else:
    print('no')