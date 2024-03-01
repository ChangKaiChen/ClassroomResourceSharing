from extensions import db
from sqlalchemy import Column, Integer, String, DateTime, Float, Text, Boolean, Enum, ForeignKey, LargeBinary, Double, \
    SmallInteger, BigInteger
from datetime import time, datetime
from datetime import datetime


# 学生表
class Students(db.Model):
    __tablename__ = 'students'
