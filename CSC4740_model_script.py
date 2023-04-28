# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 09:41:21 2023

@author: lanse
"""

import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/lanse/Downloads/Output/Output/NCAA_Defense.csv')
df1 = pd.read_csv('C:/Users/lanse/Downloads/Output/Output/NCAA_FG_Kickers.csv')
df2 = pd.read_csv('C:/Users/lanse/Downloads/Output/Output/NCAA_Quarterbacks.csv')
df3 = pd.read_csv('C:/Users/lanse/Downloads/Output/Output/NCAA_Receivers.csv')
df4 = pd.read_csv('C:/Users/lanse/Downloads/Output/Output/NCAA_Runningbacks.csv')
df5 = pd.read_csv('C:/Users/lanse/Downloads/Output/Output/NFL_FG_Kickers.csv')
df6= pd.read_csv('C:/Users/lanse/Downloads/Output/Output/NFL_Quarterback.csv')
df7 = pd.read_csv('C:/Users/lanse/Downloads/Output/Output/NFL_Receivers.csv')
df8 = pd.read_csv('C:/Users/lanse/Downloads/Output/Output/NFL_Runningbacks.csv')
df9 = pd.read_csv('C:/Users/lanse/Downloads/Output/Output/NFL_Defense.csv')

df.to_parquet('C:/Users/lanse/Downloads/Output/Output/NCAA_Defense.parquet')
df1.to_parquet('C:/Users/lanse/Downloads/Output/Output/NCAA_FG_Kickers.parquet')
df2.to_parquet('C:/Users/lanse/Downloads/Output/Output/NCAA_Quarterbacks.parquet')
df3.to_parquet('C:/Users/lanse/Downloads/Output/Output/NCAA_Receivers.parquet')
df4.to_parquet('C:/Users/lanse/Downloads/Output/Output/NCAA_Runningbacks.parquet')
df5.to_parquet('C:/Users/lanse/Downloads/Output/Output/NFL_FG_Kickers.parquet')
df6.to_parquet('C:/Users/lanse/Downloads/Output/Output/NFL_Quarterback.parquet')
df7.to_parquet('C:/Users/lanse/Downloads/Output/Output/NFL_Receivers.parquet')
df8.to_parquet('C:/Users/lanse/Downloads/Output/Output/NFL_Runningbacks.parquet')
df9.to_parquet('C:/Users/lanse/Downloads/Output/Output/NFL_Defense.parquet')