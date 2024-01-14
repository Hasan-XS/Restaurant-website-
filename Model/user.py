from sqlalchemy import *
from extention import db

class User(db.Model):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False, index=True)
    address = Column(String, nullable=False, index=True)