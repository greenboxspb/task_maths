'''
Вычислите √‾‾‾x−√y, если x и y вводит пользователь.
Перед вычислением выполнить проверку на существование квадратных корней.
'''

import math as m

x = int(input('Введите значение X: '))
y = int(input('Введите значение Y: '))
if x < 0 or y < 0:
    print('Ошибка. Введите положительное число')
decision = m.sqrt(x - m.sqrt(y))
if decision.is_integer() is True:
    print(round(decision))
else:
    print(decision)
