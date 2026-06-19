from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from backend.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(
        Integer,
        primary_key = True,
        index = True
    )

    email = Column(
        String,
        unique = True,
        nullable = False
    )

    passoword = Column(
        String, 
        nullable = False 
    )

    name = Column(
        String,
        nullable = False
    )

    phone = Column(String)