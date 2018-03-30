'''
Вычислите значение выражения (x+1)2+3(x+1) при а) x=1.7; б) x=3.
Ответ: а) 15.39 б) 28
'''

x1, x2 = 1.7, 3
print(round(((x1 + 1) ** 2) + 3 * (x1 + 1), ndigits=2))
print(((x2 + 1) ** 2) + 3 * (x2 + 1))

'''
===============================================================================
'''

'''
Пользователь вводит три числа. Найдите среднее арифметическое этих чисел,
а также разность удвоенной суммы первого и третьего чисел и утроенного второго числа.
'''

numbers = input('Введите три числа через пробел: ').split(' ')
average = (int(numbers[0]) + int(numbers[1]) + int(numbers[2])) / len(numbers)
difference = ((int(numbers[0]) + int(numbers[1])) * 2) - (int(numbers[2]) * 3)
print(round(average), difference)

'''
===============================================================================
'''

'''
Даны три переменные a, b и c. Изменить значения этих переменных так,
чтобы в a хранилось значение a+b, в b хранилась разность старых значений c−a, 
а в c хранилось сумма старых значений a+b+c.
Например, a=0, b=2, c=5, тогда новые значения a=2, b=3 и c=7.
'''

# a = 0 new a = old a + old b = 2
# b = 2 new b = old c - new a = 3
# c = 5 new c = old a + old b + old c = 7

a = 0
b = 2
c = 5

a_2 = a + b
b_2 = c - a_2
c_2 = a + b + c

print(a_2, b_2, c_2)

'''
===============================================================================
'''

'''
Из трехзначного числа x вычли его последнюю цифру.
Когда результат разделили на 10, а к частному слева приписали последнюю цифру числа x, то получилось число 237.
Найти число x.
'''

'''
Трехзначное число  можно представить как [abc]  (квадратные скобки здесь и далее  обозначают запись числа по цифрам)
Результат (x1=237) получается путем выполнения следующих действий над числом х:
1. x1/10=[ab]
2. К результату 1 пункта приписываем слева последнюю цифру числа x, то есть c. Это и есть число 237.  x=[cab]=237
3. Из последнего необходимо найти цифры a, b, c и получить исходное число  x=[abc]. 
c=x1/100; a=x1/10%10; b=x1%10; 
Исходное число x=a*100+b*10+c;
'''

# 237 = 2 + 37
# 37 = 370 / 10
# x = 370 + 2

x1 = 237
c = x1 // 100
print(c)
a = x1 // 10 % 10
print(a)
b = x1 % 10
print(b)
x = a * 100 + b * 10 + c
print(x)

'''
===============================================================================
'''

'''
Дано два числа. Вывести наибольшее из них.
'''

number = input('Введи два числа через пробел: ').split(' ')
if int(number[0]) > int(number[1]):
    print(number[0])
if int(number[1]) > int(number[0]):
    print(number[1])
if int(number[0]) == int(number[1]):
    print('Числа равны')

'''
===============================================================================
'''

'''
Дано число. Если оно более 100 или менее -100, то занулить,
иначе увеличить его на 1.
'''

num = int(input('Введите значение: '))

'''
Вариант 1
'''
# if num >= 100 or num <= -100:
#     num = 0
#     print(num)
# else:
#     print(num + 1)

'''
Вариант 2
'''
# num = 0 if num >= 100 or num <= -100 else num + 1
# print(num)

'''
Вариант 3
'''
print(num + 1 if -100 <= num <= 100 else 0)

'''
===============================================================================
'''

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
print('начальное число - {0}.\nначинаем процесс увеличения числа "{0}" на 5... (Enter)'.format(num), end=''), input()
num += 1
print('1. число увеличено до {0}... (Enter)'.format(num), end=''), input()
num += 1
print('2. число увеличено до {0}... (Enter)'.format(num), end=''), input()
num += 1
print('3. число увеличено до {0}... (Enter)'.format(num), end=''), input()
num += 1
print('4. число увеличено до {0}... (Enter)'.format(num), end=''), input()
num += 1
print('5. число увеличено до {0}... (Enter)'.format(num), end=''), input()
print('процесс завершен!!! число увеличено до {0}... (Enter)'.format(num), end='') ,input()

'''
===============================================================================
'''

'''
Пользователь вводит три числа.
Если все числа больше 10 и первые два числа делятся на 3, то вывести yes, иначе no
'''

'''
Вариант 1
'''
num = input('Введите 3 числа через пробел: ').split(' ')

n1, n2, n3 = int(num[0]), int(num[1]), int(num[2])

if n1 and n2 and n3 > 10:
    if n1 % 3 == 0 and n2 % 3 == 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')

'''
===============================================================================
'''

'''
Пользователь вводит три числа. Найти сумму тех чисел, которые делятся на 5.
Если таких чисел нет, то вывести error.
'''

nums = input('Введите 3 числа через пробел: ').split()
summ = 0
n1, n2, n3 = int(nums[0]), int(nums[1]), int(nums[2])
if n1 % 5 == 0:
    summ += n1
if n2 % 5 == 0:
    summ += n2
if n3 % 5 == 0:
    summ += n3
print('error' if not summ else summ)

'''
===============================================================================
'''

