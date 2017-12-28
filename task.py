'''
                          sin^3(x + a)
  √^5(x^2 + b) - b^2 *    —————————-----
                            x
'''

import math as m

x = 1
a = 0.1
b = 0.2

step_1 = x ** 2 + b
print(step_1)
step_2 = m.sqrt(step_1) ** 5
print(step_2)
step_3 = m.sin(x + a) ** 3
print(step_3)
step_4 = step_3 / x
print(step_4)
step_5 = (b ** 2) * step_4
print(step_5)
step_6 = step_2 - step_5
print(step_6)

print((m.sqrt(x ** 2 + b) ** 5) - (b ** 2) * ((m.sin(x + a) ** 3) / x))