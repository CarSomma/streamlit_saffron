# 🐧 Streamlit Web-App 
This repo will guide us on building a 📊🧑🏽‍🔬DataScience Web Application 🧑🏽‍🔬📊 based on [Streamlit](streamlit.md) is a free and open-source framework to rapidly build and share beautiful machine learning and data science web apps.
It is a Python-based library specifically designed for data science teams. 
Background in Front-end and Back-end development is not required.
For more information, [visit](https://docs.streamlit.io).

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
