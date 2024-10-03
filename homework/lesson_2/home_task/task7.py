#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().

point_a = int(input('Введите точку A: '))
point_b = int(input('Введите точку B: '))
point_c = int(input('Введите точку C: '))

segment_ac = point_a + point_c
segment_bc = point_b + point_c

print(f"Длина отрезка AC: {segment_ac}")
print(f"Длина отрезка BC: {segment_bc}")
print(f"Сумма отрезков AC и BC: {segment_ac + segment_bc}")
