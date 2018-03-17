'''
Дано число. Если оно более 100 или менее -100, то занулить,
иначе увеличить его на 1.
'''


num = int(input('Введите значение: '))

'''
Вариант 1
'''
# if num >= 100 or num <= -100:
#     num = 0
#     print(num)
# else:
#     print(num + 1)

'''
Вариант 2
'''
# num = 0 if num >= 100 or num <= -100 else num + 1
# print(num)

'''
Вариант 3
'''
print(num + 1 if -100 <= num <= 100 else 0)
