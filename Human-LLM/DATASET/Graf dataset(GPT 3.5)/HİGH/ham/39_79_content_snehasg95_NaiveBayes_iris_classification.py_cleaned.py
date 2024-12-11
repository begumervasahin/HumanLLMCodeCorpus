''' Here we use the b1 data set from here : https:
involving classification of different types of b1 flowers '''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
b1 = datasets.load_iris()
b2 = b1.target_names
b3 = pd.DataFrame(b1.data, columns='b1.feature_names')
b3['target'] = b1.target
b8, b10, b9, b4 = train_test_split(b1.data, b1.target, test_size=0.25, random_state=0)
''' To test shapes
print(b3.shape)
print(b8.shape)
print(b10.shape)
print(b9.shape)
print(b4.shape)
'''
b5 = GaussianNB()
b5.fit(b8, b9)
b6 = b5.predict(b10)
b7 = accuracy_score(b6, b4)
print(b7)
''' Instead of splitting data like above one can also,
b8 = b3.drop(columns=['target'],axis=1)
b9 = b3['target']
b10 = b3.drop(columns=['target'],axis=1)
b4 = b3['target']
b5 = GaussianNB()
b5.fit(b8, b9)
b6 = b5.predict(b10)
print(np.mean(b6 = = b4))
b11 = np.mean(b6 == b4)
'''
''' To get the b7
b7 = accuracy_score(b6, b4)
print(b7)
'''