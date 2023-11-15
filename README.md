# Learning Streamlit with Penguins 🐧 
In the Pythonic realm 🐍👑  of data and machine learning web application frameworks Streamlit has been acquiring quite a lot of popularity. In fact, Streamlit is designed  to be incredibly user-friendly. You can create interactive web apps with just a few lines of Python code. It abstracts away much of the complexity involved in web development, making it accessible even to those without a web development background. 

This repo will guide us step-by-step on building a 📊🧑🏽‍🔬DataScience Web Application 🧑🏽‍🔬📊 based on Streamlit. 

__🗿 Milestones 🪜 🎯👷🏽‍♀️__:
1. [Setting up a python environment 🐍](README.md#environment-🌀-and-installation-👩🏽‍🔧👨🏽‍🔧)
2. [🔥🔥 2 Warm-Up Exercises 🔥🔥 on EDA 📊🌈 and  Deploy a Machine-Learning Model 🎓🤖](warmup_exercises/README.md)
3. [⚡️📚 Quick Reading on Streamlit ⚡️📚](streamlit_exercise/streamlit.md)
4. [Building a 🐧 Web-App with Streamlit: PART I](streamlit_exercise/EDA_st_tutorial.md)
5. [Building a 🐧 Web-App with Streamlit: PART II](streamlit_exercise/predict_st_tutorial.md)

## Environment 🌀 and Installation 👩🏽‍🔧👨🏽‍🔧
### Prerequisite
+ Python 3.11.6 (We will use [pyenv](https://github.com/pyenv/pyenv#simple-python-version-management-pyenv) for Python Version Management but feel free to use any other tool)
+ Virtual environment (We will use the module venv from python but you can use any other tool)


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

## Further Readings
The following is a list of other popular python web framework:
+ [Flask](https://flask.palletsprojects.com/en/3.0.x/)
+ [Django](https://www.djangoproject.com)
+ [Dash](https://dash.plotly.com)
+ [FastAPI](https://fastapi.tiangolo.com)

## Aknowledgment 🙏🏼
I would like to thank [Dr. Paula González Avalos](https://github.com/pga99?tab=repositories) for introduce me into the Penguins and Streamlit worlds. 



