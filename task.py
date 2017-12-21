'''
Пользователь вводит два числа. Найдите сумму и произведение данных чисел.
'''

number = input('Введите 2 чила через пробел: ').split(' ')
amount = int(number[0]) + int(number[1])
multiply = int(number[0]) * int(number[1])
print(amount, multiply)
