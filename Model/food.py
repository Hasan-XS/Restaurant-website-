from sqlalchemy import *
from extention import db

class Food(db.Model):
    __tablename__ = "Foods"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False, index=True)
    description = Column(String, nullable=False, index=True)
    price = Column(Integer, nullable=False, index=True)
    active = Column(Integer, nullable=False, index=True)