
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
b1 = datasets.load_iris()
b2 = b1.target_names
b3 = pd.DataFrame(b1.data, columns=b1.feature_names)
b3['target'] = b1.target
b8, b10, b9, b4 = train_test_split(b1.data, b1.target, test_size=0.25, random_state=0)
b5 = GaussianNB()
b5.fit(b8, b9)
b6 = b5.predict(b10)
b7 = accuracy_score(b6, b4)
print(f"Accuracy b7: {b7:.2f}")
'''
b8 = b3.drop(columns=['target'])
b9 = b3['target']
b10 = b3.drop(columns=['target'])
b4 = b3['target']
b5 = GaussianNB()
b5.fit(b8, b9)
b6 = b5.predict(b10)
b11 = np.mean(b6 == b4)
print(f"Accuracy b7: {b11:.2f}")
'''
'''
b7 = accuracy_score(b6, b4)
print(f"Accuracy b7: {b7:.2f}")
'''