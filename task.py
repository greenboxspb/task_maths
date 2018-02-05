'''
Дано два числа. Вывести yes, если они отличаются на 100, иначе вывести No.
'''

number = input('Введите числа через пробел: ').split(' ')
if (int(number[0]) - int(number[1])) > 100 or (int(number[1]) - int(number[0])) > 100:
    print('Yes')
else:
    print('No')
