from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title= Column(String)
    year= Column(String)
    rating= Column(Float)
    category= Column(String)

class Users(Base):
    __tablename__ = "users"
    id= Column(Integer, primary_key=True)
    name= Column(String)
    email=Column(String)
    user_name=Column(String)
    password=Column(String)    