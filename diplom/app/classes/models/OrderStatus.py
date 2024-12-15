from app.classes.models.Model import Model


class OrderStatus(Model):
    _table = 'order_status'

    def get_data(self) -> dict:
        return {
            'name': self.name if hasattr(self, 'name') else ""
        }