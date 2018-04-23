'''
Вывести на экран фигуру из звездочек:
*******
*******
*******
*******
(квадрат из n строк, в каждой строке n звездочек)
'''

user_line = int(input('Введите количество строк: '))
symbol_asterisk = int(input('Введите количество звездочек: '))

line = 0
while line < user_line:
    print('*' * symbol_asterisk)
    line += 1
