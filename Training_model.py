import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn.metrics import accuracy_score as acc


df_NCAA_Passer = pd.read_csv('Output/NCAA_Quarterbacks.csv')
df_NCAA_Receiver = pd.read_csv('Output/NCAA_Receivers.csv')
df_NCAA_Rusher  = pd.read_csv('Output/NCAA_Runningbacks.csv')
df_NFL_Passer= pd.read_csv('Output/NFL_Quarterback.csv')
df_NFL_Receiver = pd.read_csv('Output/NFL_Receivers.csv')
df_NFL_Rusher  = pd.read_csv('Output/NFL_Runningbacks.csv')
good_players_df = pd.read_csv("Output/cheatsheet_04282023.csv")
good_players_list = good_players_df['Player']

df_NCAA_Passer['is_star'] = 0
for player in good_players_list:   
    df_NCAA_Passer.loc[df_NCAA_Passer['Player'] == player,'is_star'] = 1

df_NCAA_Rusher['is_star'] = 0
for player in good_players_list:   
    df_NCAA_Rusher.loc[df_NCAA_Rusher['Player'] == player,'is_star'] = 1

df_NCAA_Receiver['is_star'] = 0
for player in good_players_list:   
    df_NCAA_Receiver.loc[df_NCAA_Receiver['Player'] == player,'is_star'] = 1

df_NFL_Passer['is_star'] = 0
for player in good_players_list:   
    df_NFL_Passer.loc[df_NFL_Passer['Player'] == player,'is_star'] = 1

df_NFL_Rusher['is_star'] = 0
for player in good_players_list:   
    df_NFL_Rusher.loc[df_NFL_Rusher['Player'] == player,'is_star'] = 1

df_NFL_Receiver['is_star'] = 0
for player in good_players_list:   
    df_NFL_Receiver.loc[df_NFL_Receiver['Player'] == player,'is_star'] = 1


X_ncaa_passer = df_NCAA_Passer.drop(columns=['Player', 'Position', 'is_star'])
y_ncaa_passer = df_NCAA_Passer['is_star']

X_train_ncaa_passer, X_test_ncaa_passer, y_train_ncaa_passer, y_test_ncaa_passer = train_test_split(X_ncaa_passer, y_ncaa_passer, test_size=0.27)

X_train_ncaa_passer.head()
y_test_ncaa_passer.head()
model_1_passer = dtc(max_depth=3)
model_1_passer.fit(X_train_ncaa_passer, y_train_ncaa_passer)

y_pred_ncaa_passer = model_1_passer.predict(X_test_ncaa_passer)
score_1 = acc(y_test_ncaa_passer, y_pred_ncaa_passer)
print("NCAA Passing stat accuracy: " + str(score_1))


X_nfl_passer = df_NFL_Passer.drop(columns=['Player', 'Position', 'is_star'])
y_nfl_passer = df_NFL_Passer['is_star']

X_train_nfl_passer, X_test_nfl_passer, y_train_nfl_passer, y_test_nfl_passer = train_test_split(X_nfl_passer, y_nfl_passer, test_size=0.27)

X_train_nfl_passer.head()
y_test_nfl_passer.head()
model_2_passer = dtc(max_depth=6)
model_2_passer.fit(X_train_nfl_passer, y_train_nfl_passer)

y_pred_nfl_passer = model_2_passer.predict(X_test_nfl_passer)
score_2 = acc(y_test_nfl_passer, y_pred_nfl_passer)
print("NFL Passing stat accuracy: " + str(score_2))


X_ncaa_rusher = df_NCAA_Rusher.drop(columns=['Player', 'Position', 'is_star'])
y_ncaa_rusher = df_NCAA_Rusher['is_star']

X_train_ncaa_rusher, X_test_ncaa_rusher, y_train_ncaa_rusher, y_test_ncaa_rusher = train_test_split(X_ncaa_rusher, y_ncaa_rusher, test_size=0.27)

X_train_ncaa_rusher.head()
y_test_ncaa_rusher.head()
model_1_rusher = dtc(max_depth=9)
model_1_rusher.fit(X_train_ncaa_rusher, y_train_ncaa_rusher)

y_pred_ncaa_rusher = model_1_rusher.predict(X_test_ncaa_rusher)
score_3 = acc(y_test_ncaa_rusher, y_pred_ncaa_rusher)
print("NCAA Rushing stat accuracy: " + str(score_3))


X_nfl_rusher = df_NFL_Rusher.drop(columns=['Player', 'Position', 'is_star'])
y_nfl_rusher = df_NFL_Rusher['is_star']

X_train_nfl_rusher, X_test_nfl_rusher, y_train_nfl_rusher, y_test_nfl_rusher = train_test_split(X_nfl_rusher, y_nfl_rusher, test_size=0.27)

X_train_nfl_rusher.head()
y_test_nfl_rusher.head()
model_2_rusher = dtc(max_depth=5)
model_2_rusher.fit(X_train_nfl_rusher, y_train_nfl_rusher)

y_pred_nfl_rusher = model_2_rusher.predict(X_test_nfl_rusher)
score_4 = acc(y_test_nfl_rusher, y_pred_nfl_rusher)
print("NFL Rushing stat accuracy: " + str(score_3))


X_ncaa_receiver = df_NCAA_Receiver.drop(columns=['Player', 'Position', 'is_star'])
y_ncaa_receiver = df_NCAA_Receiver['is_star']

X_train_ncaa_receiver, X_test_ncaa_receiver, y_train_ncaa_receiver, y_test_ncaa_receiver = train_test_split(X_ncaa_receiver, y_ncaa_receiver, test_size=0.27)

X_train_ncaa_receiver.head()
y_test_ncaa_receiver.head()
model_1_receiver = dtc(max_depth=9)
model_1_receiver.fit(X_train_ncaa_receiver, y_train_ncaa_receiver)

y_pred_ncaa_receiver = model_1_receiver.predict(X_test_ncaa_receiver)
score_3 = acc(y_test_ncaa_receiver, y_pred_ncaa_receiver)
print("NCAA Receiving stat accuracy: " + str(score_3))


X_nfl_receiver = df_NFL_Receiver.drop(columns=['Player', 'Position', 'is_star'])
y_nfl_receiver = df_NFL_Receiver['is_star']

X_train_nfl_receiver, X_test_nfl_receiver, y_train_nfl_receiver, y_test_nfl_receiver = train_test_split(X_nfl_receiver, y_nfl_receiver, test_size=0.27)

X_train_nfl_receiver.head()
y_test_nfl_receiver.head()
model_2_receiver = dtc(max_depth=5)
model_2_receiver.fit(X_train_nfl_receiver, y_train_nfl_receiver)

y_pred_nfl_receiver = model_2_receiver.predict(X_test_nfl_receiver)
score_4 = acc(y_test_nfl_receiver, y_pred_nfl_receiver)
print("NFL Receiving stat accuracy: " + str(score_3))
