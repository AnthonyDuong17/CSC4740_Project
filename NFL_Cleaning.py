import pandas as pd
import numpy as np
import os

# NFL Stats

# Kicker Stats
path = "Data/NFL/Field Goals/"
all_df = []
# Iterate through files in folder
for file in os.listdir(path):
  filepath = path + file

  # Cleaning column data
  df = pd.read_csv(filepath, skiprows=1)

  df['Player'] = df['Player'].str.replace("*", "").str.replace("+", "")

  # Selecting specific columns and renaming
  df = df[['Player', 'Pos', 'G', 'FGM.5', 'FGA.5']]
  df = df.rename(columns={'Pos': 'Position', 'G': 'Games Played', 'FGM.5': 'FG', 'FGA.5': 'FG Attempt'}) 

  df = df[df['FG Attempt'] > 0]

  # Append all dataframes to an array before concat
  all_df.append(df)

# Concat and groupby to get totals
NFL_Kicker_df = pd.concat(all_df)
NFL_Kicker_df = NFL_Kicker_df.groupby(['Player', 'Position'], as_index=False).sum()

# Getting stat calculations
NFL_Kicker_df['FG Percentage'] = NFL_Kicker_df['FG'] / NFL_Kicker_df['FG Attempt'] * 100

NFL_Kicker_df = NFL_Kicker_df.round(2)
NFL_Kicker_df.to_csv('Output/NFL_FG_Kickers.csv', index=False)
print("Kicker Stats")
print(NFL_Kicker_df)

# Defense Stats
path = "Data/NFL/Defense/"
all_df = []
# Iterate through files in folder
for file in os.listdir(path):
  filepath = path + file

  # Cleaning column data
  df = pd.read_csv(filepath, skiprows=1)
  df['Player'] = df['Player'].str.replace("*", "").str.replace("+", "")

  # Selecting specific columns and renaming
  df = df[['Player', 'Pos', 'G', 'Solo', 'Ast', 'Comb', 'Sk', 'FF', 'FR', 'PD', 'Int', 'Yds', 'TD']]
  df = df.rename(columns={'Pos': 'Position', 'G': 'Games Played', 'Solo': 'Solo Tackles', 'Ast': 'Asst Tackles', 'Comb': 'Total Tackles', 'Sk': 'Total Sacks', 'FF': 'Forced Fumbles', 'FR': 'Fumbles Recovered', 'PD': 'Passes Defended', 'Yds': 'Int Ret Yds', 'TD': 'Int Ret TDs'}) 

  # Append all dataframes to an array before concat
  all_df.append(df)

# Concat and groupby to get totals
NFL_Defense_df = pd.concat(all_df)
NFL_Defense_df = NFL_Defense_df.groupby(['Player', 'Position'], as_index=False).sum()

# Getting stat calculations
NFL_Defense_df['Tackles Per Game'] = NFL_Defense_df['Total Tackles'] / NFL_Defense_df['Games Played']
NFL_Defense_df['Sacks Per Game'] = NFL_Defense_df['Total Sacks'] / NFL_Defense_df['Games Played']
NFL_Defense_df['Yds Per Int'] = NFL_Defense_df['Int Ret Yds'] / NFL_Defense_df['Int']

NFL_Defense_df = NFL_Defense_df[['Player', 'Position', 'Games Played', 'Solo Tackles', 'Asst Tackles', 'Total Tackles', 'Tackles Per Game', 'Total Sacks', 'Sacks Per Game', 'Forced Fumbles', 'Fumbles Recovered', 'Passes Defended', 'Int', 'Int Ret Yds', 'Yds Per Int', 'Int Ret TDs']]

NFL_Defense_df = NFL_Defense_df.round(2).replace(np.nan, 0)
NFL_Defense_df.to_csv('Output/NFL_Defense.csv', index=False)
print("Defense Stats")
print(NFL_Defense_df)

# Passing Stats
path = "Data/NFL/Passing/"
all_df = []
# Iterate through files in folder
for file in os.listdir(path):
  filepath = path + file

  # Cleaning column data
  df = pd.read_csv(filepath)
  df['Player'] = df['Player'].str.replace("*", "").str.replace("+", "")

  # Selecting specific columns and renaming
  df = df[['Player', 'Pos', 'G', 'Cmp', 'Att', 'Yds', 'TD', 'Int']]
  df = df.rename(columns={'Pos': 'Position', 'G': 'Games Played', 'Att': 'Pass Att', 'Cmp': 'Pass Comp', 'Yds': 'Pass Yds', 'TD': 'Pass TD'}) 

  # Append all dataframes to an array before concat
  all_df.append(df)

# Concat and groupby to get totals
NFL_Passing_df = pd.concat(all_df)
NFL_Passing_df = NFL_Passing_df.groupby(['Player', 'Position'], as_index=False).sum()

# Getting stat calculations
NFL_Passing_df['Pass Comp Percentage'] = NFL_Passing_df['Pass Comp'] / NFL_Passing_df['Pass Att'] * 100
NFL_Passing_df['Pass Yds Per Comp'] = NFL_Passing_df['Pass Yds'] / NFL_Passing_df['Pass Comp']
NFL_Passing_df['Pass Yds Per Game'] = NFL_Passing_df['Pass Yds'] / NFL_Passing_df['Games Played']

NFL_Passing_df = NFL_Passing_df[['Player',	'Position',	'Games Played',	'Pass Comp',	'Pass Att', 'Pass Comp Percentage', 'Pass Yds',	'Pass Yds Per Comp', 'Pass Yds Per Game', 'Pass TD', 'Int']]

NFL_Passing_df = NFL_Passing_df.round(2)
# print(NFL_Passing_df)

# Rushing Stats
path = "Data/NFL/Rushing/"
all_df = []
# Iterate through files in folder
for file in os.listdir(path):
  filepath = path + file

  # Cleaning column data
  df = pd.read_csv(filepath, skiprows=1)
  df['Player'] = df['Player'].str.replace("*", "").str.replace("+", "")

  # Selecting specific columns and renaming
  df = df[['Player', 'Pos', 'G', 'Att', 'Yds', 'TD']]
  df = df.rename(columns={'Pos': 'Position', 'G': 'Games Played', 'Att': 'Rush', 'Yds': 'Rush Yds', 'TD': 'Rush TD'}) 

  # Append all dataframes to an array before concat
  all_df.append(df)

# Concat and groupby to get totals
NFL_Rushing_df = pd.concat(all_df)
NFL_Rushing_df = NFL_Rushing_df.groupby(['Player', 'Position'], as_index=False).sum()

# Getting stat calculations
NFL_Rushing_df['Rush Yds Per Attempt'] = NFL_Rushing_df['Rush Yds'] / NFL_Rushing_df['Rush']
NFL_Rushing_df['Rush Yds Per Game'] = NFL_Rushing_df['Rush Yds'] / NFL_Rushing_df['Games Played']


NFL_Rushing_df = NFL_Rushing_df.round(2)
# print(NFL_Rushing_df)

# Receiving Stats
path = "Data/NFL/Receiving/"
all_df = []
# Iterate through files in folder
for file in os.listdir(path):
  filepath = path + file

  # Cleaning column data
  df = pd.read_csv(filepath)
  df['Player'] = df['Player'].str.replace("*", "").str.replace("+", "")

  # Selecting specific columns and renaming
  df = df[['Player', 'Pos', 'G', 'Tgt', 'Rec', 'Yds', 'TD']]
  df = df.rename(columns={'Pos': 'Position', 'G': 'Games Played', 'Tgt': 'Targets', 'Rec': 'Receptions', 'Yds': 'Reception Yds', 'TD': 'Reception TD'}) 

  # Append all dataframes to an array before concat
  all_df.append(df)

# Concat and groupby to get totals
NFL_Receiving_df = pd.concat(all_df)
NFL_Receiving_df = NFL_Receiving_df.groupby(['Player', 'Position'], as_index=False).sum()

# Getting stat calculations
NFL_Receiving_df['Catch Percentage'] = NFL_Receiving_df['Receptions'] / NFL_Receiving_df['Targets'] * 100
NFL_Receiving_df['Reception Yds Per Attempt'] = NFL_Receiving_df['Reception Yds'] / NFL_Receiving_df['Receptions']
NFL_Receiving_df['Reception Yds Per Game'] = NFL_Receiving_df['Receptions'] / NFL_Receiving_df['Games Played']
NFL_Receiving_df = NFL_Receiving_df[['Player', 'Position', 'Games Played', 'Targets', 'Receptions', 'Catch Percentage', 'Reception Yds', 'Reception Yds Per Attempt', 'Reception Yds Per Game', 'Reception TD']]

NFL_Receiving_df = NFL_Receiving_df[NFL_Receiving_df['Receptions'] > 1]

NFL_Receiving_df = NFL_Receiving_df.round(2)
# print(NFL_Receiving_df)


# Merging and Outputting NFL Dataframes

# Quarterback Stats
NFL_Rushing_df2 = NFL_Rushing_df.loc[:, NFL_Rushing_df.columns != 'Games Played']
NFL_Quarterback_df = NFL_Passing_df.merge(NFL_Rushing_df2, left_on=['Player', 'Position'], right_on=['Player', 'Position'], how='left')
NFL_Quarterback_df = NFL_Quarterback_df[NFL_Quarterback_df['Position'] == 'QB']
NFL_Quarterback_df = NFL_Quarterback_df.replace(np.nan, 0)
NFL_Quarterback_df.to_csv('Output/NFL_Quarterback.csv', index=False)
print("Quarterback Stats")
print(NFL_Quarterback_df)

# Receiver Stats
NFL_Receiver_df = NFL_Receiving_df.merge(NFL_Rushing_df2, left_on=['Player', 'Position'], right_on=['Player', 'Position'], how='left')
NFL_Receiver_df = NFL_Receiver_df[(NFL_Receiver_df['Position'] == 'WR') | (NFL_Receiver_df['Position'] == 'TE')]
NFL_Receiver_df = NFL_Receiver_df.replace(np.nan, 0)
NFL_Receiver_df.to_csv('Output/NFL_Receivers.csv', index=False)
print("Receiver Stats")
print(NFL_Receiver_df)

# Runningback stats
NFL_Receiving_df2 = NFL_Receiving_df.loc[:, NFL_Receiving_df.columns != 'Games Played']
NFL_Runningbacks_df = NFL_Rushing_df.merge(NFL_Receiving_df2, left_on=['Player', 'Position'], right_on=['Player', 'Position'], how='left')
NFL_Runningbacks_df = NFL_Runningbacks_df[(NFL_Runningbacks_df['Position'] == 'RB') | (NFL_Runningbacks_df['Position'] == 'FB')]
NFL_Runningbacks_df = NFL_Runningbacks_df.replace(np.nan, 0)
NFL_Runningbacks_df.to_csv('Output/NFL_Runningbacks.csv', index=False)
print("Runningback Stats")
print(NFL_Runningbacks_df) 