from app.init import ma
from marshmallow import fields


class UserSchema(ma.Schema):
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    email = fields.Email()
    password = fields.String()

# Object
user_schema = UserSchema()
users_schema = UserSchema(many=True)