#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.

from random import randint as ri

array = []

for i in range(10):
    array.append(ri(0, 9))

print(f"Дан массив: {array}")

for i in range(10):
    array[i] += 1

print(f"Результат: {array}")