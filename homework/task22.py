#todo:  Задан файл dump.txt. Необходимо для заданного файла подсчитать статистику количества
# гласных букв в тексте.

#Формат вывода:
# Количество букв a - 13
# Количество букв o - 12
# Количество букв e - 11
# .....................

f = open('dump.txt', 'rt', encoding='utf-8')
text = f.read().lower()
f.close()

letters = "аоэеиыуёюя"



for single_letter in letters:
    print(f"Количество букв {single_letter} - {text.count(single_letter)}")

