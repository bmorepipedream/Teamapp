import pandas as pd
import statsmodels.formula.api as smf
import pickle

# Import each Dataset as a DF.
df = pd.read_csv('stem_final_2.csv')

# Multivariate Linear Regression formula
f1 = 'income ~ yearsofexperience + yearsatcompany + title + level + education +  gender + state + race + hispanic'
# fitted model
model = smf.ols(formula=f1, data=df)
# fit Model
fitted = model.fit()

with open('model.pkl','wb') as f:
  pickle.dump(fitted,f)