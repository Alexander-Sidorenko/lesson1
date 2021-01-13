income = int(input('Введите сумму Вашего дохода в у.е.: '))
expenses = int(input('Введите сумму Ваших расходов в у.е.: '))
profit = income - expenses
if profit > 0:
    print('Ваша чистая прибыль составила: ', profit, 'у.е.')
    profitability = profit / income
    print('Рентабельность: ', profitability, '%')
    number = int(input('Давайте вычислим вклад каждого. Введите количество сотрудников в вашей компании: '))
    money = profit / number
    print('Каждый сотрудник принес компании: ', money, 'у.е.')
else: print('Ваши убытки составили: ', -profit, 'у.е.')
print('Будьте аккуратны! Необходимо пересмотреть бизнес-процессы')

