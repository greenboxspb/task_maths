'''
Пользователь вводит три числа.
Если все числа больше 10 и первые два числа делятся на 3, то вывести yes, иначе no
'''

'''
Вариант 1
'''

num = input('Введите 3 числа через пробел: ').split(' ')

n1, n2, n3 = int(num[0]), int(num[1]), int(num[2])

if n1 and n2 and n3 > 10:
    if n1 % 3 == 0 and n2 % 3 == 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')


