# import time
#
# def time_execute (func):
#     def wrapper(list_):
#         time_start = time.time()
#         func(list_)
#         print(f"Время выполнения функции: {time.time() - time_start}")
#     return wrapper
#
# test_list = range(100000000)
#
# @time_execute
# def list_sum(list_):
#     sum_ = 0
#     for i in range(len(list_)):
#         sum_ += list_[i]
#     print(sum_)
#
# list_sum(test_list)
#
# @time_execute
# def list_sum2(list_):
#     print(sum(list_))
#
# list_sum2(test_list)
#

class Cache:
    def __init__(self):
        self.__storage = {}

    @property
    def storage(self):
        return self.__storage

    @storage.setter
    def storage(self, dict_):
        key, value = dict_
        self.__storage[key] = value

    def storage_by_key(self, key):
        return self.__storage[key] if key in self.storage else None

cache = Cache()

cache.storage = ('token', 'dasdasdasdadaadadadadadad')
print(cache.storage)
print(cache.storage_by_key('token'))
