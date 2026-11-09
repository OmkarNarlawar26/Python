from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)


@app.cli.command('db_create')
def db_create():
    db.create_all()
    print("Database created!")


import routes