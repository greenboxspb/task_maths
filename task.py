'''
Вывести на экран ряд чисел 1001,  1004,  1007,  ... 1025.
'''

nums = 1001
list_nums = []
while nums < 1025:
    list_nums.append(str(nums))
    nums += 3
print(', '.join(list_nums) + '{0}'.format(', 1025.'))

