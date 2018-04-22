'''
Дано четырехзначное число. Поменяйте местами наименьшую и наибольшую цифры.
Например: 1234 4231
'''

nums = list(input('Введите четырехзначное число: '))

new_nums = nums.copy()
new_nums.sort()
min_num, big_num = nums.index(new_nums[0]), nums.index(new_nums[3])
nums[min_num], nums[big_num] = nums[big_num], nums[min_num]
print(nums)
