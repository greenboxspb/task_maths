'''
Пользователь вводит время в минутах и расстояние в километрах. Найдите скорость в м/c.
'''

'''
Скорость — V     Путь — S     Время — t ;   V   =   S : t 
'''

minutes = int(input('Введите время в минутах: '))
seconds = minutes * 60
kilometers = int(input('Введите расстояние в километрах: '))
metres = kilometers * 1000

calculation = metres / seconds
print(round(calculation), 'м/с')

