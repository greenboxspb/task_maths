'''
увеличить введенное число на 5,
увеличение числа должно происходить при нажатии на Enter,
ответ представить в виде:
начальное число - 4.
начинаем процесс увеличения числа "4" на 5... (Enter)
1. число увеличено до 5
2. число увеличено до 6
3. число увеличено до 7
4. число увеличено до 8
5. число увеличено до 9
процесс завершен!!! число увеличено до 9. (Enter)
*важное замечание, должно меняться именно вводимое число!
'''

num = int(input('Введите число: '))
num += 1
print('1. число увеличено до {0}'.format(num), end=''), input()
num += 1
print('2. число увеличено до {0}'.format(num), end=''), input()
num += 1
print('3. число увеличено до {0}'.format(num), end=''), input()
num += 1
print('4. число увеличено до {0}'.format(num), end=''), input()
num += 1
print('5. число увеличено до {0}\nпроцесс завершен!!! число увеличено до {0}'.format(num))
