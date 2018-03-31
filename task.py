'''
Даны три числа. Написать "yes",
если можно взять какие-то два из них и в сумме получить третье
'''

num = input('Введите 3 числа через пробел: ').split(' ')
n1, n2, n3 = int(num[0]), int(num[1]), int(num[2])

if (n1 + n2) == n3 or (n2 + n3) == n1 or (n1 + n3) == n2:
    print('yes')
else:
    print('no')

'''
Вариант 2
'''

print('yes') if (n1 + n2) == n3 or (n2 + n3) == n1 or (n1 + n3) == n2 else print('no')

