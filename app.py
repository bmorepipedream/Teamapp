import pandas as pd
import streamlit as st
import statsmodels.formula.api as smf




"""
# Welcome to Streamlit!
Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
In the meantime, below is an example of what you can do with just a few lines of code:
"""
# Import each Dataset as a DF.
df = pd.read_csv('stem_final_2.csv')
# Multivariate Linear Regression formula
f1 = 'income ~ yearsofexperience + yearsatcompany + title + level + education +  gender + state + race + hispanic'
# fitted model
model = smf.ols(formula=f1, data=df)
# fit Model
fitted = model.fit()




with st.form("my_form"):
   st.write("Inside the form")
   #slider_val = st.slider("Form slider")
   #slider2_val = st.slider("Form slider2")
   #checkbox_val = st.checkbox("Form checkbox")
   #text_val= st.text_input(
   #   "Placeholder for the other text input widget",
    #  "This is a placeholder",
   #   key="placeholder",
   #)
   #RACE
   race = st.selectbox(
      'Race',
      ('Black', 'Asian', 'White', 'Two or More'))
   #st.write('You selected:', race)
   #HISPANICE
   hispanic = st.selectbox(
      'Hispanic',
      ('Yes', 'No'))
   #st.write('You selected:', hispanic)
   #GENDER
   gender= st.selectbox(
      'Gender',
      ('Email', 'Home phone', 'Mobile phone'))
   #st.write('You selected:', gender)
   #EDUCATION
   education = st.selectbox(
      'Education',
      ('Email', 'Home phone', 'Mobile phone'))
   #st.write('You selected:', education)

   state = st.selectbox(
      'State',
      ('AL', 'AK', 'AZ', 'AR', 'CA', 'CZ', 'CO', 'CT', 'DE', 'DC','FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY','LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE','NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR','PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VI','VA', 'WA', 'WV', 'WI', 'WY'))
   #st.write('You selected:', state)

   age_val= st.number_input(
      "Age", min_value= 18,
      #"Age",
      key="age",)

   expericence_val = st.number_input(
      "Years of experience", min_value= 0,
      #"Years of xpericence",
      key="experience",)

   years_val = st.number_input(
      "Years at company", min_value= 0,
      #"This is a placeholder",
      key="years",)

   job_title = st.selectbox(
      'Job Title',
      ('Software Engineer', 'Product Manager', 'Data Scientist', 'Hardware Engineer',
      'Product Designer'))
   #st.write('You selected:', job_title)

   level = st.selectbox(
      'Level',
      ('Intern', 'Entry Level', 'Intermediate Level', 'Senior Level', ' Manager', 'Senior Manager'))
   #st.write('You selected:', level)

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")

   if submitted:
       st.write('race', race, 'hispanic', hispanic,'gender',gender, 'education', education, 'state', state , 'age', age_val )

st.write("Outside the form")

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)


