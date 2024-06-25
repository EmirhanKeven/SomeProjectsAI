# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 19:45:21 2024

@author: emirh
"""

import pandas as pd
import matplotlib.pyplot as plt
from pytrends.request import TrendReq

pytrends = TrendReq()

pytrends.build_payload(kw_list=['dark souls'], timeframe='2015-01-01 2024-01-01', geo='',gprop='')

df = pytrends.related_topics()

lst = df['dark souls']

rising_values = df['dark souls']['rising']
print(rising_values.head())

print(pytrends.top_charts(date='2023' ,geo='TR'))