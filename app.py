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
   st.write("Provide Responses Below")
   #RACE
   race = st.selectbox(
      'Race', ('Black', 'Asian', 'White', 'Two or More'))
   #HISPANICE
   hispanic = st.selectbox(
      'Hispanic', ('Yes', 'No'))
   #GENDER
   gender= st.selectbox(
      'Gender', ('Male', 'Female', 'Other'))
   #EDUCATION
   education = st.selectbox(
      'Education', ('High School Diploma', 'Some College', 'Bachelors', 'Graduate'))
   state = st.selectbox(
      'State',
      ('AL', 'AK', 'AZ', 'AR', 'CA', 'CZ', 'CO', 'CT', 'DE', 'DC','FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY','LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE','NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR','PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VI','VA', 'WA', 'WV', 'WI', 'WY'))
   age_val= st.number_input(
      "Age", min_value= 18,
      key="age",)
   expericence_val = st.number_input(
      "Years of experience", min_value=0,
      key="experience",)
   years_val = st.number_input(
      "Years at company", min_value=0,
      key="years",)
   job_title = st.selectbox(
      'Job Title',
      ('Software Engineer', 'Product Manager', 'Data Scientist', 'Hardware Engineer', 'Product Designer'))
   level = st.selectbox(
      'Level',
      ('Intern', 'Entry Level', 'Intermediate Level', 'Senior Level', ' Manager', 'Senior Manager'))
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")

   if submitted:
      #st.write('race', race, 'hispanic', hispanic,'gender',gender, 'education', education, 'state', state , 'age', age_val )
      demo = {'yearsofexperience': [years_val], 'yearsatcompany': [expericence_val], 'title': [job_title], 'level': [level],
           'education': [education], 'race': [race], 'hispanic': [hispanic], 'gender': [gender], 'state': [state]}

pred = fitted.predict(demo)
st.write('The predicted salary based on the demographic information you entered below is', pred[0])


title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)


