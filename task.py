'''
Дано два числа. Если хотя бы одно из них больше 30, то вывести yes, иначе no.
'''

num = input('Введите два числа через пробел: ').split(' ')
n1, n2 = int(num[0]), int(num[1])

if n1 > 30 or n2 > 30:
    print('yes')
else:
    print('no')

print('yes') if n1 > 30 or n2 > 30 else print('no')