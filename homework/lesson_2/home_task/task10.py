# todo: 10.1 Дано целое число A. Проверить истинность высказывания: «Число A является четным».
# todo: 10.2 Дано целое число A. Проверить истинность высказывания: «Число A является нечетным».
# Примечание: В задании  требуется вывести логическое значение True, если выражение
# для введеных исходных данных является истинным, и значение False в противном случае.

#10.1
number_a = int(input("Введите число A: "))
print(number_a % 2 == 0)

#10.2
number_a = int(input("Введите число A: "))
print(number_a % 2 != 0)