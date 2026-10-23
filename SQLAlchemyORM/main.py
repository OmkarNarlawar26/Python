from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, session
from sqlalchemy import Column, Integer, String

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

# row1 = Employees(name='Omkar', position='Software Engineer')
# session.add(row1)
#
# session.add_all([Employees(name='Omki', position='Software Engineering'),
#                  Employees(name='Om', position='Software Developer'),
#                  Employees(name='Trupti', position='Software Analyst'),])

query = session.query(Employees).all()
# # print(query)
#
# for employee in query:
#     print('Name: ', employee.name, 'Position: ', employee.position)

query = session.query(Employees).get(3)
print('Name: ', query.name, 'Position: ', query.position)


session.commit()