import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline

train = pd.read_csv("train.csv")

train.head()

train.count()

train[train["Name"].str.contains("Dawson")]

train[train["Name"].str.contains("Brown")]

sns.countplot(x='Survived', hue='Pclass', data=train)

# Data Wrangling 
def add_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    if pd.isnull(Age):
        return int(train[train["Pclass"] == Pclass]["Age"].mean())
    else:
        return Age

train["Age"] = train[["Age", "Pclass"]].apply(add_age,axis=1)
train.drop("Cabin",inplace=True,axis=1)
train.dropna(inplace=True)

embarked = pd.get_dummies(train["Embarked"],drop_first=True)
embarked = pd.get_dummies(train["Pclass"],drop_first=True)
train.drop(["PassengerId","Pclass","Name","Sex","Ticket","Embarked"],axis=1,inplace=True)

X = train.drop("Survived",axis=1)
y = train["Survived"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)

from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)

predictions = logmodel.predict(X_test)
from sklearn.metrics import classification_report
print(classification_report(y_test, predictions))

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, predictions)

#True positive: 154 (We predicted a positive result and it was positive)
#True negative: 77 (We predicted a negative result and it was negative)
#False positive: 9 (We predicted a positive result and it was negative)
#False negative: 27 (We predicted a negative result and it was positive)