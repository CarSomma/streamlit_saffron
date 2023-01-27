"""TODO
   Excercise: Explore the penguins pimped dataset :-) by following 
   the tasks. The data exploration would be the base on which we build 
   the streamlit app.

   Usage:
   After each task save the script and run the python script from the terminal.
   Be sure you are in the streamlit_env conda environment.
   If not activate the environment by typing in the terminal
   conda activate streamlit_env

   Mode:
   Work in group.
   
"""

### Import libraries
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

## Data exploration 

### Task1:
### Load the 'penguins_pimped.csv' file into a data frame df
### (it is under the folder /data/ )
### Print out 5 random sample from df 
### (Hint: apply the function sample() on df)

df = ...
df_sample = ...

print(df_sample)

### Task2:
### 2.1 Determine which islands are present in the data

island = ...

print(island)

### 2.2 Display the data for an island you choose from the dataframe 

my_island = '...'

my_island_df = df[df[...] == ...]

print(my_island_df.head())


### Task3
### Plotting
### Display a scatterplot: bill_length_mm vs bill_depth

fig, ax = plt.subplots()
ax = sns.scatterplot(
    data=...,
    x=...,
    y=...,
    hue='sex' # set to sex
    )

plt.show()
plt.close(fig)

### Click on X in the figure-window that pop up



### Task4
### Determine the average of the bill_length_mm by species

bill_length_mean = ...
print(bill_length_mean)



