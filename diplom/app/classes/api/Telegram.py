from requests import get
from os import getenv

class Telegram:
    _instance = None
    _connection = None

    @classmethod
    def get_instance(cls):
        return cls()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._api_key = getenv("TELEGRAM_API_KEY")
        self._chat_id = getenv("TELEGRAM_CHAT_ID")

    def sendMessage(self, message):
        response = get(f"https://api.telegram.org/bot{self._api_key}/sendMessage?chat_id={self._chat_id}&text={message}&parse_mode=html")
        return response.status_code == 200