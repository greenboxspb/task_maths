'''
Выведите на экран прямоугольник из нулей.
Количество строк вводит пользователь, количество столбцов равно 5.
'''

'''
через while
'''

# user_string = int(input('Введите количество строк: '))
#
# line = 0
# while line < user_string:
#     print('0' * 5)
#     line += 1


'''
через for
'''

user_string = int(input('Введите количество строк: '))

for line in list(range(0, user_string)):
    print('0' * 5)
