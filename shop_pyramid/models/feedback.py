from .meta import *
import datetime 
from sqlalchemy import (
    Column,
    VARCHAR,
    Integer,
    Date,
    Time,
    Boolean
    )
from sqlalchemy.orm import (
    relation,
    joinedload,
    )

class feedback(Base):
    __tablename__ = 'feedback'
    feedback_id = Column(Integer, primary_key=True)
    description = Column(VARCHAR(255))
    star = Column(Integer , nullable=False)
    period = Column(Integer,default=1)
    used = Column(Boolean,default=False)
    created_date = Column(Date, default=datetime.datetime.now())
    created_time = Column(Time, default=datetime.datetime.now().time())