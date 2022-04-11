from turtle import color, title
import pandas as pd
import matplotlib.pyplot as plt 
df = pd.DataFrame({'Name':['Anubhav','Sagar','What','L'], 'Salary': [10000,2000,2500,20000]})
df.head()

print('Min :' + str (df['Salary'].min()))
print('Max :' + str (df['Salary'].max()))
print('Mean :' + str (df['Salary'].mean()))
print('Median :' + str (df['Salary'].median()))
print('Min :' + str (df['Salary'].mode()))

print(df['Salary'].describe()['min'])

salary = df['Salary']
salary.plot.hist(title = 'Salary Distribution', color = 'grey', bins =25)
plt.axvline(salary.mean(), color = 'blue', linestyle = 'dashed',linewidth = 2)
plt.axvline(salary.median(), color = 'red', linestyle = 'dashed',linewidth = 2)
plt.show()