from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker, Session

UniverBase =declarative_base()

class Faculty(UniverBase):
    __tablename__ = "faculty"
    id = Column(Integer,primary_key=True)
    name = Column(String, nullable = False)
    students = relationship('Students', back_populates = 'faculty')

class Students(UniverBase):
    __tablename__ = "student"
    id = Column(Integer,primary_key=True)
    name = Column(String, nullable=False)
    faculty_id = Column(Integer, ForeignKey('faculty.id'))
    faculty = relationship('Faculty', back_populates='students')

    #работа с базой
engine = create_engine('sqlite:///Vsu.db', echo=False)
UniverBase.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

faculty1 = Faculty(name="ФКН")
faculty2 = Faculty(name="ПММ")

student1 = Students(name="Антон", faculty=faculty1)
student2 = Students(name="Жора", faculty=faculty1)
student3 = Students(name="Мотя", faculty=faculty2)

session.add(faculty1)
session.add(faculty2)
session.commit()

faculties = session.query(Faculty).all()

#вывод данных
for faculty in faculties:
    print(f"Факультет:{faculty.name}")
    for student in faculty.students:
        print(f"Студент:{student.name}")

