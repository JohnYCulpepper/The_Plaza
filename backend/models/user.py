from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from backend.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(                # creates a unique user id created
        Integer,
        primary_key = True,
        index = True
    )

    role = Column (             # buyer, seller, or admin; everyone's assigned a buyer
        String,
        nullable = False 
    )

    email = Column(
        String,
        unique = True,
        nullable = False
    )

    password = Column(
        String, 
        nullable = False 
    )

    name = Column(
        String,
        nullable = False
    )

    phone = Column(String)

    time_created = Column (
        String,
        nullable = False
    )

