#imports
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

#config
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

#views
from app import views, models