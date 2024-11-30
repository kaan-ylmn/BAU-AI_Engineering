import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Importing the required libareis for the project

# Task 1
df = pd.read_csv("diabetes.csv")
# Reading diabetes.csv file, then assign the dataframe to df variable

# Task 2
print(df.head(10))
# Printing the first 10 rows of the dataframe

# Task 3
print(df.info())
# Printing the information about the data types, columns, null value counts, memory consumption

# Task 4
print(df.describe())
# Printing the basic statistical details about the data

# Task 5
print(df.describe().T)
# Taking the transpose of the dataframe for reversing the axes

# Task 6
# df.loc[:,["Glucose","BloodPressure","SkinThickness","Insulin","BMI"]] = df.replace(0,np.nan)
df.iloc[:,1:6] = df.iloc[:,1:6].replace(0,np.nan)
# Both two rows transform the selected columns' 0 values to NAN
print(df)

# Task 7
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 15))
# Creating 3 by 3 grid and adjust the grid size
for i in range(3):
  for j in range(3):
    sns.histplot(data = df, x = df.columns[3*i+j], ax=axes[i][j])
    # histplot makes a histogram graph for specified column name from provided data
    axes[i][j].set_title(df.columns[3*i+j] + " Distribution")
    # Setting title for specified column name
plt.show()
# Showing the graph grid

# Task 8
df.fillna(method = "ffill",inplace = True)
df.fillna(method = "bfill", inplace = True)
# fillna function fill the nan values ​​according to the given value
# bfill method fill the nan values ​​according to the next value
# ffill method fill the nan values ​​according to the previous value
# inplace argument directly modifies the dataframe without requiring assignment
print(df)

# Task 9
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 15))
for i in range(3):
  for j in range(3):
    sns.histplot(data = df, x = df.columns[3*i+j], ax=axes[i][j])
    axes[i][j].set_title(df.columns[3*i+j] + " Distribution")
plt.show()