from operator import index

#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.

# Пример:
mass = [1,2,17,54,30,89,2,1,6,2]
#
#
# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.

_set = set(mass)

for value in _set:
    if mass.count(value) == 1:
        print(f"Для числа {value} нет минимального расстояния т.к элемент в массиве один.")
        continue

    prev = -1
    summ = -1
    results = []

    for _index in range(len(mass)):
        if mass[_index] == value:
            if prev != -1:
                new_summ = _index - prev

                if(new_summ < summ or summ == -1):
                    summ = new_summ

            prev = _index



