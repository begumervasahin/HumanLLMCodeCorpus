
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
b1 = datasets.load_iris()
b2 = pd.DataFrame(b1.data, columns=b1.feature_names)
b2['target'] = b1.target
X_train, X_test, y_train, b3 = train_test_split(b1.data, b1.target, test_size=0.25, random_state=0)
b4 = GaussianNB()
b4.fit(X_train, y_train)
b5 = b4.predict(X_test)
b6 = accuracy_score(b5, b3)
print("Accuracy Score:", b6)