from app.init import ma
from marshmallow import fields


class CountrySchema(ma.Schema):
    country_id = fields.Integer()
    country_name = fields.String()
    capital = fields.String()
    area = fields.Float()

# Object
country_schema = CountrySchema()
countries_schema = CountrySchema(many=True)