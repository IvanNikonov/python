#todo: Модифицировать программу таким образом чтобы она выводила
#  приветствие "Hello", которое до этого записано в файл text.txt
#  через метод write()
FILE_NAME = "text.txt"

f = open(FILE_NAME, "w+t")
f.write("Hello\n")
f.close()

f = open(FILE_NAME, "rt")
print(f.read())
f.close()

