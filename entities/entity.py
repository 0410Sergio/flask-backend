# coding=utf-8

from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = 'db-stock-data.c0iscncut9ja.us-east-1.rds.amazonaws.com'
db_name = 'mydb'
db_user = 'sergiocxz'
db_password = '******'
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Entity():
    date = Column(Date, primary_key=True)
    #changePercent = Column(String)
    '''created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)'''

    def __init__(self, created_by):
        '''self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by'''

class EntityNews():
    title = Column(String, primary_key=True)
    #changePercent = Column(String)
    '''created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)'''

    def __init__(self, created_by):
        '''self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by'''
