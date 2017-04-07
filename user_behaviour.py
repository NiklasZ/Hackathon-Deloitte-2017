#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 11:07:49 2017

@author: root
"""

import DB

S = DB.sess

q = S.query(DB.AccessLog).filter_by(action='activate user account').order_by(DB.AccessLog.date_time)
#q = sess.query(User).order_by(User.id)


# sess.dirty
# sess.new
# sess.commit()
