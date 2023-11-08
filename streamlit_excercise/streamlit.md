# Streamlit Essentials
The following  is based on the official [Streamlit documentation source](https://docs.streamlit.io/library/get-started/main-concepts)


- Streamlit is a Python library for creating interactive web apps for data science and machine learning.
- You build apps by adding Streamlit commands to a Python script and running it with `streamlit run my_app.py`.

## Development Flow

- Streamlit provides an interactive development loop: Write code, save, view results, and iterate.
- Changes in your script trigger automatic updates in the app.
- For a smooth development experience, arrange your code editor and app preview side by side.

## Data Flow

- Streamlit re-runs your entire script whenever changes occur in the source code or when users interact with app widgets.
- Widgets are elements like sliders and buttons that enable user interaction.
- Use the `@st.cache_data` decorator to optimize performance by skipping costly computations.

## Display and Style Data

- Streamlit supports displaying data in various ways, including text, tables, and charts.
- You can use methods like `st.write()`, `st.dataframe()`, and `st.table()`.
- Customization options are available for styling data frames.

## Widgets

- Widgets are used to capture user input and display results.
- Examples include:
  - Slider: `x = st.slider('Select a flipper length',min_value=160,max_value=240,step=5)`
  - Button: `st.button('Press me!')`
  - Select Box: `option = st.selectbox(label="Select an Island", options=['Dream','Torgersen', 'Biscoe']`

## Layout

- You can organize widgets and content in a sidebar using `st.sidebar`.
- `st.columns()` allows widgets to be displayed side by side.
- Use `st.expander` to hide or show content and save space.

## Progress and Themes

- Show progress with `st.progress()` for long-running computations.
- Streamlit supports light and dark themes, which you can customize in the settings.

## Caching

- Streamlit provides caching decorators to store and reuse the results of expensive function calls.
- Use `@st.cache_data` for computations that return data and `@st.cache_resource` for global resources.

## Multipage Apps

- Organize large apps into multiple pages for easier management and navigation.
- Create separate Python script files for each page and place them in a "pages" folder.
- Each script corresponds to a different page in the app.

## App Model

- Streamlit apps are Python scripts that execute from top to bottom.
- User interactions and changes trigger script reruns.
- Caching is used to optimize performance and speed up app responses.


