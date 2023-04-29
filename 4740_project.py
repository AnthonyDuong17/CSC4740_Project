# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 22:03:48 2023

@author: lanse
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np

# df = pd.read_csv('C:/Users/lanse/Downloads/Output/Output/NCAA_Defense.csv')
# df1 = pd.read_csv('C:/Users/lanse/Downloads/Output/Output/NCAA_FG_Kickers.csv')
df_NCAA_Passer = pd.read_csv('C:/Users/lanse/Downloads/Output/Output/NCAA_Quarterbacks.csv')
# df3 = pd.read_csv('C:/Users/lanse/Downloads/Output/Output/NCAA_Receivers.csv')
df_NCAA_Rusher  = pd.read_csv('C:/Users/lanse/Downloads/Output/Output/NCAA_Runningbacks.csv')
# df5 = pd.read_csv('C:/Users/lanse/Downloads/Output/Output/NFL_FG_Kickers.csv')
df_NFL_Passer= pd.read_csv('C:/Users/lanse/Downloads/Output/Output/NFL_Quarterback.csv')
# df7 = pd.read_csv('C:/Users/lanse/Downloads/Output/Output/NFL_Receivers.csv')
df_NFL_Rusher  = pd.read_csv('C:/Users/lanse/Downloads/Output/Output/NFL_Runningbacks.csv')
# df9 = pd.read_csv('C:/Users/lanse/Downloads/Output/Output/NFL_Defense.csv')
good_players_df = pd.read_csv("C:/Users/lanse/Downloads/Output/cheatsheet_04282023.csv")
good_players_list = good_players_df['Player']

df_NCAA_Passer['is_star'] = 0
for player in good_players_list:   
    # df_NCAA_Passer[df_NCAA_Passer['Player'] == player]['is_star'] = 1
    df_NCAA_Passer.loc[df_NCAA_Passer['Player'] == player,'is_star'] = 1
df_NCAA_Rusher['is_star'] = 0
for player in good_players_list:   
    # df_NCAA_Passer[df_NCAA_Passer['Player'] == player]['is_star'] = 1
    df_NCAA_Rusher.loc[df_NCAA_Rusher['Player'] == player,'is_star'] = 1
df_NFL_Passer['is_star'] = 0
for player in good_players_list:   
    # df_NCAA_Passer[df_NCAA_Passer['Player'] == player]['is_star'] = 1
    df_NFL_Passer.loc[df_NFL_Passer['Player'] == player,'is_star'] = 1
df_NFL_Rusher['is_star'] = 0
for player in good_players_list:   
    # df_NCAA_Passer[df_NCAA_Passer['Player'] == player]['is_star'] = 1
    df_NFL_Rusher.loc[df_NFL_Rusher['Player'] == player,'is_star'] = 1
    
    
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn.metrics import accuracy_score as acc

X_ncaa_passer = df_NCAA_Passer.drop(columns=['Player', 'Position', 'is_star'])
y_ncaa_passer = df_NCAA_Passer['is_star']


X_train_ncaa_passer, X_test_ncaa_passer, y_train_ncaa_passer, y_test_ncaa_passer = train_test_split(X_ncaa_passer, y_ncaa_passer, test_size=0.27)

X_train_ncaa_passer.head()
y_test_ncaa_passer.head()
model_1_passer = dtc(max_depth=3)
model_1_passer.fit(X_train_ncaa_passer, y_train_ncaa_passer)

y_pred_ncaa_passer = model_1_passer.predict(X_test_ncaa_passer)
score_1 = acc(y_test_ncaa_passer, y_pred_ncaa_passer)

X_nfl_passer = df_NFL_Passer.drop(columns=['Player', 'Position', 'is_star'])
y_nfl_passer = df_NFL_Passer['is_star']


X_train_nfl_passer, X_test_nfl_passer, y_train_nfl_passer, y_test_nfl_passer = train_test_split(X_nfl_passer, y_nfl_passer, test_size=0.27)

X_train_nfl_passer.head()
y_test_nfl_passer.head()
model_2_passer = dtc(max_depth=6)
model_2_passer.fit(X_train_nfl_passer, y_train_nfl_passer)

y_pred_nfl_passer = model_2_passer.predict(X_test_nfl_passer)
score_2 = acc(y_test_nfl_passer, y_pred_nfl_passer)


X_ncaa_rusher = df_NFL_Passer.drop(columns=['Player', 'Position', 'is_star'])
y_ncaa_rusher = df_NFL_Passer['is_star']


X_train_ncaa_rusher, X_test_ncaa_rusher, y_train_ncaa_rusher, y_test_ncaa_rusher = train_test_split(X_ncaa_rusher, y_ncaa_rusher, test_size=0.27)

X_train_ncaa_rusher.head()
y_test_ncaa_rusher.head()
model_1_rusher = dtc(max_depth=9)
model_1_rusher.fit(X_train_ncaa_rusher, y_train_ncaa_rusher)

y_pred_ncaa_rusher = model_1_rusher.predict(X_test_ncaa_rusher)
score_3 = acc(y_test_ncaa_rusher, y_pred_ncaa_rusher)

X_nfl_rusher = df_NFL_Passer.drop(columns=['Player', 'Position', 'is_star'])
y_nfl_rusher = df_NFL_Passer['is_star']


X_train_nfl_rusher, X_test_nfl_rusher, y_train_nfl_rusher, y_test_nfl_rusher = train_test_split(X_nfl_rusher, y_nfl_rusher, test_size=0.27)

X_train_nfl_rusher.head()
y_test_nfl_rusher.head()
model_2_rusher = dtc(max_depth=5)
model_2_rusher.fit(X_train_nfl_rusher, y_train_nfl_rusher)

y_pred_nfl_rusher = model_2_rusher.predict(X_test_nfl_rusher)
score_4 = acc(y_test_nfl_rusher, y_pred_nfl_rusher)






# df_NCAA_Passer['is_star'] = np.where(0 if x in good_players_list else 0 for x in df_NCAA_Passer['Player'] )