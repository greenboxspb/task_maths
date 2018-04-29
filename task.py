'''
Выведите на экран числа 1, 2, 3, 4, ..., 20.
'''

'''
через while
'''

# nums = 1
# list_nums = []
# while nums < 20:
#     list_nums.append(str(nums))
#     nums += 1
# print(', '.join(list_nums) + '{0}'.format(', 20.'))

'''
через for
'''

for nums in range(1, 20):
    print(nums, end=', ')
print('20.')
