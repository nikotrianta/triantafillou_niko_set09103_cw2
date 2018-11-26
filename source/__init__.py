#imports
from flask import Flask
from config import Config

#config
app = Flask(__name__)
app.config.from_object(Config)

#views
from . import views