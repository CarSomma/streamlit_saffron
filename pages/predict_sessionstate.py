"""A Streamlit page for predicting penguin weights and showcasing the usage of session state.

This Streamlit page demonstrates how to predict the weight of penguins and showcases the usage of Streamlit's session state feature.

### Import libraries
- streamlit: For creating web applications with Python.
- pandas: For data manipulation and analysis.
- utils.load_model: A custom utility function for loading machine learning models.

# Set up pages name
- Home: Links to the main page of the application.
- OracleSessionState: Links to a page demonstrating usage of Streamlit's session state.
- OracleCallBack: Links to a page demonstrating usage of Streamlit's callback feature.

# Title and Description
- Title: "How 'heavy' are penguins 🐧?"
- Description: "We want to showcase the usage of session state."

# Streamlit Sessions and Session State
- Streamlit Sessions: When a user interacts with a Streamlit app, it creates a session. A session represents a single instance of interaction with the app, from the moment the user opens the app until they close it.
- Session State: Streamlit's session state allows you to store and manage session-specific data, such as user interactions and application state. This enables apps to remember user preferences, maintain state between interactions, and provide a personalized experience.

# Initialize session state for prediction count
- Prediction Count: Initializes a session state variable 'prediction_count' if it does not already exist. This variable tracks the total number of predictions made during the session.

# Interaction Widgets
- Slider: Allows users to select a flipper length between 160 and 240.
- Selectbox: Allows users to choose a penguin species and sex.


### Usage
- Run the script to launch the Streamlit application.
- Interact with the sidebar widgets to select penguin parameters.
- Click the "Update Prediction" button to display a prediction message and increment the prediction count.
- View the total predictions made during the session.
"""

import streamlit as st
import pandas as pd
from utils import load_model

# load the model
model = load_model("pages/model_penguins.pkl")


# Set up pages name
st.sidebar.page_link(page="app.py", label="Home", icon="🏠")
st.sidebar.page_link(page="pages/predict_sessionstate.py", label="OracleSessionState", icon="🔮")
st.sidebar.page_link(page="pages/predict_oncallback.py", label="OracleCallBack", icon="🤙🏼")
st.sidebar.markdown("---")

st.title("How 'heavy' are penguins  🐧?")
st.markdown('''We want to showcase the usage of session state''')

# Initialize session state for prediction count
# session state is like a python dictionary
if 'prediction_count' not in st.session_state:
    st.session_state.prediction_count = 0


st.markdown(f"Session State before interacting with button `Update prediction` \n {st.session_state}")


# Set the value of flipper_length to a number between 160 and 240
flipper_lenght = st.sidebar.slider('Select a flipper length',min_value=160,max_value=240,step=5)

# Set the value of species to one of the possible options 'Adelie','Chinstrap','Gentoo'
species = st.sidebar.selectbox("Chose a species", options=['Adelie','Chinstrap','Gentoo'])

# Set the value of sex to 'Female' or 'Male'
sex = st.sidebar.selectbox("Chose a sex", options=['Female','Male'])


# Add a button to update prediction
if st.button("Update Prediction"):
    
    # Display final prediction
    text = '```Hello from Penguins```'
    st.markdown(text)

    st.session_state.prediction_count += 1

st.write(f"Total predictions made during this session: {st.session_state.prediction_count}")

