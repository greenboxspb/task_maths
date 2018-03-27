'''
Даны три числа. Найдите наибольшее число из них.
'''

a = 1
b = 2
c = 3


if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)
