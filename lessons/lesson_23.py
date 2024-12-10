import psycopg2
import config

class Db:

    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.connection = self.connect()

    def connect(self):
        try:
            self.connection = psycopg2.connect(f"host={self.host} dbname={self.db} user={self.user} password={self.password}")
            return self.connection
        except Exception as e:
            print(Exception)
            print(e)

    def select(self, sql):
        try:
            cur = self.connection.cursor()
            cur.execute(sql)
        except Exception as e:
            pass
        else:
            self.connection.commit()
            return cur.fetchall()

    def insert_one(self, sql, data):
        pass

    def insert_all(self, sql, data):
        pass

    def update(self, sql):
        pass

    def delete(self, sql):
        pass

db = Db(
    config.host,
    config.port,
    config.user,
    config.password,
    config.db,
)

print(db.select("SELECT id, name FROM film"))