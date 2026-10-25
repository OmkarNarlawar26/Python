from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, session, relationships, relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy import and_

engine = create_engine('sqlite:///hr.db')
Base = declarative_base()

class Employees(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    position = Column(String)

class Projects(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    emp_id = Column(Integer, ForeignKey('employees.id'))
    name = Column(String)
    employees = relationship('Employees', back_populates='projects')
    
Employees.projects = relationship('Projects', back_populates='employees')

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# emp1 = Employees(name='Omkar', position='Student')
# emp1.projects = [Projects(name='Python for Everyone'), Projects(name='Python DSA')]
# session.add(emp1)

rows = [
    Employees(
        name = 'Om',
        position = 'Intern',
        projects = [Projects(name='Python Django'), Projects(name='Python Flask')]
    ),
    Employees(
        name = 'Jay',
        position = 'Developer',
        projects = [Projects(name='SQLite Project'), Projects(name='SQLAlchemy Project')]
    )
]

session.add_all(rows)
session.commit()



