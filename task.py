'''
Дано четырехзначное число. Определите, есть ли одинаковые цифры в нем.
'''

nums = list(input('Введите четырехзначное число: '))
number_1, number_2, number_3, number_4 = int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3])

if number_1 == number_2 or number_1 == number_3 or number_1 == number_4:
    print('В числе есть одинаковые цифры')
elif number_2 == number_3 or number_2 == number_4:
    print('В числе есть одинаковые цифры')
elif number_3 == number_4:
    print('В числе есть одинаковые цифры')
else:
    print('В числе НЕТ одинаковых цифр')


'''
Вариант № 2
'''

nums = input('Введите четырехзначное число: ')

if int(nums[0]) == int(nums[1]) or int(nums[0]) == int(nums[2]) or int(nums[0]) == int(nums[3]):
    print('В числе есть одинаковые цифры')
elif int(nums[1]) == int(nums[2]) or int(nums[1]) == int(nums[3]):
    print('В числе есть одинаковые цифры')
elif int(nums[2]) == int(nums[3]):
    print('В числе есть одинаковые цифры')
else:
    print('В числе НЕТ одинаковых цифр')