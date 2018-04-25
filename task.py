'''
Выведите на экран числа 1, 2, 3, 4, ..., 20.
'''

nums = 1
list_nums = []
while nums < 20:
    list_nums.append(str(nums))
    nums += 1
print(', '.join(list_nums) + '{0}'.format(', 20.'))
