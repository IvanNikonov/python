# from os import getenv
#
# from flask.cli import load_dotenv
# from sqlalchemy.util import md5_hex
# from app.models import Admin
# from app import db
# from app import app
#
# load_dotenv()
#
# admin = Admin(
#     login = 'admin',
#     hash_password = md5_hex('admin' + getenv('HASH_SOLE'))
# )
#
# with app.app_context():
#     db.session.add(admin)
#     db.session.commit()
