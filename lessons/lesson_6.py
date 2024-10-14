# Задача 1

# file = open('lesson_6.py', "r+")
# print(file.read())
#
# if True:
#     test = 1
#
# file.close()

# Задача 2

import datetime

FILE_LOG = 'files/lesson_6/error.log'

def logger(message, error_type, line, code):
    file = open(FILE_LOG, 'a+', encoding="utf-8")
    error = f"{error_type}: {datetime.datetime.now()}: {code}: {__file__}: {line}: {message}"
    file.write(error + "\n")
    file.close()

logger(
    error_type = 'Warning',
    code = 777,
    line = 10,
    message = 'Test'
)