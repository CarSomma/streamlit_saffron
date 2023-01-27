# Hi Binomials happy to be here today
## Installing streamlit in a conda env

In your terminal type:

```bash
conda create --name streamlit_env 
```

To use streamlit_env:

```bash
conda activate streamlit_env
```

To install streamlit:

```bash
conda install -c conda-forge streamlit
```

To install further library:

```bash
conda install -c conda-forge --file requirements.txt
```

To check that everything works properly:

```bash
streamlit hello
```
(it should pop up a streamlit web app in your browser)