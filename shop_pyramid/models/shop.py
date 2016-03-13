from .meta import * 
from datetime import datetime,timedelta
import datetime
from sqlalchemy import (
    Column,
    VARCHAR,
    Integer,
    Numeric,
    TEXT,
    ForeignKey,
    Date,
    Time
    )

class Shop(Base):
    __tablename__ = 'shops'
    shop_id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255), nullable=False)
    category = Column(VARCHAR(255), nullable=False)
    description = Column(VARCHAR(255))
    ads = Column(TEXT)
    rank = Column(Integer)
    latitude = Column(Numeric, nullable=False)
    longitude = Column(Numeric, nullable=False)
    types=Column(VARCHAR(255))
    start_date = Column(Date)
    end_date = Column(Date)
    created_date = Column(Date, default=datetime.datetime.now())
    created_time = Column(Time, default=datetime.datetime.now().time())
    user = Column(Integer,ForeignKey('user.user_id',ondelete='Cascade'), nullable=False)

   
    #feedback 4atayem , phone table