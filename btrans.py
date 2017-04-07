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

#import csv

with open("bank_transfer_file.csv", 'r') as f:
    lines = f.readlines()
    
entries = []
for line in lines:
    tokens = line.strip().split("|")
    
    