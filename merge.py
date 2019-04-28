#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 21:30:04 2019

@author: dexter
"""

import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def match_name(item,item_list,min_score=0):
    max_score = -1
    # Returning empty name for no match as well
    max_name = ""
    # Iternating over all names in the other
    for name2 in list_names:
        #Finding fuzzy match score
        score = fuzz.ratio(name, name2)
        # Checking if we are above our threshold and have a better score
        if (score > min_score) & (score > max_score):
            max_name = name2
            max_score = score
    return (max_name, max_score)

data=pd.read_csv("test_cvs.csv")
data1=data.dropna()
for name in data1[['address','phone']].values.tolist():
    match=match_name()

