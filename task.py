'''
Дан прямоугольник размером 647 x 170. Сколько квадратов со стороной 30 можно вырезать из него?
'''

import math as m

s_rectangle = 647 * 170
s_square = 30 * 30
print(m.floor(s_rectangle / s_square))
