'''
Пользователь вводит номер месяца. Вывести название поры года (весна, лето и т.д.)
'''

month = int(input('Введите цифру месяца: '))


'''
Вариант 1
'''

if 1 <= month <= 2 or month == 12:
    print('Winter')
elif 3 <= month <= 5:
    print('Spring')
elif 6 <= month <= 8:
    print('Summer')
elif 9 <= month <= 11:
    print('Autumn')
else:
    print('Ошибка, введите значение от 1 до 12')


