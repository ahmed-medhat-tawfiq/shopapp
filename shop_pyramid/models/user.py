from .meta import *
import datetime 
from sqlalchemy import (
    Column,
    VARCHAR,
    Integer,
    Table,
    Date,
    Numeric,
    Boolean,
    TEXT,
    Time
    )

from sqlalchemy.orm import (
    relation,
    joinedload,
    )




class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    first_name = Column(VARCHAR(255), nullable=False)
    last_name= Column(VARCHAR(255), nullable=False)
    username = Column(VARCHAR(255), unique=True)
    password = Column(VARCHAR(255))
    email= Column(VARCHAR(255), unique=True, default='not exist')
    location=Column(VARCHAR(255))
    country=Column(VARCHAR(255))
    phone1 =Column(VARCHAR(255), unique=True)
    phone2 = Column(VARCHAR(255), unique=True)
    shop_no=Column(Integer,default=0)
    avatar = Column(TEXT , default='none')
    groups = Column(VARCHAR(255), default='n')
    sales_id = Column(Integer, default=0)
    admin_id = Column(Integer, default=0)
    block=Column(Boolean, default=False)
    created_date = Column(Date, default=datetime.datetime.now())
    created_time = Column(Time, default=datetime.datetime.now().time())
    

