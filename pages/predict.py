"""TODO 
    Excercise: Make predictions with the linear regression trained model (model_penguins.pkl). 
               The model predicts the body_mass_g 
               given the input features 
               flipper_length_mm, species and sex
    Usage:
               After each task save the script and run the python script from the terminal.
               Be sure you are in the streamlit_env environment.
               If not activate the environment by typing in the terminal
               source streamlit_env/bin/activate (Mac/Linux)
               .\streamlit_env\Scripts\activate.ps1 (Windows)

    Mode:
               Work in group.
"""
import pickle
import streamlit as st
import pandas as pd

# Task1:
# load the model
with open("/pages/model_penguins.pkl", "rb") as file:
    model = pickle.load(file)
print(model)

# Task2:
# Set the value of flipper_length to a number between 160 and 240
flipper_lenght = 170

# Set the value of species to one of the possible options 'Adelie','Chinstrap','Gentoo'
species = 'Gentoo'

# Set the value of sex to 'Female' or 'Male'
sex = 'Female'

# Task3:
# Let's create a dictionary having as keys the input features 
# (see initial doc string at the top) 
# and corresponding values the one we have set just above
input_dict_X = {
    'flipper_length_mm':flipper_lenght,
    'species':species,
    'sex':sex 
}
print(input_dict_X)

# Task4:
# create a dataframe from the input_dict_X 
input_X = pd.DataFrame(data=input_dict_X, index=[0])

# Task5:
# make prediction with the model
y_pred = model.predict(input_X)

print(y_pred)