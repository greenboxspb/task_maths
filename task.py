'''
Выведите на экран числа 1.2, 1.4, 1.6, ..., 2.8.
'''

nums = 1.2
list_nums = []
while nums < 2.6:
    list_nums.append(str(nums))
    nums += 0.2
    nums = round(nums, 1)
print(', '.join(list_nums) + '{0}'.format(', 2.8.'))
