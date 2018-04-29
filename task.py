'''
Вывести на экран ряд чисел 1001,  1004,  1007,  ... 1025.
'''

'''
через while
'''

nums = 1001
list_nums = []
while nums < 1025:
    list_nums.append(str(nums))
    nums += 3
print(', '.join(list_nums) + '{0}'.format(', 1025.'))


'''
через for
'''

for nums in range(1001, 1025, 3):
    print(nums, end=', ')
print('1025.')