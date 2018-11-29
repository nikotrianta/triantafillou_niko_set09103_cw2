from flask import Flask, g
from . import db
import sqlite3

app = Flask(__name__)
db_location = 'sqlite3.db'


def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = sqlite3.connect(db_location) 
        g.db = db
    return db

@app.teardown_appcontext
def close_db_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(64), index=True, unique=True)
    message = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)