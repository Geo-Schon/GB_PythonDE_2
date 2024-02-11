"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение дробей. Для проверки своего кода используйте модуль fractions
"""
from fractions import Fraction


def gcd(num, den):
    if den == 0:
        return num
    else:
        return gcd(den, num % den)


def multiply(num1, den1, num2, den2):
    num = num1 * num2
    den = den1 * den2
    common_factor = gcd(num, den)
    num //= common_factor
    den //= common_factor
    return (num, den)


def add(numer1, denom1, numer2, denom2):
    common_numer = numer1 + numer2
    common_denom = denom1 + denom2
    return (common_numer, common_denom)


num_1 = int(input("Введите числитель первой дроби: "))
den_1 = int(input("Введите знаменатель первой дроби: "))
num_2 = int(input("Введите числитель второй дроби: "))
den_2 = int(input("Введите знаменатель второй дроби: "))

numerator, denominator = multiply(num_1, den_1, num_2, den_2)
summa_num, summa_den = add(num_1, den_1, num_2, den_2)

print(f"Сумма дробей {num_1}/{den_1} и {num_2}/{den_2} = {summa_num}/{summa_den}")
print(f"Произведение дробей {num_1}/{den_1} и {num_2}/{den_2} = {numerator}/{denominator}")

print(f'{Fraction(num_1, den_1) + Fraction(num_2, den_2)}')
print(f'{Fraction(num_1, den_1) * Fraction(num_2, den_2)}')
