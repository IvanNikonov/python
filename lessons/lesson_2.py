# Тернарная операция

# x = 50
# y = 120
# z = x if x > y else y
# print(z)

# | - pipe


# month = input("Введите номер месяца: ")
#
# match int(month):
#     case 1 | 2 | 12:
#         print("Зима")
#     case 3 | 4 | 5:
#         print("Весна")
#         pass
#     case 6 | 7 | 8:
#         print("Лето")
#         pass
#     case 9 | 10 | 11:
#         print("Осень")
#         pass
#     case _:
#         print("Месяца не существует")

# month = 12
#
# def _summ(l_month):
#     return l_month % 10 + l_month // 10

# def _summ(l_month):
#     return int(str(l_month)[0]) + int(str(l_month)[1])

# test
# result = _summ(month)
# print(result)
# assert 4 == result
