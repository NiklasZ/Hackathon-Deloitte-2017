#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 10:28:56 2017

@author: root
"""



import DB
S = DB.sess


q = S.query(DB.InvoicePurchaseOrder)

puos = []
for i in q:
    puos.append((int(i.po_id[4:]),i.vendor_id))

puos = sorted(puos)

multiples = {}
lookup = {}

for i, elem in enumerate(puos):
    if i-1<0: continue # skip first
    puo, vid = elem
    puop, vidp = puos[i-1]

    if puop + 1 == puo and vidp == vid:
        start = lookup[puo-1]
        lookup[puo] = start
        multiples[start].append(puo)
        
    else:
        lookup[puo] = puo
        multiples[puo] = [puo,]
        
rmult = []
count = 0
for k,v in multiples.items():
    if len(v)>1:
        print k, len(v), v
        count += len(v)
        rmult.append(k)