#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 09:57:31 2017

@author: root
Created on Wed Mar 15 18:53:23 2017
@author: rafik
"""
from __future__ import unicode_literals

import os

import csv, sqlite3

files = """access_log.csv
account_company.csv
account_external.csv
authorization_level.csv
bank_transfer_file.csv
calendar.csv
department.csv
employee.csv
employee_department.csv
invoice_purchase_order.csv
invoice_transactions.csv
public_holidays_zrh.csv
system_users.csv
transactions.csv
user_groups.csv
vendor_address.csv
vendor.csv""".split()



con = sqlite3.connect("db.sqlite")
cur = con.cursor()

for fn in files:
    tablename = fn[:-4]
    fpath = os.path.join("data", fn)
    print "working on", fn, tablename, fpath
    with open(fpath, "r") as f:
        header = f.readlines()[0][3:].strip().split("|")
        print header
    
    headstr = "(%s)" % (", ".join(header))
    qstr = "(%s)" % ", ".join(["?" for _ in header])
    
    try:
        cur.execute("CREATE TABLE %s %s;" % (tablename, headstr)) # use your column names here
    except:
        pass

    with open(fpath,'rb') as fin: # `with` statement available in 2.5+
        # csv.DictReader uses first line in file for column headings by default
#        dr = csv.DictReader(fin) # comma is default delimiter
#        to_db = [(i['col1'], i['col2']) for i in dr]

        lines = fin.readlines()
        to_db = []
        lines.pop(0) # get rid of header
        for line in lines:
            line = line.decode("utf-8").replace(u'\xa6', "'")
            tokens = line.strip().split("|")
            to_db.append(tokens)

        #cur.executemany("INSERT INTO t (col1, col2) VALUES (?, ?);", to_db)
        print 
        cur.executemany("INSERT INTO %s %s VALUES %s;" % (tablename, headstr, qstr), to_db)
con.commit()
con.close()


'''
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


engine = create_engine('sqlite:///db.sqlite3', echo=True)
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

'''