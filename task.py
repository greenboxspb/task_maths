'''
Пользователь вводит четыре числа.
Найдите наибольшее четное число среди них.
Если оно не существует, выведите фразу "not found"
'''

num = input('Введите четыре числа через пробел: ').split(' ')
n1, n2, n3, n4 = int(num[0]), int(num[1]), int(num[2]), int(num[3])

if n1 % 2 == 0 and n1 > n2 and n1 > n3 and n1 > n4:
    print(n1)
elif n2 % 2 == 0 and n2 > n1 and n2 > n3 and n2 > n4:
    print(n2)
elif n3 % 2 == 0 and n3 > n1 and n3 > n2 and n3 > n4:
    print(n3)
elif n4 % 2 == 0 and n4 > n1 and n4 > n3 and n4 > n2:
    print(n4)
else:
    print('not found')

