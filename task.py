'''
Пользователь вводит три числа. Найти сумму тех чисел, которые делятся на 5.
Если таких чисел нет, то вывести error.
'''


nums = input('Введите 3 числа через пробел: ').split()
summ = 0
n1, n2, n3 = int(nums[0]), int(nums[1]), int(nums[2])
if n1 % 5 == 0:
    summ += n1
if n2 % 5 == 0:
    summ += n2
if n3 % 5 == 0:
    summ += n3

print('error' if not summ else summ)

