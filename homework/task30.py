#  1. Реализовать класс DB - синглтон. Экземляр класса(подключение) к PostgreSQL
#  должно быть единственным.

import psycopg2
from abc import ABC, abstractmethod

class DB:
    _instance = None
    _connection = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.connection = self.connect()

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                f"host={self.host} dbname={self.db} user={self.user} password={self.password}")
            return self.connection
        except Exception as e:
            print(Exception)
            print(e)

    @classmethod
    def get_instance(cls):
        return cls._instance


db1 = DB(host="PostgreSQL-16", port="5432", user="orm", password="tester", db="orm")
db2 = DB(host="PostgreSQL-16", port="5432", user="orm", password="tester", db="orm")
print(db1 is db2) #True
        

#  2. Реализовать  фабрику которая создает модели различных производителей

# 3. Реализовать для класса Car абстрактный класс который содержит
# aбстрактные методы sold, discount

class AbstractCar(ABC):
    brand = None
    model = None

    def __init__(self, model):
        self.model = model

    def __repr__(self):
        return f"Машина {self.brand}, модель {self.model}"

    @abstractmethod
    def sold(self):
        pass

    @abstractmethod
    def discount(self):
        pass

class Toyota(AbstractCar):
    brand = 'Toyota'

    def sold(self):
        print(f"Автомобиль {self.brand} {self.model} продан ")

    def discount(self):
        print(f"На автомобиль {self.brand} {self.model} скидка 5%")

class Lada(AbstractCar):
    brand = 'Lada'

    def sold(self):
        print(f"Автомобиль {self.brand} {self.model} в наличии ")

    def discount(self):
        print(f"На автомобиль {self.brand} {self.model} скидка 15%")

class Mercedes(AbstractCar):
    brand = 'Mercedes'

    def sold(self):
        print(f"Автомобиль {self.brand} {self.model} в наличии ")

    def discount(self):
        print(f"На автомобиль {self.brand} {self.model} скидка 50%")

class CarFactory:

    def make_lada(self, model):
        return Lada(model)

    def make_mercedes(self, model):
        return Mercedes(model)

    def make_toyota(self, model):
        return Toyota(model)

factory_cat = CarFactory()

car_lada = factory_cat.make_lada('Гранта')
car_toyota = factory_cat.make_toyota('Camry')
car_mercedes = factory_cat.make_mercedes('Benz')

print(car_lada)
print(car_toyota)
print(car_mercedes)

car_mercedes.sold()
car_mercedes.discount()