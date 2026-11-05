from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///country.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
auth = HTTPBasicAuth()

from app.controllers import country_controller
from app.controllers import user_controller
from app import commands
