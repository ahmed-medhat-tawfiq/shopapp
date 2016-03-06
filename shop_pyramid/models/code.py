from .meta import *
import datetime 
from alembic import op
import sqlalchemy as sa

from sqlalchemy import (
    Column,
    VARCHAR,
    Integer,
    Date,
    Time,
    Boolean,
    Unicode
    )
from sqlalchemy.orm import (
    relation,
    joinedload,
    )
class Code(Base):
    __tablename__ = 'code'
    code_id = Column(Integer, primary_key=True)
    code = Column(VARCHAR(255), nullable=False ,unique=True)
    period = Column(Integer,default=1)
    answer_image=Column(Unicode(100))
    used = Column(Boolean,default=False)
    created_date = Column(Date, default=datetime.datetime.now())
    created_time = Column(Time, default=datetime.datetime.now().time())
    