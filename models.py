from extensions import Base
from sqlalchemy import Column, Integer, String, DateTime, Float, Text, Boolean, Enum, ForeignKey, LargeBinary, Double, \
    SmallInteger, BigInteger
from datetime import time, datetime
from datetime import datetime


# 学生表
class Users(Base):
    __tablename__ = 'users'
    username = Column('username', String, nullable=False, primary_key=True)
    password = Column('password', String, nullable=False)
    email = Column('email', String, nullable=False)


class PublishedArticles(Base):
    __tablename__ = 'published_articles'
    id = Column('id', Integer, nullable=False, primary_key=True, autoincrement=True)
    title = Column('title', String, nullable=False)
    content = Column('content', String, nullable=False)
    category = Column('category', String, nullable=False)
    author = Column('author', String, nullable=False)
    date = Column('date', DateTime, nullable=False, default=datetime.now())


class DeletedArticles(Base):
    __tablename__ = 'deleted_articles'
    id = Column('id', Integer, nullable=False, primary_key=True)
    title = Column('title', String, nullable=False)
    content = Column('content', String, nullable=False)
    category = Column('category', String, nullable=False)
    author = Column('author', String, nullable=False)
    published_date = Column('published_date', DateTime, nullable=False)
    deleted_date = Column('deleted_date', DateTime, nullable=False, default=datetime.now())
