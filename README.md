# Learning Streamlit with Penguins 🐧 
In the Pythonic realm 🐍👑  of data and machine learning web application frameworks Streamlit has been acquiring quite a lot of popularity. In fact, Streamlit is designed  to be incredibly user-friendly. You can create interactive web apps with just a few lines of Python code. It abstracts away much of the complexity involved in web development, making it accessible even to those without a web development background. 

This repo will guide us step-by-step on building a 📊🧑🏽‍🔬DataScience Web Application 🧑🏽‍🔬📊 based on Streamlit. 

__🗿 Milestones 🪜 🎯👷🏽‍♀️__:
1. [Setting up a python environment 🐍](README.md#environment-🌀-and-installation-👩🏽‍🔧👨🏽‍🔧)
2. [🔥🔥 2 Warm-Up Exercises 🔥🔥 on EDA 📊🌈 and  Deploy a Machine-Learning Model 🎓🤖](warmup_exercises/README.md)
3. [⚡️📚 Quick Reading on Streamlit ⚡️📚](streamlit_excercise/streamlit.md)
4. [Building a 🐧 Web-App with Streamlit: PART I](streamlit_exercise/penguins_st_tutorial.md)
5. [Building a 🐧 Web-App with Streamlit: PART II](streamlit_exercise/penguins_st_tutorial.md)

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

__🎉Congratulations🎉__. 
