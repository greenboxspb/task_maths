'''
Вывести на экран числа 100, 96, 92, ... до последнего положительного включительно.
'''

nums = 100
list_nums = []
while nums > 0:
    list_nums.append(str(nums))
    nums -= 4
print(', '.join(list_nums) + '{0}'.format(', 0.'))