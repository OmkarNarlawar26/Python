from app.init import app, db
from app.models.country import Country
from app.models.user import User

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