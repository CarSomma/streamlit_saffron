# Streamlit Tutorial: Exploring the PenguinsPalmer Dataset

This Streamlit tutorial guides you through creating an interactive data exploration app using the palmerpenguins dataset and is based on the [penguins exercise](README.md#data-analysis-excercise-on-penguins). Therefore, please make sure to complete first the penguins excercise, and  then follow the tasks step by step to build your app.

## Task 1: Environment Setup

Before we start, ensure you are working within your Streamlit environment. If not, activate the environment with the following command:

```bash
# Mac/Linux user
source streamlit_env/bin/activate
# Windows user
.\streamlit_env\Scripts\activate.ps1 
```

## Task 2: Import Libraries

Import the required libraries for your Streamlit app:

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
```

## Task 3: Title and Introduction

Set a title for your Streamlit app and provide an introduction to the dataset:

```python
# Set the title
st.title("Funfact about penguins🐧")

# Add an image and description
st.image('penguins.png')
st.markdown("This is the [palmerpenguins](https://allisonhorst.github.io/palmerpenguins/) dataset that describes measurements on penguins")
st.markdown("---")
```

## Task 4: Load and Display Data

Load the penguins dataset and display a sample:

```python
# Load the penguins dataset
df = pd.read_csv("./data/penguins_pimped.csv")

# Display a sample of the dataset
df_sample = df.sample(n=5)
st.header("Penguins 🐧 data")
st.dataframe(df_sample)
st.markdown("**-->Here you can describe your data<--**")
```

## Task 5: User Interaction with Widgets

Allow users to interact with widgets, such as selecting an island to filter the data:

```python
st.subheader("Let's play with the data")

# Create a dropdown menu for selecting an island
island = df['island'].unique()
user_island = st.selectbox(label="Select an Island", options=island)

# Add a checkbox to filter data based on the selected island
if st.checkbox("Do you really want to see the filtered data according to your island?"):
    st.dataframe(df[df['island'] == user_island])
st.markdown("---")
```

## Task 6: Create Scatterplots

Create scatterplots using Matplotlib, Seaborn, and Plotly:

### Matplotlib + Seaborn

```python
st.header("Showing 🐧 cases with Matplotlib, Seaborn, and Plotly")
st.subheader("🐧 Matplotlib + Seaborn")
fig, ax = plt.subplots()
ax = sns.scatterplot(
    data=df,
    x='bill_length_mm',
    y='bill_depth_mm',
    hue='species'
)
st.pyplot(fig)
```

### Plotly

```python
st.subheader("🐧 Plotly")
plotly_fig = px.scatter(
    data_frame=df,
    x='bill_length_mm',
    y='bill_depth_mm',
    color='species',
    animation_frame='sex',
)
st.plotly_chart(plotly_fig)
```

## Task 7: Create a Bar Chart

Calculate the average bill length by species and display it as a bar chart:

```python
st.subheader("🐧 Bar Chart")
bill_length_mean = df.groupby(by='species')['bill_length_mm'].mean()
st.bar_chart(bill_length_mean)
```

## Task 8: Geospatial Visualization

Visualize the penguin data on a map:

```python
st.subheader("🐧 Maps 🗺️📍")
st.map(df)
```
