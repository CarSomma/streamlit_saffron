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
with open("...", "rb") as file:
    model = pickle...

# Task2:
# Set the value of flipper_length to a number between 160 and 240
flipper_lenght = ...

# Set the value of species to one of the possible options 'Adelie','Chinstrap','Gentoo'
species = ...

# Set the value of sex to 'Female' or 'Male'
sex = ...

# Task3:
# Let's create a dictionary having as keys the input features 
# (see initial doc string at the top) 
# and corresponding values the one we have set just above
input_dict_X = {
    ...
}
print(input_dict_X)

# Task4:
# create a dataframe from the input_dict_X 
input_X = ...

# Task5:
# make prediction with the model
y_pred = ...

print(y_pred)