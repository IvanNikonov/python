from flask import render_template
from app import app, db
from app.models import Resume


@app.route('/')
@app.route('/index')
def index():
    resume = db.session.query(Resume).get(1)
    return render_template("page.html", resume=resume)