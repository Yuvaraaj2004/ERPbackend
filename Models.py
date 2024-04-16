from fastapi import Depends
from sqlalchemy import Column, Date, Integer, String, ForeignKey, Sequence, Enum
from sqlalchemy.orm import relationship, backref
from DataBase import Base, get_db


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq', start=1), primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    dob = Column(String(100), nullable=False)
    contact_number = Column(String(13), nullable=False)
    user_type = Column(Integer, nullable=False)
    students = relationship("Student", back_populates="user")
    faculties = relationship("Faculty", back_populates="user")
    marks = relationship("Mark", back_populates="user")  # Added relationship

    def __init__(self, name, email, dob, contact_number, user_type, **d):
        self.name = name
        self.email = email
        self.dob = dob
        self.contact_number = contact_number
        self.user_type = user_type


class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, Sequence(
        'student_id_seq', start=1), primary_key=True)
    register_number = Column(String, nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    user = relationship("User", back_populates="students")


class Faculty(Base):
    __tablename__ = 'faculty'

    faculty_id = Column(Integer, Sequence(
        'faculty_id_seq', start=1), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    user = relationship("User", back_populates="faculties")


class Subjects(Base):
    __tablename__ = 'subjects'

    subject_id = Column(Integer, Sequence(
        'subject_id_seq', start=1), primary_key=True)
    subject_name = Column(String, nullable=False, unique=True)
    # Added relationship
    marks = relationship("Mark", back_populates="subject")


class Mark(Base):
    __tablename__ = 'Marks'
    user_id = Column(Integer, ForeignKey(
        'users.id', ondelete='CASCADE'), primary_key=True)
    semester = Column(Integer, nullable=False, primary_key=True)
    subject_id = Column(Integer, ForeignKey(
        'subjects.subject_id'), primary_key=True)
    grade = Column(String, nullable=True)

    # Define the 'user' relationship
    user = relationship("User", back_populates="marks")

    subject = relationship("Subjects", back_populates="marks")
