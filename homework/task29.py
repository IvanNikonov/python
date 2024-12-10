from datetime import datetime
from pprint import pprint


#todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.
def counter(func):

    def wrapper(*args, **kwargs):
        f = open('debug.log', 'r+')
        is_new = True
        rows = []
        separator = ", "
        while True:
            row = f.readline().replace('\n', '')
            if not row:
                break

            row = row.split(separator)
            if(row[0] == func.__name__):
                row[1] = str(int(row[1]) + 1)
                row[2] = datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S')
                is_new = False

            row = separator.join(row) + '\n'
            rows.append(row)

        if is_new:
            rows.append(separator.join(
                [
                    func.__name__,
                    str(1),
                    datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S'),
                ]
            ) + '\n')

        f.seek(0)
        f.writelines(rows)
        func(*args, **kwargs)
        f.close()
    return wrapper

@counter
def show():
    print("Вызов функции show")

@counter
def render():
    print("Вызов функции render")

show()
render()