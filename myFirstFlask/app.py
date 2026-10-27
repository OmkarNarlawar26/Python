from flask import Flask, jsonify, request
from sqlalchemy import Column, Float, String, Integer
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///country.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

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




# @app.route('/countries', methods=['GET'])         # Method 1
@app.get('/countries')                              # Traditional method
def countries():
    country_list = Country.query.all()
    result = countries_schema.dump(country_list)
    return jsonify(result)


@app.route('/country_details/<int:country_id>', methods=['GET'])
def country_details(country_id:int):
    country = Country.query.filter_by(country_id=country_id).first()
    if country:
        result = country_schema.dump(country)
        return jsonify(result)
    return jsonify("That country dose not exist!"), 404



# This is done by using (form)
# @app.route('/add_country', methods=['POST'])
@app.post('/add_country')
def add_country():
    country_name = request.form['country_name']
    check_country = Country.query.filter_by(country_name=country_name).first()
    if check_country:
        return jsonify("The country by that name exists in DB"), 409  # 409 tell us that there is conflict
    capital = request.form['capital']
    area = request.form['area']
    new_country = Country(country_name=country_name, capital=capital, area=area)
    db.session.add(new_country)
    db.session.commit()
    return jsonify("New country added!"), 201



# This is done by using (get)
@app.route('/add_country1', methods=['POST'])
def add_country1():
    data = request.get_json()
    if not data:
        return jsonify("Invalid or missing JSON data"), 400
    country_name = data.get('country_name')
    check_country = Country.query.filter_by(country_name=country_name).first()
    if check_country:
        return jsonify("The country by that name exists in DB"), 409  # 409 tell us that there is conflict
    capital = data.get('capital')
    area = data.get('area')
    new_country = Country(country_name=country_name, capital=capital, area=area)
    db.session.add(new_country)
    db.session.commit()
    return jsonify(message="you added a new country"), 201



@app.route('/countries/<int:country_id>', methods=['PATCH'])
def update_country(country_id):
    data = request.get_json()
    country = Country.query.filter_by(country_id=country_id).first()
    if not country:
        return jsonify(message = "Country not found"), 404
    if 'country_name' in data:
        country.country_name = data['country_name']
    if 'capital' in data:
        country.captial = data['capital']
    if 'area' in data:
        country.area = data['area']
    db.session.commit()
    return jsonify({"message": "Country updates successfully", "country_id":country_id}), 200



@app.route('/countries/<int:country_id>', methods=['DELETE'])
def remove_country(country_id):
    country = Country.query.filter_by(country_id=country_id).first()
    if not country:
        # return jsonify(message="Country not found"), 404                  # Option 1
        return {"message": "Country not found"}                             # Option 2
    db.session.delete(country)
    db.session.commit()
    return jsonify(message = f"You deleted a country with id of {country_id}"), 202


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
    area = Column(Float)


class UserSchema(ma.Schema):
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    email = fields.Email()
    password = fields.String()


class CountrySchema(ma.Schema):
    country_id = fields.Integer()
    country_name = fields.String()
    capital = fields.String()
    area = fields.Float()

# objects
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# objects
country_schema = CountrySchema()
countries_schema = CountrySchema(many=True)

@app.cli.command('db_create')
def db_create():
    db.create_all()
    print("Database Created!")

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