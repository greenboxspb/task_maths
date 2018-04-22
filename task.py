'''
Дано четырехзначное число.
Переставьте местами цифры так, чтобы сначала оказались цифры, меньшие пяти.
'''

'''
если используем сортировку (хитрый способ, ведь не говориться как именно
нужно переставить местами цифры)
'''
# nums = list(input('Введите четырехзначное число: '))
#
# if int(nums[0]) < 5 or int(nums[1]) < 5 or int(nums[2]) < 5 or int(nums[3]) < 5:
#     nums.sort()
# print(''.join(nums))


'''
если используем копию списка и пустой список
'''
nums = list(input('Введите четырехзначное число: '))

new_nums = nums.copy()
nums_2 = []
if int(nums[0]) < 5:
    nums_2.append(nums[0])
    new_nums.remove(nums[0])
if int(nums[1]) < 5:
    nums_2.append(nums[1])
    new_nums.remove(nums[1])
if int(nums[2]) < 5:
    nums_2.append(nums[2])
    new_nums.remove(nums[2])
if int(nums[3]) < 5:
    nums_2.append(nums[3])
    new_nums.remove(nums[3])
print(''.join(nums_2 + new_nums))

