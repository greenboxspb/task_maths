'''
Известно, что x кг конфет стоит a рублей.
Определите, сколько стоит y кг этих конфет, а также сколько кг конфет можно купить на k рублей. Все значения вводит пользователь.
'''

x = int(input('Введите количество кг конфет: '))
a = int(input('Введите стоимость кг конфет: '))
y = int(input('Сколько будет стоить введеное количесво кг конфет: '))
print('{0} рублей - столько стоит {1} кг конфет'.format(y * a, y))
k = int(input('Сколько кг конфет можно купить на введеное количесво рублей: '))
print('{0} килограмм - столько конфет можно купить на {1} рублей'.format(round(k/a), k))