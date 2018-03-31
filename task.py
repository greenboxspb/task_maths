'''
Дано четыре числа, если первые два числа больше 5, третье число делится на 6,
четвертое число не делится на 3, то вывести yes, иначе no.
'''

num = input('Введите четыре числа через пробел: ').split(' ')
n1, n2, n3, n4 = int(num[0]), int(num[1]), int(num[2]), int(num[3])

if n1 > 5 and n2 > 5 and n3 % 6 == 0 and n4 % 3 == 0:
    print('yes')
else:
    print('no')


print('yes') if n1 > 5 and n2 > 5 and n3 % 6 == 0 and n4 % 3 == 0 else print('no')