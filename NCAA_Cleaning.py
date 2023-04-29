import pandas as pd
import numpy as np
import os

# NCAA Data

# Field Goal Stats
path = "Data/NCAA/Field Goals/"
all_df = []
# Iterate through files in folder
for file in os.listdir(path):
  filepath = path + file

  # Cleaning column data
  df = pd.read_csv(filepath)
  df['Player'] = df['Player'].str.split(", ").str[0]

  # Selecting specific columns and renaming
  df = df[['Player', 'Pos', 'G', 'FG', 'FGA']]
  df = df.rename(columns={'Pos': 'Position', 'G': 'Games Played', 'FGA': 'FG Attempt'}) 

  # Append all dataframes to an array before concat
  all_df.append(df)

# Concat and groupby to get totals
FieldGoal_df = pd.concat(all_df)
FieldGoal_df = FieldGoal_df.groupby(['Player', 'Position'], as_index=False).sum()

# Getting stat calculations
FieldGoal_df['FG Percentage'] = FieldGoal_df['FG'] / FieldGoal_df['FG Attempt'] * 100

FieldGoal_df = FieldGoal_df.round(2)
FieldGoal_df.to_csv('Output/NCAA_FG_Kickers.csv', index=False)
print("Field Goal Stats")
print(FieldGoal_df)

# Rushing Stats
path = "Data/NCAA/Rushing/"
all_df = []
# Iterate through files in folder
for file in os.listdir(path):
  filepath = path + file

  # Cleaning column data
  df = pd.read_csv(filepath)
  df['Player'] = df['Player'].str.split(", ").str[0]
  df['Rush Yds'] = df['Rush Yds'].map(str).str.replace(",", "").map(int)

  # Selecting specific columns and renaming
  df = df[['Player', 'Pos', 'G', 'Rush', 'Rush Yds', 'Rush TD']]
  df = df.rename(columns={'Pos': 'Position', 'G': 'Games Played'}) 

  # Append all dataframes to an array before concat
  all_df.append(df)

# Concat and groupby to get totals
Rushing_df = pd.concat(all_df)
Rushing_df = Rushing_df.groupby(['Player', 'Position'], as_index=False).sum()

# Getting stat calculations
Rushing_df['Rush Yds Per Attempt'] = Rushing_df['Rush Yds'] / Rushing_df['Rush']
Rushing_df['Rush Yds Per Game'] = Rushing_df['Rush Yds'] / Rushing_df['Games Played']
Rushing_df = Rushing_df[['Player', 'Position', 'Games Played', 'Rush', 'Rush Yds', 'Rush Yds Per Attempt', 'Rush TD', 'Rush Yds Per Game']]

Rushing_df = Rushing_df.round(2)
# print("Rushing Stats")
# print(Rushing_df)

# Receiving Stats
path = "Data/NCAA/Receiving/"
all_df = []
# Iterate through files in folder
for file in os.listdir(path):
  filepath = path + file

  # Cleaning column data
  df = pd.read_csv(filepath)
  df['Player'] = df['Player'].str.split(", ").str[0]
  df['Rec Yds'] = df['Rec Yds'].map(str).str.replace(",", "").map(int)

  # Selecting specific columns and renaming
  df = df[['Player', 'Pos', 'G', 'Rec', 'Rec Yds', 'Rec TD']]
  df = df.rename(columns={'Pos': 'Position', 'G': 'Games Played', 'Rec': 'Receptions', 'Rec Yds': 'Reception Yds', 'Rec TD': 'Reception TD'}) 

  # Append all dataframes to an array before concat
  all_df.append(df)

# Concat and groupby to get totals
Receiving_df = pd.concat(all_df)
Receiving_df = Receiving_df.groupby(['Player', 'Position'], as_index=False).sum()

# Getting stat calculations
Receiving_df['Reception Yds Per Attempt'] = Receiving_df['Reception Yds'] / Receiving_df['Receptions']
Receiving_df['Reception Yds Per Game'] = Receiving_df['Reception Yds'] / Receiving_df['Games Played']
Receiving_df = Receiving_df[['Player', 'Position', 'Games Played', 'Receptions', 'Reception Yds', 'Reception Yds Per Attempt', 'Reception TD', 'Reception Yds Per Game']]

Receiving_df = Receiving_df.round(2)
# print("Receiving Stats")
# print(Receiving_df)

# Passing Stats
path = "Data/NCAA/Passing/"
all_df = []
# Iterate through files in folder
for file in os.listdir(path):
  filepath = path + file

  # Cleaning column data
  df = pd.read_csv(filepath)
  df['Player'] = df['Player'].str.split(", ").str[0]
  df['Pass Yds'] = df['Pass Yds'].map(str).str.replace(",", "").map(int)

  # Selecting specific columns and renaming
  df = df[['Player', 'Pos', 'G', 'Pass Att', 'Pass Com', 'Int', 'Pass TD', 'Pass Yds']]
  df = df.rename(columns={'Pos': 'Position', 'G': 'Games Played', 'Pass Com': 'Pass Comp'}) 

  # Append all dataframes to an array before concat
  all_df.append(df)

# Concat and groupby to get totals
Passing_df = pd.concat(all_df)
Passing_df = Passing_df.groupby(['Player', 'Position'], as_index=False).sum()

# Getting stat calculations
Passing_df['Pass Comp Percentage'] = Passing_df['Pass Comp'] / Passing_df['Pass Att'] * 100
Passing_df['Pass Yds Per Comp'] = Passing_df['Pass Yds'] / Passing_df['Pass Comp']
Passing_df['Pass Yds Per Game'] = Passing_df['Pass Yds'] / Passing_df['Games Played']
Passing_df = Passing_df[['Player', 'Position', 'Games Played', 'Pass Att', 'Pass Comp', 'Pass Comp Percentage', 'Int', 'Pass TD', 'Pass Yds', 'Pass Yds Per Comp', 'Pass Yds Per Game']]

Passing_df = Passing_df.round(2)
# print("Passing Stats")
# print(Passing_df)

# Tackling Stats
path = "Data/NCAA/Tackles/"
all_df = []
# Iterate through files in folder
for file in os.listdir(path):
  filepath = path + file

  # Cleaning column data
  df = pd.read_csv(filepath)
  df['Player'] = df['Player'].str.split(", ").str[0]

  # Selecting specific columns and renaming
  df = df[['Player', 'Pos', 'G', 'Solo Tack', 'Asst Tack', 'TT']]
  df = df.rename(columns={'Pos': 'Position', 'G': 'Games Played', 'Solo Tack': 'Solo Tackles', 'Asst Tack': 'Asst Tackles', 'TT': 'Total Tackles'}) 

  # Append all dataframes to an array before concat
  all_df.append(df)

# Concat and groupby to get totals
Tackle_df = pd.concat(all_df)
Tackle_df = Tackle_df.groupby(['Player', 'Position'], as_index=False).sum()

# Getting stat calculations
Tackle_df['Tackles Per Game'] = Tackle_df['Total Tackles'] / Tackle_df['Games Played']

Tackle_df = Tackle_df.round(2)
# print("Tackling Stats")
# print(Tackle_df)

# Sacking Stats
path = "Data/NCAA/Sacks/"
all_df = []
# Iterate through files in folder
for file in os.listdir(path):
  filepath = path + file

  # Cleaning column data
  df = pd.read_csv(filepath)
  df['Player'] = df['Player'].str.split(", ").str[0]

  # Selecting specific columns and renaming
  df = df[['Player', 'Pos', 'G', 'Solo Sack', 'Asst Sack', 'Sack Yds', 'Tot Sack']]
  df = df.rename(columns={'Pos': 'Position', 'G': 'Games Played', 'Tot Sack': 'Total Sacks'}) 

  # Append all dataframes to an array before concat
  all_df.append(df)

# Concat and groupby to get totals
Sack_df = pd.concat(all_df)
Sack_df = Sack_df.groupby(['Player', 'Position'], as_index=False).sum()

# Getting stat calculations
Sack_df['Sacks Per Game'] = Sack_df['Total Sacks'] / Sack_df['Games Played']

Sack_df = Sack_df.round(2)
# print("Sacking Stats")
# print(Sack_df)

# Forced Fumble Stats
path = "Data/NCAA/Forced Fumbles/"
all_df = []
# Iterate through files in folder
for file in os.listdir(path):
  filepath = path + file

  # Cleaning column data
  df = pd.read_csv(filepath)
  df['Player'] = df['Player'].str.split(", ").str[0]

  # Selecting specific columns and renaming
  df = df[['Player', 'Pos', 'G', 'FF']]
  df = df.rename(columns={'Pos': 'Position', 'G': 'Games Played', 'FF': 'Forced Fumbles'}) 

  # Append all dataframes to an array before concat
  all_df.append(df)

# Concat and groupby to get totals
Forced_Fumbles_df = pd.concat(all_df)
Forced_Fumbles_df = Forced_Fumbles_df.groupby(['Player', 'Position'], as_index=False).sum()

# Getting stat calculations
Forced_Fumbles_df['Forced Fumbles Per Game'] = Forced_Fumbles_df['Forced Fumbles'] / Forced_Fumbles_df['Games Played']

Forced_Fumbles_df = Forced_Fumbles_df.round(2)
# print("Forced Fumbles Stats")
# print(Forced_Fumbles_df)

# Fumble Recovered Stats
path = "Data/NCAA/Fumbles Recovered/"
all_df = []
# Iterate through files in folder
for file in os.listdir(path):
  filepath = path + file

  # Cleaning column data
  df = pd.read_csv(filepath)
  df['Player'] = df['Player'].str.split(", ").str[0]

  # Selecting specific columns and renaming
  df = df[['Player', 'Pos', 'G', 'Fum Rec']]
  df = df.rename(columns={'Pos': 'Position', 'G': 'Games Played', 'Fum Rec': 'Fumbles Recovered'}) 

  # Append all dataframes to an array before concat
  all_df.append(df)

# Concat and groupby to get totals
Fumbles_Recovered_df = pd.concat(all_df)
Fumbles_Recovered_df = Fumbles_Recovered_df.groupby(['Player', 'Position'], as_index=False).sum()

# Getting stat calculations
Fumbles_Recovered_df['Fumbles Recovered Per Game'] = Fumbles_Recovered_df['Fumbles Recovered'] / Fumbles_Recovered_df['Games Played']

Fumbles_Recovered_df = Fumbles_Recovered_df.round(2)
# print("Fumbles Recovered Stats")
# print(Fumbles_Recovered_df)

# Pass Defense Stats
path = "Data/NCAA/Pass Defense/"
all_df = []
# Iterate through files in folder
for file in os.listdir(path):
  filepath = path + file

  # Cleaning column data
  df = pd.read_csv(filepath)
  df['Player'] = df['Player'].str.split(", ").str[0]

  # Selecting specific columns and renaming
  df = df[['Player', 'Pos', 'G', 'PBU']]
  df = df.rename(columns={'Pos': 'Position', 'G': 'Games Played', 'PBU': 'Passes Defended'}) 

  # Append all dataframes to an array before concat
  all_df.append(df)

# Concat and groupby to get totals
Pass_Defense_df = pd.concat(all_df)
Pass_Defense_df = Pass_Defense_df.groupby(['Player', 'Position'], as_index=False).sum()

Pass_Defense_df = Pass_Defense_df.round(2)
# print("Pass Defense Stats")
# print(Pass_Defense_df)

# Interception Stats
path = "Data/NCAA/Interceptions/"
all_df = []
# Iterate through files in folder
for file in os.listdir(path):
  filepath = path + file

  # Cleaning column data
  df = pd.read_csv(filepath)
  df['Player'] = df['Player'].str.split(", ").str[0]

  # Selecting specific columns and renaming
  df = df[['Player', 'Pos', 'G', 'Int', 'Int Ret Yds', 'Int Ret TDs']]
  df = df.rename(columns={'Pos': 'Position', 'G': 'Games Played'}) 

  # Append all dataframes to an array before concat
  all_df.append(df)

# Concat and groupby to get totals
Interception_df = pd.concat(all_df)
Interception_df = Interception_df.groupby(['Player', 'Position'], as_index=False).sum()

# Getting stat calculations
Interception_df['Yds Per Int'] = Interception_df['Int Ret Yds'] / Interception_df['Int']

Interception_df = Interception_df.round(2)
# print("Interception Stats")
# print(Interception_df)


# Merging and Outputting NCAA Dataframes

# Running Back Dataframe
All_Rushing_df = Rushing_df.merge(Receiving_df, left_on=['Player', 'Position'], right_on=['Player', 'Position'], how='left')
All_Rushing_df = All_Rushing_df.drop(columns=['Games Played_y']).rename(columns={'Games Played_x': 'Games Played'}).replace(np.nan, 0)

All_Rushing_df.to_csv('Output/NCAA_Runningbacks.csv', index=False)
print("Running Back Stats")
print(All_Rushing_df)

# Receivers Dataframe
All_Receiver_df = Receiving_df.merge(Rushing_df, left_on=['Player', 'Position'], right_on=['Player', 'Position'], how='left')
All_Receiver_df = All_Receiver_df.drop(columns=['Games Played_y']).rename(columns={'Games Played_x': 'Games Played'}).replace(np.nan, 0)

All_Receiver_df.to_csv('Output/NCAA_Receivers.csv', index=False)
print("Receiver Stats")
print(All_Receiver_df)

# Quarterback Dataframe
All_QB_df = Passing_df.merge(Rushing_df, left_on=['Player', 'Position'], right_on=['Player', 'Position'], how='left')
All_QB_df = All_QB_df.drop(columns=['Games Played_y']).rename(columns={'Games Played_x': 'Games Played'}).replace(np.nan, 0)

All_QB_df.to_csv('Output/NCAA_Quarterbacks.csv', index=False)
print("Quarterback Stats")
print(All_QB_df)

# Defense Stats
Sack_df = Sack_df.loc[:, Sack_df.columns != 'Games Played']
All_Defense_df = Tackle_df.merge(Sack_df, left_on=['Player', 'Position'], right_on=['Player', 'Position'], how='left')

Forced_Fumbles_df = Forced_Fumbles_df.loc[:, Forced_Fumbles_df.columns != 'Games Played']
All_Defense_df = All_Defense_df.merge(Forced_Fumbles_df, left_on=['Player', 'Position'], right_on=['Player', 'Position'], how='left')

Fumbles_Recovered_df = Fumbles_Recovered_df.loc[:, Fumbles_Recovered_df.columns != 'Games Played']
All_Defense_df = All_Defense_df.merge(Fumbles_Recovered_df, left_on=['Player', 'Position'], right_on=['Player', 'Position'], how='left')

Pass_Defense_df = Pass_Defense_df.loc[:, Pass_Defense_df.columns != 'Games Played']
All_Defense_df = All_Defense_df.merge(Pass_Defense_df, left_on=['Player', 'Position'], right_on=['Player', 'Position'], how='left')

Interception_df = Interception_df.loc[:, Interception_df.columns != 'Games Played']
All_Defense_df = All_Defense_df.merge(Interception_df, left_on=['Player', 'Position'], right_on=['Player', 'Position'], how='left')


All_Defense_df = All_Defense_df.replace(np.nan, 0)
All_Defense_df.to_csv('Output/NCAA_Defense.csv', index=False)
print("Defense Stats")
print(All_Defense_df)
