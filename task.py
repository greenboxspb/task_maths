'''
Пользователь вводит три числа. Найдите среднее арифметическое этих чисел,
а также разность удвоенной суммы первого и третьего чисел и утроенного второго числа.
'''

numbers = input('Введите три числа через пробел: ').split(' ')
average = (int(numbers[0]) + int(numbers[1]) + int(numbers[2])) / len(numbers)
difference = ((int(numbers[0]) + int(numbers[1])) * 2) - (int(numbers[2]) * 3)
print(round(average), difference)
