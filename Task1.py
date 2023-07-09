"""
Задание №6.
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""

def main():
    # Запрос текущего депозита
    start_sum = check_balance()
    num_operation = 0
    operation = True
    while operation:
        # Проверка на богатство. Даже для ошибочных операций вычитает 10%
        start_sum = check_rich(start_sum)
        # Вывод баланса
        rounded_sum = round(start_sum, 2)
        print(f"Текущий баланс - {rounded_sum}")
        # Выбор действия (внести/снять)
        x, msg = action()
        print(msg)
        if x == 1:
            # Счетчик успешной операции
            num_operation += 1
            # Получаем сумму для операции
            sum_operation = check_amount(x)
            # Если сумма операции = 0, то шаг не засчитывается
            if sum_operation == 0:
                num_operation -= 1
            # Вычисляем результат операции
            start_sum = deposit_cash(sum_operation, start_sum)
            # Проверяем номер операции
            bonus = bonus_operation(num_operation)
            if bonus:
                # Начисляем процент за каждую 3 операцию
                start_sum = sum_balance_bonus(start_sum, bonus)
        elif x == 2 and start_sum > 0:
            # Счетчик успешной операции
            num_operation += 1
            # Получаем сумму для операции
            sum_operation = check_amount(x)
            # Если сумма операции = 0, то шаг не засчитывается
            if sum_operation == 0:
                num_operation -= 1
            # Проверка на превышение лимита доступных средств
            if sum_operation > start_sum:
                print("\nНедостаточно средств!")
                num_operation -= 1
            else:
                # Вычисляем результат операции
                start_sum = withdraw_cash(sum_operation, start_sum)
            # Проверяем номер операции
            bonus = bonus_operation(num_operation)
            if bonus:
                # Начисляем процент за каждую 3 операцию
                start_sum = sum_balance_bonus(start_sum, bonus)
        elif x == 3:
            operation = False
        elif x == 2 and start_sum <= 0:
            print("\nНедостаточно средств. Вы можете только пополнить баланс")
            continue


def action():
    """
    ✔ Допустимые действия: пополнить, снять, выйти
    :return: x = int, msg = string
    """
    x = int(input("\nВыберете действие: \n1 - Внести на счет\n2 - Снять со счета\n3 - Выйти\n"))
    msg = ''
    if x == 1:
        msg = "\nВы выбрали Внести!"
    elif x == 2:
        msg = "\nВы выбрали Снять!"
    elif x == 3:
        msg = "\nВыйти"
    else:
        msg = "\nТакой команды нет!"
    return x, msg


def check_amount(action):
    """
    ✔ Сумма пополнения и снятия кратны 50 у.е.
    :param action: int
    :return: int
    """
    if action == 1:
        prompt = "\nСколько хотите внести? Введите сумму кратную 50 у.е: "
    elif action == 2:
        prompt = "\nСколько хотите снять? Введите сумму кратную 50 у.е: "
    else:
        return 0

    while True:
        n = int(input(prompt))
        if n == 0:
            print("\nВы ввели 0. Никаких операций не произведено")
        elif n % 50 == 0:
            return n
        else:
            print("\nСумма должна быть кратной 50 у.е. Попробуйте еще раз.")


def deposit_cash(value, curr_dep):
    """
    Отвечает за внесение на счет
    :param value: int
    :param curr_dep: int
    :return: int
    """
    new_balance = curr_dep + value
    return new_balance


def withdraw_cash(value, curr_dep):
    """
    Отвечает за снятие со счета
    :param value: int
    :param curr_dep: int
    :return: int
    """
    chp = percentage_for_withdrawal(value)
    # value -= chp
    new_balance = curr_dep - chp
    return new_balance


def check_balance():
    """
    ✔ Начальная сумма равна нулю
    :return: int
    """
    return 0


def percentage_for_withdrawal(value: int):
    """
    ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
    :param value: int
    :return: int
    """
    percent = 0.015
    if 30 <= value <= 600:
        result = value + value * percent
        print(f"Комиссия 1.5% от суммы снятия. Вы сняли {value}у.е., комиссия - {value * percent} у.е.")
    else:
        result = value
    return result


def bonus_operation(step: int):
    """
    Проверяет на каждую 3 операцию
    :param step: int
    :return: int
    """
    bo = 3
    percent = 0
    if step % bo == 0:
        percent = bo
        return percent
    else:
        return percent


def sum_balance_bonus(balance, bonus):
    """
    ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
    :param balance: int
    :param bonus: int
    :return: int
    """
    result = balance + balance * bonus/100
    print(f"Вам начислен бонус {bonus}%")
    return result


def check_rich(value):
    """
    ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
    операцией, даже ошибочной.
    :param value: int
    :return: int
    """
    if value > 5_000_000:
        tax = value * 0.1
        value -= tax
        print(f"Снят налог на богатство 10%!")
    return value


if __name__ == '__main__':
    main()
