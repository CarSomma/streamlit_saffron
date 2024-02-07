"""TODO 
    Exercise: Make predictions with the linear regression trained model (model_penguins.pkl). 
               The model predicts the body_mass_g 
               given the input features 
               flipper_length_mm, species and sex
    Usage:
               After each task save the script and run the python script from the terminal.
               Be sure you are in the .streamlit_env environment.
               If not activate the environment by typing in the terminal
               source .streamlit_env/bin/activate (Mac/Linux)
               .streamlit_env\Scripts\Activate.ps1 (Windows)

    Mode:
    Work in group.
"""
import pickle
import streamlit as st
import pandas as pd

# load the model
with open("pages/model_penguins.pkl", "rb") as file:
    model = pickle.load(file)

# Set up pages name
st.sidebar.page_link(page="app.py", label="Home", icon="🏠")
st.sidebar.page_link(page="pages/predict.py", label="Oracle", icon="🔮")
st.sidebar.markdown("---")

st.title("How 'heavy' are penguins  🐧?")
st.markdown('---')
st.markdown('''Imagine using your linear regression model is like consulting a penguin fortune-teller named ```Penguinstradamus```. 
         You give it flipper length, species, and sex data, and it predicts penguin body mass.
```Penguinstradamus```, with great flair, predicts a number for you. 
         Keep in mind that the accuracy depends on data quality and penguin whims. 
         So, trust your model, but remember, penguins can be unpredictable!''')

st.markdown('This is the ```Penguinstradamus``` tool:')
st.text(f"{model}")

st.markdown('---')

# Set the value of flipper_length to a number between 160 and 240
flipper_lenght = st.sidebar.slider('Select a flipper length',min_value=160,max_value=240,step=5)

# Set the value of species to one of the possible options 'Adelie','Chinstrap','Gentoo'
species = st.sidebar.selectbox("Chose a species", options=['Adelie','Chinstrap','Gentoo'])

# Set the value of sex to 'Female' or 'Male'
sex = st.sidebar.selectbox("Chose a sex", options=['Female','Male'])

# Let's create a dictionary having as keys the input features (see initial doc string at the top) 
# and corresponding values the one we have set just above

input_dict_X = {
    'flipper_length_mm':flipper_lenght,
    'species':species,
    'sex': sex
}

# create a dataframe from the input_dict_X 
input_X = pd.DataFrame(data=input_dict_X, index=[0])

# make prediction with the model
y_pred = model.predict(input_X)


# Display final prediction
text = '```Penguinstradamus says```:\n'

st.markdown(f"""{text}
```{round(y_pred[0],0)} g```""")