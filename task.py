'''
Даны два трехзначных числа.
Найдите шестизначное число, образованное из двух данных чисел
путем дописывания второго числа к первому справа.
'''

numbers = input('Введите два трехзначных числа через пробел: ').split(' ')
print(numbers[1] + numbers[0])
