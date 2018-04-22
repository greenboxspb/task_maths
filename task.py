'''
Выведите на экран n раз фразу "Silence is golden". Число n вводит пользователь.
'''

n = int(input('Введите число: '))
sentence = 1
while sentence <= n:
    print('Silence is golden', sentence)
    sentence += 1
