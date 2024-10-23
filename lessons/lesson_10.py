from requests import get, post, put, delete

# Анонимные функции
# list_ = [10, 11, 14, 25, 33, 36, 100, 101]
# func = lambda val: val % 2 == 1
# print(list(filter(func, list_)))

# Генераторы

# print([x**2 for x in range(0, 50) if x % 3])

# Вложенная генерация

# matrix = [[i for i in range(5)] for _ in range(5)]
#
# print(matrix)

# Генератор словарей
# list_ = [10, 23, 4, 56, -10]
#
# for key, val in { i: list_[i] for i in range(len(list_))}.items():
#     print(f"key: {key} value: {val}")
access_token = "y0_AgAAAAAD_-_pAAyipgAAAAEVCTU3AABBkGBJza1Nqpy8C7qG84PBDu557Q"

def upload_files_disk(file):
    global access_token
    headers = {"Authorization": f"OAuth {access_token}"}
    params = {"path": f"{file}"}
    r = get("https://cloud-api.yandex.net/v1/disk/resources/upload",
            headers=headers, params=params)
    href = r.json()["href"]
    files_ = {"file": open(f"files/playlist/{file}", "rb")}
    r = put(href, files = files_)

files = ['file.mp3', 'file.txt', 'file.pdf', 'file2.mp3', 'file.doc']
mp3 = [file for file in files if file[-3:] == 'mp3']

list(map(upload_files_disk, mp3))