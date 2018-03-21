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
if 7 <= num <= 40:
    print(num - 100)
if num < 0 or num > 3000:
    print(num * 3)
if 0 <= num <= 1 or num == 6 or 41 <= num <= 3000:
    num = 0
    print(num)


'''
Вариант 2
'''
'''
нет мыслей!
'''


# num = num + 10 if 2 <= num <= 5 else 0
# num = num - 100 if 7 <= num <= 40 else 0
# num = num * 3 if num < 0 or num > 3000 else 0
# print(num)

# print(num + 10 if 2 <= num <= 5 else 0, num - 100 if 7 <= num <= 40 else 0, num * 3 if num < 0 or num > 3000 else 0)

