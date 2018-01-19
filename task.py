'''
Вычислите √‾‾‾x−√y, если x и y вводит пользователь.
Перед вычислением выполнить проверку на существование квадратных корней.
'''

import math as m

x = int(input('Введите значение X: '))
if x < 0:
    print('Ошибка. Введите положительное число.')
y = int(input('Введите значение Y: '))
if y < 0:
    print('Ошибка. Введите положительное число.')

decision = m.sqrt(x - m.sqrt(y))
if decision.is_integer() is True:
    print(round(decision))

else:
    print(decision)
