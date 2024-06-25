# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 17:44:18 2024

@author: emirh
"""

import pandas as pd
import matplotlib.pyplot as plt
from pytrends.request import TrendReq

pytrends = TrendReq()

kw_list = ['dark souls','minecraft','gta', 'elden ring','terraria']

pytrends.build_payload(kw_list, timeframe='2015-01-01 2024-01-01',geo='', gprop='')

df = pytrends.interest_over_time()

df.to_excel('trend_analiz_1.xlsx')

plt.figure(figsize=(20,14))
plt.plot(df.index,df['dark souls'],'k')
plt.plot(df.index,df.minecraft,'r')
plt.plot(df.index,df.gta,'b')
plt.plot(df.index,df["elden ring"],'g')
plt.plot(df.index,df.terraria,'p')
plt.legend(['dark souls','minecraft','gta','elden ring','terraria'])

plt.show()