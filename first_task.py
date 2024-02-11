"""
1. Напишите программу банкомат.
- Начальная сумма равна нулю. Допустимые действия: пополнить, снять, выйти
- Сумма пополнения и снятия кратны 50 у.е.
- Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
- После каждой третей операции пополнения или снятия начисляются проценты - 3%
- Нельзя снять больше, чем на счёте
- При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
- Любое действие выводит сумму денег
"""

def refill_withdraw(balance, count, mode, commission):
    money_commission = 0 + commission

    while True:
        money = int(input('Введите сумму пополнения (кратную 50): '))
        if money % 50 == 0:
            break
        else:
            print('Повторите попытку')

    if count == 3:
        money_commission += 0.03

    match mode:
        case 1:
            balance += (money - (money * money_commission))
        case 2:
            if money > balance:
                print('Ошибочная операция!')
                return balance
            if money * (0.015 + money_commission) <= 30:
                balance -= (money + 30)
            elif money * (0.015 + money_commission) >= 600:
                balance -= (money + 600)
            else:
                balance -= (money + (money * (0.015 + money_commission)))

    return balance


balance = 0
number_operations = 0
money_commission = 0

while True:
    print(f'\nВведите номер операции:\n'
      '1. Пополнить счет\n'
      '2. Снять деньги\n'
      '3. Показать баланс\n'
      '4. Выйти\n')

    mode = int(input('Введите номер операции: '))

    if balance >= 5_000_000:
        money_commission = 10

    match mode:
        case 1:
            balance = refill_withdraw(balance, number_operations, mode, money_commission)
            number_operations += 1
        case 2:
            if balance != 0:
                balance = refill_withdraw(balance, number_operations, mode, money_commission)
                number_operations += 1
            else:
                print('Нулевой баланс!')
        case 3:
            print(f'Ваш баланс: {balance}')
        case 4:
            break

