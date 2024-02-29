"""A Streamlit app for exploring fun facts about penguins.

### Import libraries
- streamlit: For creating web applications with Python.
- pandas: For data manipulation and analysis.
- matplotlib.pyplot: For creating static plots.
- seaborn: For statistical data visualization.
- plotly.express: For creating interactive plots.
    
Additionally, it imports a custom utility function `load_data` from the `utils` module.

# Set up pages name
- Home: Links to the main page of the application.
- OracleSessionState: Links to a page demonstrating usage of Streamlit's session state.
- OracleCallBack: Links to a page demonstrating usage of Streamlit's callback feature.

# Title and Image
- Title: "Funfact about penguins🐧"
- Image: Displays the 'penguins.png' image.
- Description: Links to the palmerpenguins dataset and provides a brief description.

# Data Exploration
- Loads the 'penguins_pimped.csv' dataset using the `load_data` utility function, which is cached for improved performance.
- Displays a sample of 5 rows from the cached dataset.
- Provides a markdown section for describing the dataset.

### Usage
- Run the script to launch the Streamlit application.
- Use the sidebar to navigate between different pages.
- Explore the penguins dataset and associated fun facts.
"""

   


### Import libraries
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from utils import load_data

# Set up pages name
st.sidebar.page_link(page="app.py", label="Home", icon="🏠")
st.sidebar.page_link(page="pages/predict_sessionstate.py", label="OracleSessionState", icon="🔮")
st.sidebar.page_link(page="pages/predict_oncallback.py", label="OracleCallBack", icon="🤙🏼")

# Let's give a title
st.title("Funfact about penguins🐧")

# Let's add an image
st.image('penguins.png')
st.markdown("This is the [palmerpenguins](https://allisonhorst.github.io/palmerpenguins/) dataset that describes measurements on penguins")
st.markdown("---")
## Let's create a section about data
#df = pd.read_csv("./data/penguins_pimped.csv")
df = load_data("./data/penguins_pimped.csv")
df_sample = df.sample(5, random_state=42)

st.header("Penguins 🐧 data")
st.dataframe(df_sample)

st.markdown("**-->Here you can describe your data<--**")
