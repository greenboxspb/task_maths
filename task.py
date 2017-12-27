'''
Вычислите значение выражения |x−5|−sinx/3 + √x^2+2014 * cos2x−3 при x=−2.34. Ответ: -1.76911
'''

'''
|x−5|−sinx/3 + √x^2+2014 * cos2x−3 при x=−2.34. Ответ: -1.76911
'''

import math as m

x = -2.34
step_1 = abs(x - 5)
step_2 = step_1 - m.sin(x)
step_3 = step_2 / 3
step_4 = m.sqrt((x ** 2) + 2014)
step_5 = (step_4 * (m.cos(2 * x))) - 3
step_6 = step_3 + step_5
print(round(step_6, ndigits=5))

print(round(((abs(x - 5) - m.sin(x)) / 3) + (((m.sqrt((x ** 2) + 2014)) * (m.cos(2 * x))) - 3), ndigits=5))

