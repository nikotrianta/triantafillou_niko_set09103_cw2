import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'