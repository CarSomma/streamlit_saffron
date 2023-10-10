"""Here we make predictions with the linear regression trained model (model_penguins.pkl). 
The model predicts the body_mass_g given the input features flipper_length_mm, species and sex
"""
import pickle
import streamlit as st
import pandas as pd

# load the model
with open("...", "rb") as file:
    model = pickle...


# Set the value of flipper_length to a number between 160 and 240
flipper_lenght = ...

# Set the value of species to one of the possible options 'Adelie','Chinstrap','Gentoo'
species = ...

# Set the value of sex to 'Female' or 'Male'
sex = ...

# Let's create a dictionary having as keys the input features (see initial doc string at the top) 
# and corresponding values the one we have set just above
input_dict_X = {
    ...
}

# create a dataframe from the input_dict_X 
input_X = ...

# make prediction with the model
y_pred = ...

print(y_pred)