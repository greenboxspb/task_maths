'''
Дано три числа.
Если ровно два из них  меньше 5, то вывести yes, иначе вывести no.
'''

num = input('Введите три числа через пробел: ').split(' ')
n1, n2, n3 = int(num[0]), int(num[1]), int(num[2])

if not n1 == n2 == n3:
    if n1 == n2 or n2 == n3 or n1 == n3:
        if n1 < 5 and n2 < 5 and n3 < 5:
            print('yes')
        else:
            print('no')
    else:
        print('no')
else:
    print('no')


