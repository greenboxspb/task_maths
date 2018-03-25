'''
Пользователь вводит три числа.
Если все числа больше 10 и первые два числа делятся на 3, то вывести yes, иначе no
'''

'''
Вариант 1
'''

num = input('Введите 3 числа через пробел: ').split(' ')

num1 = int(num[0])
num2 = int(num[1])
num3 = int(num[2])

if num1 > 10 and num2 > 10 and num3 > 10:
    if num1 % 3 == 0 and num2 % 3 == 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')


'''
Вариант 2
'''

num1, num2, num3 = int(num[0]), int(num[1]), int(num[2])

if num1 > 10 and num2 > 10 and num3 > 10:
    if num1 % 3 == 0 and num2 % 3 == 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')
