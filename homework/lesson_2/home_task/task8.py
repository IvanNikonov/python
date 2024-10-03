# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково слева направо и справа налево".

number_string = input("Введите четырехзначное число: ")

if len(number_string) != 4:
    print('Вы ввели не четырехзначное число')
    exit()

print(
    number_string[0] == number_string[-1]
    and number_string[1] == number_string[-2]
)