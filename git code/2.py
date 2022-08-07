# dataframe using pandas
import pandas as pd
df = pd.DataFrame ({'Name' : ['Anubhav', 'Reyansh', 'Shruti', 'Sanaya'], 'Salary': [10000, 20000, 25000, 35000]})
print (df.head())

# calculate statistics
print ('Min :' +str (df['Salary'].min()))
print ('Max :' +str (df['Salary'].max()))
print ('Mean :' +str (df['Salary'].mean()))
print ('Median :' +str (df['Salary'].median()))
print ('Mod :' +str (df['Salary'].mode()))

df['Salary'].describe()
# df['Salary'].describe()['count']


# data plotting

%matplotlib inline
import matplotlib.pyplot as plt
df = pd.DataFrame ({'Name' : ['Anubhav', 'Reyansh', 'Shruti', 'Sanaya'], 'Salary': [10000, 200000, 2500, 35000]})
salary = df['Salary']
salary.plot.hist(title = 'Salary Distribution', color ='grey', bins=25)
plt.axvline(salary.mean(), color ='blue', linestyle = 'dashed', linewidth = 2)
plt.axvline(salary.median(), color ='red', linestyle = 'dashed', linewidth = 2)
plt.show()



