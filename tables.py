from sqlalchemy import Table, MetaData, Column, String, Integer, Boolean, ForeignKey, Date
from sqlalchemy import Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
