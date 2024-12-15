from app.classes.models.Model import Model
from app.classes.models.Product import Product


class OrderElement(Model):
    _table = 'order_element'

    def __init__(self, fields=None):
        super().__init__(fields)
        self.sum = self.price + self.count if hasattr(self, 'price') and hasattr(self, 'count') else None
        self.product = Product.get_by_key('id', self.id_product) if hasattr(self, 'id_product') else None

    def get_data(self) -> dict:
        return {
            'count': self.count if hasattr(self, 'count') else "0",
            'price': self.price if hasattr(self, 'price') else "0",
            'id_order': self.id_order if hasattr(self, 'id_order') else "0",
            'id_product': self.id_product if hasattr(self, 'id_product') else "0",
        }