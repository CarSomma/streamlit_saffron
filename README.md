# Learning Streamlit with Penguins 🐧 
In the Pythonic 🐍 realm of data and machine learning web application frameworks Streamlit has been acquiring quite a lot of popularity. In fact, Streamlit is designed to be incredibly user-friendly. You can create interactive web apps with just a few lines of Python code. It abstracts away much of the complexity involved in web development, making it accessible even to those without a strong web development background. 

This repo will guide you on building a 📊🧑🏽‍🔬DataScience Web Application 🧑🏽‍🔬📊 based on [Streamlit](streamlit.md).

## Environment 🌀 and Installation 👩🏽‍🔧👨🏽‍🔧
For __MacOs__/__Linux__ users
```bash
# Sets the local Python version to 3.11.6 using pyenv
pyenv local 3.11.6 
# Create a Virtual Environment named .streamlit_env using venv
python -m venv .streamlit_env
# Activate the Virtual Environment
source .streamlit_env/bin/activate
# Install Streamlit and Additional Libraries
pip install -r requirements.txt
```

For __Windows__ users


```bash
# Sets the local Python version to 3.11.6 using pyenv
pyenv local 3.11.6 
# Create a Virtual Environment named .streamlit_env using venv
python -m venv .streamlit_env
# Activate the Virtual Environment
.streamlit_env\Scripts\Activate.ps1
# Install Streamlit and Additional Libraries
pip install -r requirements.txt
```



### 🧪 Test Streamlit Installation 👨🏽‍🔧👩🏽‍🔧
You can check if Streamlit is installed correctly and run a sample app with the following command:
```bash
streamlit hello
```
This should open a Streamlit web app in your default web browser.


## Data analysis excercise on penguins
**Business goal:**

*Our marketing team would love to know about the penguins 🐧*

Use an editor (e.g., Vscode) to open the file penguins_excercise.py. Read the TODO doc string at the beginning of the file. 

Afterward we will create out of that a nice [report](penguins_st_tutorial.md) using Streamlit.

## Model prediction on penguins
**Business goal:**

*Our scientific team would love to know how 'heavy' penguins 🐧 are given some input features*

Use an editor (e.g., Vscode) to open the file predict.py under the folder pages. Read the TODO doc string at the beginning of the file. 

Afterward we will implement predictions given user inputs in the Streamlit app.
