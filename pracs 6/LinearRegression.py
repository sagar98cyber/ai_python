import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%matplotlib inline
train = pd.read_csv("train.csv")
train.head()

train.count()