#todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.
#
# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!
letters = ' abcdefghijklmnopqrstuvwxyz'
str_list = ['8 5 12 12 15', '8 5 12 12 15 , 0 23 15 18 12 4 !']

for str_ in str_list:
    str_ = str_.split(' ')
    str_ = ''.join([letters[int(letter)] if letter.isdigit() else letter for letter in str_])
    print(str_)
