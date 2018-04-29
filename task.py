'''
Выведите следующие строки.
Первая: 25  25.5  24.8.
Вторая: 26 26.5 25.8.  И так далее.
Последняя строка: 35 35.5 34.8.
'''


'''
через while
'''

nums = 25
while nums <= 35:
    print(nums, '{0} {1}'.format(nums + 0.5, nums - 0.2))
    nums += 1

'''
через for
'''

for nums in range(25, 36):
    print(nums, '{0} {1}'.format(nums + 0.5, nums - 0.2))