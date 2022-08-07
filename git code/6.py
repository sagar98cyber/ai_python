#finding r square from scikit learn
# Import Libary
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# read data
df=pd.read_csv('E:\MD\headbrain.csv')
X = df['Head Size(cm^3)'].values
Y = df['Brain Weight(grams)'].values
m = len(X)
X=X.reshape(m,1)
reg=LinearRegression()
reg=reg.fit(X,Y)

Y_pred = reg.predict(X)
r2_score= reg.score(X,Y)
print(r2_score)
