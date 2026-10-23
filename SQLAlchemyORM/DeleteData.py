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

query = session.query(Employees).get(2)
session.delete(query)

session.commit()

