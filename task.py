'''
Дано два числа. Вывести наибольшее из них.
'''


number = input('Введи два числа через пробел: ').split(' ')
if int(number[0]) > int(number[1]):
    print(number[0])
if int(number[1]) > int(number[0]):
    print(number[1])
if int(number[0]) == int(number[1]):
    print('Числа равны')

