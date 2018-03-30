'''
Даны три числа. Найдите наибольшее число из них.
'''

nums = input('Введите 3 числа через пробел: ').split(' ')

a, b, c = int(nums[0]), int(nums[1]), int(nums[2])


if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)
