#todo Задача 1. Чтение матрицы, load_matrix(filename)
# Дан файл, содержащий таблицу целых чисел вида
# (в каждой строке через пробел записаны числа)
#
# 11 12 13 14 15 16
# 21 22 23 24 25 26
# 31 32 33 34 35 36
#
#
# Требуется написать функцию load_matrix(filename) которая загружает эту таблицу из файла.
# Если в каждой строке находится одинаковое количество чисел, функция возвращает список списков целых чисел.
# В противном случае возвращает False.
#
# Задачу следует решить с использованием списковых включений, циклы использовать НЕЛЬЗЯ!
def load_matrix(filename):
    f = open(filename, 'rt', encoding='utf-8')
    rows = f.readlines()
    f.close()
    result = [[int_ for int_ in row.replace('\n', '').split(' ')]  for row in rows]
    count = set(
        map(
            lambda list_: len(list_),
            result
        )
    )
    return False if len(count) > 1 else result

print(load_matrix('matrix.txt'))