'''
Пользователь вводит три числа. Увеличьте первое число в два раза, второе числа уменьшите на 3,третье число возведите в квадрат
и затем найдите сумму новых трех чисел.
'''

numbers = input('Введите 3 числа через пробел: ').split(' ')
print(numbers, type(numbers))
square = int(numbers[0]) ** 2
minus = int(numbers[1]) - 3
square2 = int(numbers[2]) ** 2
total = square + minus + square2
print(total)
