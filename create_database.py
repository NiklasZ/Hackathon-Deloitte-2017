#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 09:57:31 2017

@author: root
Created on Wed Mar 15 18:53:23 2017
@author: rafik
"""

import pickle

from sqlalchemy import Column, Integer, UnicodeText, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import collate
from sqlalchemy import desc, asc


def save_obj(obj, name):
    with open(name, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open(name, 'rb') as f:
        return pickle.load(f)


engine = create_engine('sqlite:///registration.sqlite3', echo=True)
Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = 'registrationTable'

    id           = Column(Integer, primary_key=True)
    title        = Column(UnicodeText, nullable=True)
    firstname    = Column(UnicodeText)
    lastname     = Column(UnicodeText)
    email        = Column(UnicodeText)
    affiliation  = Column(UnicodeText)
    address      = Column(UnicodeText)
    hasPayed     = Column(Boolean)
    isPassive    = Column(Boolean)

    def __repr__(self):
        return "<User(id=%i lastname='%s', firstname='%s')>" % (
                self.id, self.lastname, self.firstname)

Base.metadata.create_all()

Session = sessionmaker(bind=engine)
sess = Session()

# u = s.query(User).filter_by(firstname='Rafael').first()
# q = sess.query(User).order_by(User.id)
# sess.dirty
# sess.new
# sess.commit()