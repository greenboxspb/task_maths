'''
Дано трехзначное число. Переставьте первую и последнюю цифры.
'''

nums = list(input('Введите трехзачное число: '))

nums[0], nums[2] = nums[2], nums[0]
print(' '.join(nums))