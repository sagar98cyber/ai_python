# dataframe using pandas
import pandas as pd


# data plotting
#Program number 8
#%matplotlib inline
import matplotlib.pyplot as plt
df = pd.DataFrame ({'Name' : ['Anubhav', 'Reyansh', 'Shruti', 'Sanaya'], 'Salary': [10000, 200000, 2500, 35000]})
salary = df['Salary']
salary.plot.hist(title = 'Salary Distribution', color ='grey', bins=25)
plt.axvline(salary.mean(), color ='blue', linestyle = 'dashed', linewidth = 2)
plt.axvline(salary.median(), color ='red', linestyle = 'dashed', linewidth = 2)
plt.show()



