#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 11:07:49 2017

@author: root
"""

import DB

S = DB.sess

#q = S.query(DB.system_users).filter_by(action='activate user account').order_by(DB.AccessLog.date_time)
#q = sess.query(User).order_by(User.id)


# sess.dirty
# sess.new
# sess.commit()

employees = {}

q1 = S.query(DB.SystemUsers)


eid2uid = {}
uid2eid = {}

for u in q1:
   
    eid = u.employee_id
    uid = u.user_id
    eid2uid[eid] = uid
    uid2eid[uid] = eid
    if eid not in employees:
        employees[eid] = {}
    employees[eid]['SystemUsers'] = u
    
q2 = S.query(DB.Employee)

for e in q2:
    eid = e.employee_id
    if eid not in employees:
        employees[eid] = {}
    employees[eid]['Employee'] = e

q4 = S.query(DB.AuthorisationLevel)
gid2al = {}
for al in q4:
    gid = al.group_id
    gid2al[gid] = al
    
    
    
q3 = S.query(DB.UserGroups)
for ug in q3:
    uid = ug.user_id
    gid = ug.group_id
    
    print gid, uid

    eid = uid2eid[uid]
    if eid not in employees:
        employees[eid] = {}
    employees[eid]['UserGroups'] = ug
#    employees[eid]['AuthorisationLevel'] = gid2al[gid]


# use it like this
eid = uid2eid['u8284']
e = employees[eid]
print e
