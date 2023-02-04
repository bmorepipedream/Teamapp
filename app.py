import pandas as pd
import streamlit as st



"""
# Welcome to Streamlit!
Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
In the meantime, below is an example of what you can do with just a few lines of code:
"""

with st.form("my_form"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   slider2_val = st.slider("Form slider2")
   checkbox_val = st.checkbox("Form checkbox")
   text_val= st.text_input(
      "Placeholder for the other text input widget",
      "This is a placeholder",
      key="placeholder",
   )
   ethnicity = st.selectbox(
      'How would you like to be contacted?',
      ('Email', 'Home phone', 'Mobile phone'))

   st.write('You selected:', option)

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")

   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val, 'text', text_val)

st.write("Outside the form")

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)


