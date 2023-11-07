# Hi Saffron happy to be here today with Streamlit
Streamlit is a free and open-source framework to rapidly build and share beautiful machine learning and data science web apps.
It is a Python-based library specifically designed for data science teams. 
Background in Front end and Back end development is not required.
For more information, [visit](https://docs.streamlit.io).
1. **Create a Virtual Environment:**
You can use venv

```bash
python -m venv streamlit_env
```
This command creates a virtual environment named streamlit_env.

2. **Activate the Virtual Environment**:
On Windows:

```bash
.\streamlit_env\Scripts\activate.ps1
```
On macOS and Linux:

```bash
source streamlit_env/bin/activate
```

3. **Install Streamlit and Additional Libraries:**
Inside the activated virtual environment, you can use pip to install Streamlit and any other libraries:

```bash
pip install -r requirements.txt
```

4. **Test Streamlit Installation:**
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
