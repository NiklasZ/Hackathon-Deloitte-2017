# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#importing data
#import pandas as pd
#from sklearn import linear_model
#from sklearn.preprocessing import PolynomialFeatures
#import numpy as np

import csv

with open("bank_transfer_file.csv", 'r') as f:
    lines = f.readlines()
    
entries = []
data = {}
header = lines.pop(0).strip().split("|")
for line in lines:
    tokens = line.strip().split("|")
    
    idd = tokens[0]
    dt = tokens[1]
    account1 = tokens[2]
    account2 = tokens[3]
    amount = tokens[4]
    msg = tokens[5]
    
    entries.append(tokens)
    data[idd] = tokens
    
    
sdata = {}
for tokens in entries:
    idd = tokens[0]
    dt = tokens[1]
    account1 = tokens[2]
    account2 = tokens[3]
    amount = tokens[4]
    msg = tokens[5]
    
    if amount not in sdata:
        sdata[amount] = []
        
    sdata[amount].append(idd)

counts = {}
counts_bt_2 = {}
tot_count = 0
for k,v in sdata.items():
    counts[k] = len(v)
    if len(v)>2:
        counts_bt_2[k] = len(v)
        tot_count += len(v)
        
print "Count of transactions with same amounts:", len(counts_bt_2.keys()), "tot nr transactions:", tot_count



