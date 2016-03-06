from .meta import *
import datetime
from sqlalchemy import (
    Column,
    VARCHAR,
    Integer,
    Date,
    Time,
    ForeignKey,
    Boolean
    )

class Phone(Base):
    __tablename__ = 'phone'
    phone_id = Column(Integer, primary_key=True)
    number = Column(VARCHAR(255), nullable=False ,unique=True)
    Primary = Column(Boolean,default=False)
    created_date = Column(Date, default=datetime.datetime.now())
    created_time = Column(Time, default=datetime.datetime.now().time())
    shop = Column(Integer,ForeignKey('shops.shop_id',ondelete='Cascade'), nullable=False)