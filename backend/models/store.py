from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from backend.database import Base

class Store(Base):
    __tablename__ = 'stores'

    id = Column(
        Integer,
        primary_key = True,
        index = True
    )

    store_name = Column (
        String,
        nullable = False
    )


    email = Column (
        String,
        nullable = False
    )

    is_approved = Column (
        bool,
        nullable = False
    )
    
    time_created = Column (
        String, 
        nullable = False
    )

    

