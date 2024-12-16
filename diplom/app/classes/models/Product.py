from app.classes.models.Model import Model


class Product(Model):
    _table = 'product'

    def get_data(self) -> dict:
        return {
            'name': self.name if hasattr(self, 'name') else '',
            'alias': self.alias if hasattr(self, 'alias') else '',
            'price': str(self.price) if hasattr(self, 'price') else '0',
            'is_active': "1" if hasattr(self, 'is_active') and self.is_active is not "0" else "0"
        }

    def validate(self):

        if self.price == "":
            self.errors.append('Поле цена обязательно для заполнения')


        if self.name == "":
            self.errors.append('Поле наименование обязательно для заполнения')
        elif not self.is_field_unique("name"):
            self.errors.append('Поле наименование должно быть уникальным')

        if self.alias == "":
            self.errors.append('Поле псевдоним обязательно для заполнения')
        elif not self.is_field_unique("alias"):
            self.errors.append('Поле псевдоним должно быть уникальным')

        return len(self.errors) == 0

    def get_url(self):
        return f"/product/{self.alias}/"

