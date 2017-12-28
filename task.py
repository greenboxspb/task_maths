'''
Даны катеты прямоугольного треугольника. Найдите площадь, периметр и гипотенузу треугольника.
'''

import math as m

cathetus_a = int(input('Катет треугольника A: '))
cathetus_b = int(input('Катет треугольника B: '))

area = 1/2 * cathetus_a * cathetus_b
hypotenuse = m.sqrt((cathetus_a ** 2) + (cathetus_b ** 2))
perimeter = cathetus_a + cathetus_b + hypotenuse

print('Площадь треугольника:', round(area))
print('Периметр треугольника:', round(perimeter))
print('Гипотенуза треугольника:', round(hypotenuse))
