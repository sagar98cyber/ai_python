from cProfile import label
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('pracs 6\headbrain.csv')

X = df['Head Size(cm^3)'].values
Y = df['Brain Weight(grams)'].values
print(df.shape)
df.head()

np.corrcoef(X,Y)
plt.scatter(X,Y,c= 'Green',label = 'Data points')
plt.xlabel('Head Size in cm3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()

