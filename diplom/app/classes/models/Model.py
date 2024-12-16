from abc import ABC, abstractmethod
from app.classes.DB import DB


class Model(ABC):
    _table = None

    def __init__(self, fields=None):

        if isinstance(fields, dict):
            self.set_attributes(fields)

        self.errors = []

    @abstractmethod
    def get_data(self) -> dict:
        pass

    @classmethod
    def get_list(cls, filters=[], sorters=[], limit=20):
        where = ''
        order_by = 'ORDER BY id ASC'

        if isinstance(filters, list) and len(filters) > 0:
            where = f"WHERE {" AND ".join(filters)}"

        if isinstance(sorters, list) and len(sorters) > 0:
            order_by = f"ORDER BY {", ".join(sorters)}"

        sql = f'SELECT * FROM "{cls._table}" {where} {order_by} LIMIT {limit}'

        print(sql)
        result = DB.get_instance().select_all(sql)

        if result is None:
            return None

        list_object = []

        for row in result:
            list_object.append(cls(row))

        return list_object

    @classmethod
    def get_by_key(cls, key, value):
        return cls.get_by_keys({key: value})

    @classmethod
    def get_by_keys(cls, data):

        if not data or not isinstance(data, dict):
            return None

        where = []

        for key, value in data.items():
            where.append(f"{key} = '{value}'")

        sql = f'SELECT * FROM "{cls._table}" WHERE {' AND '.join(where)} LIMIT 1'
        result = DB.get_instance().select_one(sql)

        if result is None:
            return None

        return cls(result)

    def validate(self) -> bool:
        return True

    def save_to_db(self):
        is_old = hasattr(self, 'id')

        if is_old:
            self.action_before_update()
            data = self.get_data()
            data = ', '.join([f"{key} = '{value}'" for key, value in data.items()])
            sql = f'UPDATE "{self._table}" SET {data} WHERE "id" = {self.id}'
        else:
            self.action_before_insert()
            data = self.get_data()
            columns = ', '.join((list(data.keys())))
            values = ', '.join(map(lambda element: f"'{element}'", list(data.values())))
            sql = f'INSERT INTO "{self._table}" ({columns}) VALUES ({values}) RETURNING id'

        result = DB.get_instance().execute(sql, not is_old)

        if is_old:
            self.action_after_update()
        else:
            self.id = result
            self.action_after_insert()

        return result

    def delete(self):
        pass

    def set_attributes(self, fields):
        for key, value in fields.items():
            self.__setattr__(key, value)

    def is_field_unique(self, field_name):
        where_id = f" AND id <> {self.id}" if hasattr(self, 'id') else ""
        result = DB.get_instance().select_one(
            f"SELECT id FROM {self._table} WHERE {field_name} LIKE '{self.__getattribute__(field_name)}' {where_id}"
        )

        return result is None

    def action_before_insert(self):
        pass

    def action_after_insert(self):
        pass

    def action_before_update(self):
        pass

    def action_after_update(self):
        pass
