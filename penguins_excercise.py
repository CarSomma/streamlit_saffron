"""TODO
   Excercise: Explore the penguins pimped dataset :-) by following 
   the tasks. The data exploration would be the base on which we build 
   the streamlit app.

   Usage:
   After each task save the script and run the python script from the terminal.
   Be sure you are in the streamlit_env environment.
   If not activate the environment by typing in the terminal
   source streamlit_env/bin/activate

   Mode:
   Work in group.
   
"""

### Import libraries
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Let's give a title
st.title("Funfact about penguins🐧")

# Let's add an image
st.image('penguins.png')
st.markdown("This is the [palmerpenguins](https://allisonhorst.github.io/palmerpenguins/) dataset that describes measurements on penguins")
st.markdown("---")
## Let's create a section about data
df = pd.read_csv("./data/penguins_pimped.csv")
df_sample = df.sample(n=5)

st.header("Penguins 🐧 data")
st.dataframe(df_sample)
st.markdown("**-->Here you can describe your data<--**")



### Let's give a user the possibility to select island and filter dataframe
### To create a subsection
st.subheader("Let's play with the data")

island = df['island'].unique()

### Dropdown menu
user_island = st.selectbox(label="Select an Island",options=island)


### Check box
if st.checkbox("Do you really want to see the filtered data according to your island?"):
    st.dataframe(df[df['island'] == user_island])

st.markdown("---")

## Display a scatterplot: bill_length_mm vs bill_depth_mm
st.header("Showing  🐧 cases with matplotlib, seaborn and plotly")
st.subheader("🐧 Matplotlib + Seaborn")
fig, ax = plt.subplots()
ax = sns.scatterplot(
    data=df,
    x='bill_length_mm',
    y='bill_depth_mm',
    hue='species' # set to species
    )
st.pyplot(fig)

st.subheader("🐧 Plotly")
plotly_fig = px.scatter(
    data_frame=df,
    x='bill_length_mm',
    y='bill_depth_mm',
    color='species',
    animation_frame='sex',
)

st.plotly_chart(plotly_fig)


### Determine the average of the bill_length_mm by species
st.subheader("🐧 Barchart")
bill_length_mean = df.groupby(by='species')['bill_length_mm'].mean()

st.bar_chart(bill_length_mean)


### Plotting a map
st.subheader("🐧 Maps 🗺️📍")
st.map(df)