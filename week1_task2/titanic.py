import pandas as p
import numpy as np
from sklearn.tree import DecisionTreeClassifier

data = p.read_csv('titanic.csv', index_col='PassengerId')

dataToClassify = data[['Pclass', 'Fare', 'Age', 'Sex', 'Survived']]
dataToClassify['Sex'] = np.where(dataToClassify['Sex'] == 'male', 0, 1)
print dataToClassify
dataToClassify = dataToClassify.dropna(axis=0)

print dataToClassify
x = dataToClassify[['Pclass', 'Fare', 'Age', 'Sex']]
y = dataToClassify[['Survived']]
clf = DecisionTreeClassifier(random_state=241)
clf.fit(x, y)

importance = clf.feature_importances_
print importance
