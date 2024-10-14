#Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
#Дан номер единицы массы и масса тела M в этих единицах (вещественное число). Вывести массу данного тела в килограммах.
# Данную задачу нужно решить с помощью конструкции  match  (Python v3.10)


# Пример:
# Введите единицу массы тела
#       1 - килограмм
#       2 — миллиграмм
#       3 — грамм
#       4 — тонна
#       5 — центнер
# >4

#Введите  массу тела
# >1

# Ответ: 1000 кг

unit = int(input("Введите единицу массы тела: "))
weight = float(input("Введите Массу тела: "))

match  unit:
    case 1: #килограмм
        pass
    case 2: #миллиграмм
        weight /= 1000000
    case 3: #грамм
        weight /= 1000
    case 4: #тонна
        weight *= 1000
    case 5: #центнер
        weight *= 100
    case _: #Неизвестная единица измерения
        print("Введена неизвестная единица измерения")
        exit()

print(f"{weight} кг")
