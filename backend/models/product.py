from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from backend.database import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(
        Integer,
        primary_key = True,
        index = True
    )

    name = Column (
        String,
        nullable = False
    )

    category = Column(
        String,
        nullable = False
    )

    cost = Column(
        String,
        nullable = False
    )

    time_created = Column (
        String,
        nullable = False
    )
