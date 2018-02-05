'''
Дано число. Если оно меньше 7, то вывести Yes, если больше 10, то вывести No, если равно 9, то вывести Error.
'''

num = int(input('Введите число: '))
if num == 9:
    print('Error')
elif num < 7 and num <= 10 and num != 9:
    print('Yes')
elif num > 10:
    print('No')
