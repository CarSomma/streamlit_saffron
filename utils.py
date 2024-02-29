"""A collection of utility functions for loading and processing data and models.

This module provides functions that are used across multiple Python scripts within the project. 
It includes functions for:
    - Loading data from CSV files
    - Loading pre-trained machine learning models

Usage:
    - Import this module using `import utils`.
    - Call the functions defined in this module from other Python scripts as needed.

Functions:
    - `load_data(data: str)`: 
        Loads a dataset from a CSV file and returns it as a Pandas DataFrame.

    - `load_model(model: str) -> LinearRegression`: 
        Loads a pre-trained machine learning model from a pickled file and returns it.

These functions are cached using Streamlit's `st.cache_data` decorator to improve performance by avoiding redundant computations or file loading operations. 
When a function decorated with `st.cache_data` is called, Streamlit checks if it has been called before with the same input parameters and returns the cached result if available. 
Cached results are stored persistently on disk and automatically invalidated when the code or data used in the function changes.

Note: 
    Type hints (e.g., `str`, `pd.DataFrame`, `LinearRegression`) are used in function signatures to specify the expected types of function parameters and return values. 
    This helps improve code clarity and enables static type checking tools to catch potential errors.
"""


import streamlit as st
import pandas as pd
import pickle as pk
from sklearn.linear_model import LinearRegression

    
@st.cache_data
def load_data(data: str) -> pd.DataFrame:
    """Loads a dataset from a CSV file and returns it as a Pandas DataFrame."""
    df = pd.read_csv(data)
    return df

@st.cache_data
def load_model(model: str) -> LinearRegression:
    """Loads a pre-trained linear regression model from a pickled file and returns it.

    Parameters:
    - model (str): The file path to the pickled file containing the pre-trained linear regression model.

    Returns:
    - LinearRegression: A pre-trained linear regression model loaded from the pickled file.
    """
    with open(model, mode='rb') as file:
        model = pk.load(file)
    return model

