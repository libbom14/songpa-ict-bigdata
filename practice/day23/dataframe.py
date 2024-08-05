#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 09:54:10 2024

@author: bella
"""

import pandas as pd
test = pd.read_excel("d:/data/test.xlsx")
test.dtypes
test["class"] = test["class"].astype("str")
class_label = {'1':'1반','2':'2반','3':'3반', '4':'4반','5':"5반"}
test["class"] = test["class"].map(class_label)
