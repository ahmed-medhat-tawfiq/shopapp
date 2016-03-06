from .meta import *
from datetime import datetime,timedelta
import datetime
from sqlalchemy import (
    Column,
    VARCHAR,
    Integer,
    Float,
    ForeignKey,
    DateTime,
    Date,
    Boolean,
    Time
    )

class Month(Base):
    __tablename__ = 'month'
    month_id = Column(Integer, primary_key=True)
    # start_day = Column(VARCHAR(255), default=datetime.datetime.now().strftime("%a"))
    # start_month = Column(VARCHAR(255), default=datetime.datetime.now().strftime("%B"))
    # start_year = Column(VARCHAR(255), default=datetime.datetime.now().strftime("%Y"))
    # end_day = Column(VARCHAR(255))
    # end_month = Column(VARCHAR(255))
    # end_year = Column(VARCHAR(255))

    t_purse=Column(Float, default=0)
    t_customer=Column(Integer , default=0)
    t_pcustomer=Column(Integer, default=0)
    t_vcustomer=Column(Integer, default=0)
    t_time=Column(Integer, default=0)
    # t_persuasion=Column(Float, default=0)
    # t_againts=Column(Float, default=0)
    t_sdate = Column(DateTime, default=datetime.datetime.now())
    t_edate = Column(DateTime, default=datetime.datetime.now()+datetime.timedelta(hours=12))
    
    # y_purse=Column(Float, default=0)
    # y_customer=Column(Float, default=0)
    # y_pcustomer=Column(Float, default=0)
    # y_vcustomer=Column(Float, default=0)
    # y_time=Column(Float, default=0)
    # y_persuasion=Column(Float, default=0)
    # y_againts=Column(Float, default=0)
    
    m_purse=Column(Float, default=0)
    m_customer=Column(Integer, default=0)
    m_pcustomer=Column(Integer, default=0)
    m_vcustomer=Column(Integer, default=0)
    m_time=Column(Integer, default=0)
    # m_persuasion=Column(Float, default=0)
    # m_againts=Column(Float, default=0)
    start_date = Column(Date, default=datetime.datetime.now())
    end_date = Column(Date, default=datetime.datetime.now()+datetime.timedelta(days=30))
    old = Column(Boolean, default=False)
    user = Column(Integer,ForeignKey('user.user_id',ondelete='Cascade'), nullable=False)

   