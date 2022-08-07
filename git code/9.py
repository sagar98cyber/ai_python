import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn import tree
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

#%matplotlib inline


data = pd.read_csv('E:\MD\Iris.csv')
data


data.shape
col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
data.columns = col_names


data.info()



data['species'].value_counts()


target_col = ['species']



X = data.drop(['species'], axis=1)
y = data['species']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)


clf_gini = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=0)



clf_gini.fit(X_train, y_train)



y_pred_gini = clf_gini.predict(X_test)
y_pred_gini

from sklearn.metrics import accuracy_score
print('Model accuracy score with criterion gini index: {0:0.4f}'. format(accuracy_score(y_test, y_pred_gini)))
# y_pred_gini are the predicted class labels in the test-set.


print('Training set score: {:.4f}'.format(clf_gini.score(X_train, y_train)))
print('Test set score: {:.4f}'.format(clf_gini.score(X_test, y_test)))




plt.figure(figsize=(12,8))
tree.plot_tree(clf_gini.fit(X_train, y_train))



