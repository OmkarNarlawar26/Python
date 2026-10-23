from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, session
from sqlalchemy import Column, Integer, String
from sqlalchemy import and_

engine = create_engine('sqlite:///hr.db')
Base = declarative_base()

class Employees(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    position = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

query = session.query(Employees).filter(Employees.id == 1)
query.update({Employees.name: 'Mr. Omkar Narlawar'})
session.commit()

# query = session.query(Employees).get(1)
# Another method to update
# print(query.name, query.position)
# query.name = 'Omkar Narlawar'
# session.commit()
# print(query.name, query.position)

