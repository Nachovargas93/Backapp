from sqlalchemy import Column, Integer, String 

from app import db


class Todo(db.Model):

    id = Column(Integer, primary_key=True)
    content = Column(String(20))