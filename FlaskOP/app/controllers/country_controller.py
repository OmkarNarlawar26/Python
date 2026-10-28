from flask import jsonify, request
from app.init import app, db
from app.models.country import Country
from app.schemas.country_schema import country_schema, countries_schema


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