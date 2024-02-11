"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""


number = int(input('Введите целое число: '))
hex_digits = "0123456789ABCDEF"
hex_number = ""
print(hex(number))

while number > 0:
    remainder = number % 16
    hex_digit = hex_digits[remainder]
    hex_number = hex_digit + hex_number
    number //= 16

print(f"Щестнадцатеричное строковое представление числа: {hex_number}")


