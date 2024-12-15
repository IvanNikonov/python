from app.classes.models.Model import Model
from os import getenv
from hashlib import md5
from flask import session


class Admin(Model):
    AUTH_KEY = 'admin'
    _table = 'admin'

    def get_data(self) -> dict:
        return {}

    @classmethod
    def get_hash_by_password(cls, password):
        if not isinstance(password, str):
            return ''

        password_salted = password + getenv("HASH_SALT")
        hash_password = md5(password_salted.encode())
        return hash_password.hexdigest()

    @classmethod
    def get_admin_by_credentials(cls, login, password):
        return Admin.get_by_keys(
            {
                "login": login,
                "hash_password": cls.get_hash_by_password(password)
            }
        )

    @classmethod
    def is_authorized(cls):
        return cls.get_authorized() is not None

    @classmethod
    def get_authorized(cls):
        if cls.AUTH_KEY not in session:
            return None

        return cls.get_by_key('id', session[cls.AUTH_KEY])

    def authorize(self):
        if hasattr(self, 'id'):
            session[self.AUTH_KEY] = self.id
            return True
        return False

    @classmethod
    def logout(cls):
        session.pop(cls.AUTH_KEY)
