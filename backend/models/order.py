from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from backend.database import Base

class Order(Base):
    __tablename__ = 'orders'

    id = Column(          # links to users table
        Integer,
        primary_key = True,
        index = True
    )

    total_amount = Column (
        String,
        nullable = False
    )

    store_id = Column(
        String,
        nullable = False
    )

    status = Column(        # pending or done
        String,
        nullable = False
    )

    time_created = Column(
        String,
        nullable = False
    )


