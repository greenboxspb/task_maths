'''
Пользователь вводит номер месяца. Вывести название поры года (весна, лето и т.д.)
'''

month = int(input('Введите цифру месяца: '))


'''
Вариант 1
'''

if 1 <= month <= 2 or month == 12:
    print('Winter')
if 3 <= month <= 5:
    print('Spring')
if 6 <= month <= 8:
    print('Summer')
if 9 <= month <= 11:
    print('Autumn')
if month <= 0 or month >= 13:
    print('Ошибка, введите значение от 1 до 12')
