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

# query = session.query(Employees).filter(Employees.id != 3)
# query = session.query(Employees).filter(Employees.name.like('O%'))    # gives name whose first letter starts with O
# query = session.query(Employees).filter(Employees.name.like('%r%'))   # gives name in which r is present in between or last or first

# query = session.query(Employees).filter(Employees.id.in_([1,3]))      # gives details of id 1 and 3

query = session.query(Employees).filter(and_(Employees.id > 1, Employees.name.like('T%')) )     # gives details of id 1 and 3


for employee in query:
    print('Name: ', employee.name, 'Position: ', employee.position)

session.commit()