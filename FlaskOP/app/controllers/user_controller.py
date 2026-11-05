from flask import request, jsonify
from werkzeug.security import generate_password_hash

from app.init import app, db
from app.models.user import User


@app.post('/register')
def register():
    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    new_user = User(first_name = data['first_name'],
                    last_name = data['last_name'],
                    email = data['email'],
                    password = hashed_password)

    db.session.add(new_user)
    db.session.commit()
    return jsonify(message = "Registered Successfully"), 201