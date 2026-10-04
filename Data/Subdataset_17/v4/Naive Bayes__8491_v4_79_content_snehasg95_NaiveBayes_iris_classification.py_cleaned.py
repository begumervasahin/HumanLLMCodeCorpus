
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
iris = datasets.load_iris()
class_names = iris.target_names
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.25, random_state=0)
clf = GaussianNB()
clf.fit(X_train, y_train)
y_predict = clf.predict(X_test)
score = accuracy_score(y_predict, y_test)
print(f"Accuracy score: {score:.2f}")
'''
X_train = iris_df.drop(columns=['target'])
y_train = iris_df['target']
X_test = iris_df.drop(columns=['target'])
y_test = iris_df['target']
clf = GaussianNB()
clf.fit(X_train, y_train)
y_predict = clf.predict(X_test)
acc_score = np.mean(y_predict == y_test)
print(f"Accuracy score: {acc_score:.2f}")
'''
'''
score = accuracy_score(y_predict, y_test)
print(f"Accuracy score: {score:.2f}")
'''