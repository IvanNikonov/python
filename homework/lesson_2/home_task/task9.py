# todo: Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0).
# Примечание: коэффициенты получаем через функцию input().

coefficient_a = int(input("Введите коэффициент A: "))

if coefficient_a == 0:
    print("коэффициент A не может быть равен нулю")
    exit()

coefficient_b = int(input("Введите коэффициент B: "))

result = -coefficient_b / coefficient_a
print(f"x равен {result}")