from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Date, Time

import settings

DeclarativeBase = declarative_base()

def db_connect():
    return create_engine(URL(**settings.DATABASE))
	
def create_fares_table(engine):
    DeclarativeBase.metadata.create_all(engine)
	
class Fares(DeclarativeBase):
	__tablename__ = "fares"
	id = Column(Integer, primary_key=True)
	fare = Column('fare', String)
	origtime = Column('origtime', Time, nullable=True)
	desttime = Column('desttime', Time, nullable=True)
	origcity = Column('orig', String, nullable=True)
	origlocation = Column('origlocation', String, nullable=True)
	destcity = Column('dest', String, nullable=True)
	destlocation = Column('destlocation', String, nullable=True)
	duration = Column('duration', String, nullable=True)
	timescraped = Column('timescraped', Time, nullable=True)
	datescraped = Column('datescraped', Date, nullable=True)
	departuredate = Column('departuredate', Date, nullable=True)