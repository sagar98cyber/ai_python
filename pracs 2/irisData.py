import pandas as pd
import matplotlib.pyplot as plt 

sepalLength = []
sepalWidth = []
petalLength = []
petalWidth = []
target = []

def parserFunction(var,df):
    
    print('Min :' + str (df[var].min()))
    print('Max :' + str (df[var].max()))
    print('Mean :' + str (df[var].mean()))
    print('Median :' + str (df[var].median()))
    print('Min :' + str (df[var].mode()))
    print(df[var].describe()['min'])
    salary = df[var]
    salary.plot.hist(title = f'{var} Distribution', color = 'grey')
    plt.axvline(salary.mean(), color = 'blue', linestyle = 'dashed',linewidth = 2)
    plt.axvline(salary.median(), color = 'red', linestyle = 'dashed',linewidth = 2)
    plt.show()

def splitFunction(parsedString):                #function to split the string and apppend to the list
    myList = parsedString.split(',')
    sepalLength.append(float(myList[0]))
    sepalWidth.append(float(myList[1]))
    petalLength.append(float(myList[2]))
    petalWidth.append(float(myList[3]))
    target.append(myList[4])


with open('iris_dataset.csv',buffering=200000) as f:
    for line in f:
        splitFunction(line)


df = pd.DataFrame({'Sepal Length': sepalLength})
df.head()

parserFunction('Sepal Length',df)

df = pd.DataFrame({'Sepal Width': sepalWidth})
df.head()

parserFunction('Sepal Width',df)

df = pd.DataFrame({'Petal Length': petalLength})
df.head()

parserFunction('Petal Length',df)

df = pd.DataFrame({'Petal Length': petalWidth})
df.head()

parserFunction('Petal Width',df)





