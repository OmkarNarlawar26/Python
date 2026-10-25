from flask import Flask, jsonify, request
from sqlalchemy import Column, Float, String, Integer
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///country.db'
db = SQLAlchemy(app)

@app.route('/')
def Jay_Ganesh():
    return 'Jay Ganesh...!'

@app.route('/simple')
def simple():
    return 'Simple Jay Ganesh!'

@app.route('/json')
def json():
    return jsonify(text='Simple Jay Ganesh!',
                   message='You have run API successfully!'), 201

@app.route('/not-found')
def not_found():
    return jsonify(error='This is route was not found'), 404

@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age > 18:
        return jsonify(message= f"Welcome {name}!!!")
    else:
        return jsonify(message= f"Sorry {name}, you are not old enough to access this API")

@app.route('/api_variables/<string:name>/<int:age>')
def api_variables(name:str, age:int):
    if age > 21:
        return jsonify(message= f"Welcome {name}!!!")
    else:
        return jsonify(message= f"Sorry {name}, you are not old enough to access this API")

@app.route('/countries', methods=['GET'])
def countries():
    country_list = Country.query.all()
    return jsonify(data=country_list)

# DATABASE
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

class Country(db.Model):
    __tablename__ = 'countries'
    country_id = Column(Integer, primary_key=True)
    country_name = Column(String)
    capital = Column(String)
    area = Column(String)

@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print("Database Dropped!")

@app.cli.command('db_seed')
def db_seed():
    db.create_all()
    usa = Country(country_name='USA',
                  capital='Washington',
                  area='3796742')
    germany = Country(country_name='Germany',
                  capital='Berlin',
                  area='138067')

    db.session.add(usa)
    db.session.add(germany)
    test_user = User(first_name='Omkar',
                     last_name='Narlawar',
                     email='omkar@gmail.com',
                     password='1234')

    db.session.add(test_user)
    db.session.commit()
    print("Database Seeded!")

if __name__ == '__main__':
    app.run()