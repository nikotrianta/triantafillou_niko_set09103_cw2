#imports
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

#config
app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'any secret string'
db = SQLAlchemy(app)

#views
from . import views, models