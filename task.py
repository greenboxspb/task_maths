'''
Дано четырехзначное число. Поменяйте местами наименьшую и наибольшую цифры.
Например: 1234 4231
'''

'''
без условий
'''

nums = list(input('Введите четырехзначное число: '))

# new_nums = nums.copy()
# new_nums.sort()
# min_num, big_num = nums.index(new_nums[0]), nums.index(new_nums[3])
# nums[min_num], nums[big_num] = nums[big_num], nums[min_num]
# print(nums)

'''
с условиями
'''

if nums[0] > nums[1] and nums[0] > nums[2] and nums[0] > nums[3]:
    if nums[1] < nums[2] and nums[1] < nums[3]:
        nums[0], nums[1] = nums[1], nums[0]
        print(nums, '1')
    elif nums[2] < nums[1] and nums[2] < nums[3]:
        nums[0], nums[2] = nums[2], nums[0]
        print(nums, '2')
    elif nums[3] < nums[1] and nums[3] < nums[2]:
        nums[0], nums[3] = nums[3], nums[0]
        print(nums, '3')

elif nums[1] > nums[0] and nums[1] > nums[2] and nums[1] > nums[3]:
    if nums[2] < nums[0] and nums[2] < nums[3]:
        nums[1], nums[2] = nums[2], nums[1]
        print(nums, '4')
    elif nums[0] < nums[2] and nums[0] < nums[3]:
        nums[1], nums[0] = nums[0], nums[1]
        print(nums, '5')
    elif nums[3] < nums[0] and nums[3] < nums[2]:
        nums[1], nums[3] = nums[3], nums[1]
        print(nums, '6')

elif nums[2] > nums[0] and nums[2] > nums[1] and nums[2] > nums[3]:
    if nums[3] < nums[0] and nums[3] < nums[1]:
        nums[2], nums[3] = nums[3], nums[2]
        print(nums, '7')
    elif nums[0] < nums[1] and nums[0] < nums[3]:
        nums[2], nums[0] = nums[0], nums[2]
        print(nums, '8')
    elif nums[1] < nums[0] and nums[1] < nums[3]:
        nums[2], nums[1] = nums[1], nums[2]
        print(nums, '9')

elif nums[3] > nums[0] and nums[3] > nums[1] and nums[3] > nums[2]:
    if nums[0] < nums[1] and nums[0] < nums[2]:
        nums[3], nums[0] = nums[0], nums[3]
        print(nums, '10')
    elif nums[1] < nums[0] and nums[1] < nums[2]:
        nums[3], nums[1] = nums[1], nums[3]
        print(nums, '11')
    elif nums[2] < nums[0] and nums[2] < nums[1]:
        nums[3], nums[2] = nums[2], nums[3]
        print(nums, '12')

