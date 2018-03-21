'''
Пользователь вводит два числа. Если они не равны 10 и первое число четное,
то вывести их сумму, иначе вывести их произведение.
'''


'''
Вариант 1
'''

num = input('Введите два числа через пробел: ').split(' ')


number = int(num[0])
number2 = int(num[1])
if number != 10 and number2 != 10 and number2 % 2 == 0:
    print(number + number2, 'a')
else:
    print(number * number2, 'b')

'''
Вариант 2
'''

# number = int(num[0])
# number2 = int(num[1])
# number = number + number2 if number != 10 and number2 != 10 and number2 % 2 == 0 else number * number2, 'a'
# print(number)
