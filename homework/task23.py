# todo: Шифр Цезаря
# Описание шифра.
# В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
# является одним из самых простых и широко известных методов шифрования.
# Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
# фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
# E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.
#
# Задача.
# Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
# циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
# В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
# В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.

letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
encode_message = []
f = open('message.txt', encoding='utf-8')
lines = f.readlines()
f.close()

for line_index in range(len(lines)):
    new_line = []

    for letter in lines[line_index]:
        lower_letter = letter.lower()
        is_big = not (lower_letter == letter)

        if letter.lower() in letters:
            new_letter = letters[letters.index(letter.lower()) - line_index - 1]
            new_line.append(new_letter.upper() if is_big else new_letter)
        else:
            new_line.append(letter)

    encode_message.append(''.join(new_line))
print(''.join(encode_message))



