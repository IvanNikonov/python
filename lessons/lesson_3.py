# import random

# random_number = random.randint(1, 100)
# attempt = 5
#
# for i in range(attempt, 0, -1):
#     input_number = int(input("Введите число: "))
#
#     if input_number == random_number:
#         print('Вы победили')
#         exit()
#     elif input_number > random_number:
#         print(f"Искомое число меньше! Осталось попыток: {i - 1}")
#     else:
#         print(f"Искомое число больше! Осталось попыток: {i - 1}")
#
# print("Вы проиграли")

word = "арбузабуза"
m_word = list("арбузабуза")
field = ['x'] * len(word)

while 'x' in field:
    letter = input("Введите букву: ")

    for key in range(len(word)):
        if word[key] == letter:
            field[key] = letter
    print(field)
else:
    print('Игра закончена')




