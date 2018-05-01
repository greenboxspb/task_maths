'''
Вывести на экран фигуру из звездочек:
*******
*******
*******
*******
(квадрат из n строк, в каждой строке n звездочек)
'''

'''
через while
'''

user_line = int(input('Введите значение: '))

line = 0
while line < user_line:
    print('*' * user_line)
    line += 1

'''
через for
'''

user_num = int(input('Введите значение: '))

for new_line in range(user_num):
    print('*' * user_num)




