'''
Дано число. Если оно от 2 до 5 включительно, то увеличить его на 10.
Если оно от 7 до 40, то уменьшить на 100.
Если оно не более 0 или более 3000, то увеличить в 3 раза (то есть умножить на 3).
Иначе занулить это число.
'''


num = int(input('Введите число: '))


'''
Вариант 1
'''

if 2 <= num <= 5:
    print(num + 10)
elif 7 <= num <= 40:
    print(num - 100)
elif num < 0 or num > 3000:
    print(num * 3)
else:
    print(0)

'''
Вариант 2
'''

if 2 <= num <= 5:
    print(num + 10)
else:
    if 7 <= num <= 40:
        print(num - 100)
    else:
        if num < 0 or num > 3000:
            print(num * 3)
        else:
            print(0)

