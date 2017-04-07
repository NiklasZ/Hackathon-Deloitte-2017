#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 11:10:08 2017

@author: root
"""

from sqlalchemy import Column, Integer, UnicodeText, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import collate
from sqlalchemy import desc, asc



engine = create_engine('sqlite:///db.sqlite', echo=True)
Base = declarative_base(bind=engine)


class AccessLog(Base):
    __tablename__ = 'access_log'

    
    date_time    = Column(UnicodeText, primary_key=True)
    user_id      = Column(UnicodeText)
    action       = Column(UnicodeText)
    value        = Column(UnicodeText)

    def __repr__(self):
        return "AccessLog datetime=%s userid=%s, %s, %s'" % (
                self.date_time, self.user_id, self.action, self.value)
        
        


Base.metadata.create_all()

Session = sessionmaker(bind=engine)
sess = Session()
