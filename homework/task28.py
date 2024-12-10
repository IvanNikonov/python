#todo: Реализовать в игре "Поле чудес" возможность сохранять состояние игры (save game).
# Пользователю должна быть предоставлена возможность восстановиться из файла сериализации.

import random
import pickle
import os

obj = {'word_index': None,
       'field': None,
       'attempt': None,
       'name_save_game': None}

words = [
    "оператор",
    "конструкция",
    "объект"
]

desc_  = [
    "Символ или ключевое слово используемое для операций над данными",
    "Определение слова конструкция",
    "Экземпляр класса с определенными значениями для его атрибутов"
]

def init(word_index = random.randint(0, len(words) - 1), field = '', attempts = 10):
    global words
    global desc_
    word = words[word_index]
    description = desc_[word_index]

    if field == '':
        field = ['▒'] * len(word)

    return (word, description, field, attempts, word_index)

def run(word, description, field, attempts, word_index):
    global obj

    print(description)
    print(' '.join(field))

    while '▒' in field:

        if(attempts == 0):
            print("Вы проиграли")
            break

        letter = input("Введите букву: ")

        if letter == "0":
            name_save_game = str(input('Сохранить как: '))
            obj['word_index'] = word_index
            obj['attempts'] = attempts
            obj['field'] = field
            obj['name_save_game'] = name_save_game
            with open('./savegame/' + name_save_game + '.pkl', 'wb') as fp:
                pickle.dump(obj, fp)
                print("Ваша игра записана!")
            exit(0)

        if letter not in word:
            attempts -= 1
            print("Нет такой буквы")
            print(f"У вас осталось {attempts} попыток !")
            continue


        for key in range(len(word)):
            if word[key] == letter:
                field[key] = letter
        print(' '.join(field))
    else:
        print("Вы победили")

menu = """
    1. Начать игру 
    2. Загрузить игру
    0. Сохранить игру
"""
print(menu)
пункт_меню = int(input('Введите пункт меню: '))
match пункт_меню:
    case 1:
        res = init()
        run(*res)
    case 2:
        dir_ = os.listdir('./savegame')
        for file in dir_:
            print(file)
        name_save_game = str(input('Введите файл: '))
        with open('./savegame/' + name_save_game, "rb") as f:
            obj = pickle.load(f)
        res = init(obj['word_index'], obj['field'], obj['attempts'])
        print(f"Игра {obj['name_save_game']} восстановлена! ")
        run(*res)