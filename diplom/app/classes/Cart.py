from flask import session
from app.classes.models.Product import Product


class Cart:
    KEY_NAME = 'cart'

    _instance = None
    _connection = None

    @classmethod
    def get_instance(cls):
        return cls()

    def get_cart_info(self):
        data = {
            'total_count': 0,
            'total_summ': 0,
            'list': []
        }

        for row_dict in self._data:
            product = Product.get_by_key('id', row_dict['product_id'])
            summ = product.price * row_dict['count']

            data['total_count'] = data['total_count'] + row_dict['count']
            data['total_summ'] = data['total_summ'] + summ
            data['list'].append(
                {
                    'summ': summ,
                    'count': row_dict['count'],
                    'product': product
                }
            )

        return data

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._data = session[self.KEY_NAME] if self.KEY_NAME in session else []

    def add(self, id):
        is_new = True
        new_data = []

        for cart_dict in self._data:
            if cart_dict['product_id'] == id:
                is_new = False
                new_data.append({
                    "product_id": id,
                    "count": cart_dict['count'] + 1
                })
                continue
            new_data.append(cart_dict)

        if is_new:
            new_data.append({
                "product_id": id,
                "count": 1
            })

        self._data = new_data
        self.save_to_session()
        return self._data

    def delete(self, id):
        new_data = []

        for cart_dict in self._data:
            if cart_dict['product_id'] == id:
                continue
            new_data.append(cart_dict)

        self._data = new_data
        self.save_to_session()
        return self._data

    def clear(self):
        session.pop(self.KEY_NAME)
        self._data = []
        session.modified = True

    def save_to_session(self):
        session[self.KEY_NAME] = self._data
        session.modified = True
