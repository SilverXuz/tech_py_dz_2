"""
✔ Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
Программа должна возвращать сумму и *произведение дробей. Для проверки своего кода используйте модуль fractions.
"""

from fractions import Fraction


def main():
    fraction1 = input("Введите первую дробь в формате a/b: ")
    fraction2 = input("Введите вторую дробь в формате a/b: ")

    sum_result, multiply_result = manual_fraction_calculation(fraction1, fraction2)
    print("\nСумма дробей:", sum_result)
    print("Произведение дробей:", multiply_result)

    print("\nПроверка через модуль fractions")
    f_sum_result, f_multiply_result = fraction_calculation_with_module(fraction1, fraction2)
    print("Сумма дробей:", f_sum_result)
    print("Произведение дробей:", f_multiply_result)


def manual_fraction_calculation(fraction1, fraction2):
    numerator1, denominator1 = map(int, fraction1.split('/'))
    numerator2, denominator2 = map(int, fraction2.split('/'))

    # Вычисление суммы дробей
    sum_numerator = numerator1 * denominator2 + numerator2 * denominator1
    sum_denominator = denominator1 * denominator2
    sum_fraction = f"{sum_numerator}/{sum_denominator}"

    # Вычисление произведения дробей
    multiply_numerator = numerator1 * numerator2
    multiply_denominator = denominator1 * denominator2
    multiply_fraction = f"{multiply_numerator}/{multiply_denominator}"

    return sum_fraction, multiply_fraction


def fraction_calculation_with_module(fraction1, fraction2):
    fraction_obj1 = Fraction(fraction1)
    fraction_obj2 = Fraction(fraction2)

    # Вычисление суммы дробей
    sum_fraction = fraction_obj1 + fraction_obj2

    # Вычисление произведения дробей
    multiply_fraction = fraction_obj1 * fraction_obj2

    return str(sum_fraction), str(multiply_fraction)


if __name__ == '__main__':
    main()
