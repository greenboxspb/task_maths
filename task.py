'''
Вычислите значение выражения e^x−2+|sin(x)|−x^10*cos*1/x при x=3.6
'''

import math as m

x = 3.6
step_1 = (m.e) ** (x -2)
print(step_1)
step_2 = m.fabs(m.sin(x))
print(step_2)
step_3 = (x ** 10) * m.cos(1/x)
step_4 = step_1 + step_2
step_5 = step_4 - step_3
print(step_5)
