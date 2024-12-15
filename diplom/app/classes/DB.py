from os import getenv
from app.classes.Utils import Utils
import psycopg2


class DB:
    _instance = None
    _connection = None

    @classmethod
    def test(cls):
        return "test"

    @classmethod
    def get_instance(cls):
        return cls()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.host = getenv("DB_HOST")
        self.port = getenv("DB_PORT")
        self.user = getenv("DB_USER")
        self.password = getenv("DB_PASSWORD")
        self.db = getenv("DB_NAME")
        self._connection = self.connect()

    def connect(self):
        try:
            return psycopg2.connect(
                f"host={self.host} dbname={self.db} user={self.user} password={self.password}")
        except Exception as e:
            print(Exception)
            print(e)

    def get_cursor(self, sql):
        cur = self._connection.cursor()
        cur.execute(sql)
        return cur

    def select_one(self, sql):
        cur = self.get_cursor(sql)
        sql_tuple = cur.fetchone()
        sql_name = list(map(lambda element: element.name, cur.description))

        if sql_tuple is None:
            return None

        return Utils.combine_lists(sql_name, sql_tuple)

    def select_all(self, sql):
        cur = self.get_cursor(sql)
        sql_list = cur.fetchall()
        sql_name = list(map(lambda element: element.name, cur.description))
        result_list = []
        if sql_list is None:
            return None

        for row in sql_list:
            result_list.append(Utils.combine_lists(sql_name, row))

        return result_list

    def execute(self, sql, insert=False):
        cur = self.get_cursor(sql)
        self._connection.commit()

        if insert:
            return cur.fetchone()[0]

        return cur.rowcount
