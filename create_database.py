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
import sqlite3

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
        cur.execute("CREATE TABLE %s %s;" % (tablename, headstr))
    except:
        pass

    with open(fpath,'rb') as fin:
        lines = fin.readlines()
        to_db = []
        lines.pop(0) # get rid of header
        for line in lines:
            line = line.decode("utf-8").replace(u'\xa6', "'")
            tokens = line.strip().split("|")
            to_db.append(tokens)

        #cur.executemany("INSERT INTO t (col1, col2) VALUES (?, ?);", to_db)
        cur.executemany("INSERT INTO %s %s VALUES %s;" % (tablename, headstr, qstr), to_db)
con.commit()
con.close()

