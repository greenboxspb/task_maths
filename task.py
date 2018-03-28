'''
Даны три числа.
Найдите те два из них, сумма которых наибольшая.
'''

a = 1
b = 1
c = 1

# if a < b and a < c:
#     print(b + c)
# elif b < a and b < c:
#     print(a + c)
# elif c < a and c < b:
#     print(a + b)



sum1 = a + b
sum2 = a + c
sum3 = b + c

if sum1 > sum2 and sum1 > sum3:
    print(a + b, '1')
if sum2 > sum1 and sum2 > sum3:
    print(a + c, '2')
if sum3 > sum1 and sum3 > sum2:
    print(b + c, '3')
if sum1 == sum2:
    print(a + b, '4')
elif sum2 == sum3:
    print(a + c, '5')
elif sum1 == sum3:
    print(a + b, '6')