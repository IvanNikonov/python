# todo: Преобразуйте переменную age и foo в число
# age = "23"
# foo = "23abc"
#
# Преобразуйте переменную age в Boolean
# age = "123abc"
#
# Преобразуйте переменную flag в Boolean
# flag = 1
#
# Преобразуйте значение в Boolean
# str_one = "Privet"
# str_two = ""
#
# Преобразуйте значение 0 и 1 в Boolean
#
# Преобразуйте False в строку

age = "23"
foo = "23abc"
age = int(age)
foo = int(foo, 16)
print("Преобразуйте переменную age и foo в число")
print(type(age))
print(type(foo))
print(foo)

age = "123abc"
age = bool(age)
print("Преобразуйте переменную age в Boolean")
print(type(age))

flag = 1
flag = bool(flag)
print("Преобразуйте переменную flag в Boolean")
print(type(flag))

str_one = "Privet"
str_two = ""
str_one = bool(str_one)
str_two = bool(str_two)
print("Преобразуйте значение в Boolean")
print(type(str_one))
print(type(str_two))

str_one = 0
str_two = 1
str_one = bool(str_one)
str_two = bool(str_two)
print("Преобразуйте значение 0 и 1 в Boolean")
print(type(str_one))
print(type(str_two))

foo = False
foo = str(foo)
print("Преобразуйте False в строку")
print(type(foo))