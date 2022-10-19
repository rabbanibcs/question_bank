
from enum import unique
from unicodedata import name
from sqlalchemy import Column, Boolean,  ForeignKey, Integer, PrimaryKeyConstraint, String
from .database import Base
from sqlalchemy.sql.sqltypes import Date
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from datetime import date


class Topic(Base):
    __tablename__='topics'

    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False,unique=True)
    questions=relationship("BcsQuestion",back_populates = "topic")


class Bcs(Base):
    __tablename__='bcs'

    id=Column(Integer,primary_key=True,nullable=False)
    ordinal=Column(Integer,nullable=False,unique=True)
    total_marks=Column(Integer,nullable=False)
    duration=Column(Integer,nullable=False)
    special=Column(String)
    exam_year=Column(String(4),nullable=False)

    questions=relationship("BcsQuestion")


class Directoriate(Base):
    __tablename__='derectoriates'

    id=Column(Integer,primary_key=True,nullable=False)
    derectoriate_name=Column(String,nullable=False)
    post_name=Column(String,nullable=False)
    duration=Column(Integer,nullable=False)
    total_marks=Column(Integer,nullable=False)



class Question(Base):
    __abstract__ = True

    id=Column(Integer,primary_key=True,nullable=False)

    question=Column(String,nullable=False)
    option_a=Column(String,nullable=False)
    option_b=Column(String,nullable=False)
    option_c=Column(String,nullable=False)
    option_d=Column(String,nullable=False)
    answer=Column(String(1),nullable=False)

    note=Column(String,nullable=True)
    explanation=Column(String,nullable=True)
    created_at=Column(Date,default=date.today)

class BcsQuestion(Question):
    
    __tablename__='bcs_questions'

    topic_id=Column(Integer, ForeignKey("topics.id"),nullable=True)
    bcs=Column(Integer, ForeignKey("bcs.ordinal"),nullable=False)
    topic=relationship("Topic", back_populates = "questions")


class DirectoriateQustion(Question):

    __tablename__='directorate_questions'

    topic=Column(Integer, ForeignKey("topics.id"),nullable=True)
    directorate=Column(Integer, ForeignKey("derectoriates.id"),nullable=False)
    exam_year=Column(String(4),nullable=False)
    exam_step=Column(Integer)
    # related_topic=relationship("Topic")
    

class User(Base): 

    __tablename__='users'

    id=Column(Integer,primary_key=True,nullable=False)
    name=Column(String,nullable=True)
    email=Column(String,nullable=False,unique=True)
    phone=Column(String(11),nullable=False,unique=True)
    password=Column(String,nullable=False)
    created_at=Column(Date,default=date.today)

   
















