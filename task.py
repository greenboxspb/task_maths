'''
Даны две переменных с некоторыми значениями. Поменять местами значения этих переменных
'''

a = input('Введите значение А: ')
b = input('Введите значение B: ')

a, b = b, a
print(a, b)
