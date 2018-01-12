'''
Пользователь вводит сумму вклада в банк и годовой процент.
Найдите сумму вклада через 5 лет (рассмотреть два способа начисления процентов)
'''

money = int(input('Введите сумму вклада: '))
percent = int(input('Введите процент: '))

result_year = money + (((money / 100) * percent) * 5)
print(result_year)

result_month = money + ((((money / 100) * percent) / 12) * 60)
print(result_month)

# сложный процент "с ежегодной капитализацией процентов"
res = money * ((1 + (percent / 100)) ** 5)
print(res)