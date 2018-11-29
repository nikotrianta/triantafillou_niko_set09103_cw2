import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('/static/var/sqlite3.db') or \
        'sqlite:///' + os.path.join(basedir, 'static/var/sqlite3.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False