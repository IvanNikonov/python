from app.classes.models.Model import Model
from app.classes.models.OrderElement import OrderElement
from app.classes.models.OrderStatus import OrderStatus
from app.classes.api.Telegram import Telegram
from datetime import datetime
from app.classes.Cart import Cart


class Order(Model):
    _table = 'order'

    def __init__(self, fields=None):
        super().__init__(fields)
        self.status = OrderStatus.get_by_key('id', self.id_status) if hasattr(self, 'id_status') else None
        self.elements = OrderElement.get_list([f"id_order = {self.id}"], ["id ASC"], 100) if hasattr(self, 'id') else None
        self.dt_create_formated =  self.dt_create.strftime('%d.%m.%Y %H:%M:%S') if hasattr(self, 'dt_create') else None

    def get_data(self) -> dict:
        return {
            'dt_create': self.dt_create if hasattr(self, 'dt_create') else datetime.now(),
            'sum': self.sum if hasattr(self, 'sum') else "0",
            'name': self.name if hasattr(self, 'name') else "",
            'phone': self.phone if hasattr(self, 'phone') else "",
            'email': self.email if hasattr(self, 'email') else "",
            'comment': self.comment if hasattr(self, 'comment') else "",
            'id_status': self.id_status if hasattr(self, 'id_status') else "0",
        }

    def validate(self):

        if self.name == "":
            self.errors.append('Поле ФИО обязательно для заполнения')

        if self.phone == "":
            self.errors.append('Поле Телефон обязательно для заполнения')

        if self.email == "":
            self.errors.append('Поле E-mail обязательно для заполнения')

        return len(self.errors) == 0

    def action_before_insert(self):
        cart = Cart.get_instance().get_cart_info()
        self.id_status = 1
        self.sum = cart['total_summ']

    def action_after_insert(self):
        cart = Cart.get_instance().get_cart_info()

        for row in cart['list']:
            element = OrderElement({
                "count": row['count'],
                "price": row['product'].price,
                "id_order": self.id,
                "id_product": row['product'].id
            })

            if element.validate():
                element.save_to_db()

        Cart.get_instance().clear()

        self.notify_by_telegram()

    def notify_by_telegram(self):
        order = Order.get_by_key('id', self.id)
        message = ''
        message += f'Новый заказ №{order.id} на сайте\n'
        message += f'<b>Время заказа:</b> {order.dt_create_formated}\n'
        message += f'<b>ФИО:</b> {order.name}\n'
        message += f'<b>Телефон:</b> {order.phone}\n'
        message += f'<b>E-mail:</b> {order.email}\n'
        message += f'<b>Сумма заказа:</b> {order.sum} руб.\n'
        message += f'<b>Состав заказа</b>\n'

        for element in order.elements:
            message += f'{element.product.name} - {element.count} шт.\n'

        Telegram.get_instance().sendMessage(message)
