# todo: База данных пользователя.
# Задан массив объектов пользователя

#
# users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
#          {'login': 'Ivan',  'age': 10, 'group': "guest"},
#          {'login': 'Dasha', 'age': 30, 'group': "master"},
#          {'login': 'Fedor', 'age': 13, 'group': "guest"}]
#
# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.
#
# #Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе
#
# тип сортировки: 1
#
# #Затем сообщение для ввода
# Ввидите критерии поиска: 16
#
# Результат:
# #Пользователь: 'Piter' возраст 23 года , группа  "admin"
# #Пользователь: 'Dasha' возраст 30 лет , группа  "master"

users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

_type = int(input("Введите тип сортировки: "))
value = input("Ввeдите критерии поиска: ")
result = []

for row in users:
    match _type:
        case 1: #По возрасту
            if int(value) < row['age']:
                result.append(row)
        case 2: #По первой букве логина
            if value ==  row['login'][0]:
                result.append(row)
            pass
        case 3: #По группе
            if value ==  row['group']:
                result.append(row)
            pass
        case _:
            print('Неизвестный тип сортировки')
            exit(1);

for value in result:
    print(f"Пользователь: '{value['login']}' возраст {value['age']} года , группа  \"{value['group']}\"")




