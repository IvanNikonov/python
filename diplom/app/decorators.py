from flask import render_template
from functools import wraps
from app.classes.models.Admin import Admin

def decorator_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if Admin.is_authorized():
            return func(*args, **kwargs)

        return render_template('admin/login.html')
    return wrapper