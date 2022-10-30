from sqlalchemy import  Column, Integer, String 
from database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(40),  index=True)
    password = Column(String(200))
    name = Column(String(40))
