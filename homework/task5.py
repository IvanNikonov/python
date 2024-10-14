#todo: Написать программу, которая считывает два числа и выводит их сумму, разность, частное, произведение,
# результат целочисленного деления, результат деления с остатком, результат возведения в степень.

first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

print(f"Сумма: {first_number + second_number}")
print(f"Разность: {first_number - second_number}")
print(f"Частное: {first_number / second_number}")
print(f"Произведение: {first_number * second_number}")
print(f"Целочисленное деление: {first_number // second_number}")
print(f"Остаток от деления: {first_number % second_number}")
print(f"Возведение в степень: {first_number ** second_number}")

