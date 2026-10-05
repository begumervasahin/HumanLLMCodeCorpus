import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from xgboost import XGBClassifier
b1 = pd.read_csv('train.dat', header=None, sep=' ', quoting=3)
b2 = pd.read_csv('train.labels', header=None, sep=' ', quoting=3)
b3 = pd.read_csv('test.dat', header=None, sep=' ', quoting=3)
b4 = b1.iloc[:, :-1]
b5 = b2.iloc[:, 0]
b6 = b3
b7 = b4 - np.mean(b4, axis=0)
b8 = b6 - np.mean(b6, axis=0)
b9 = PCA(n_components=28)
b10 = b9.fit_transform(b7)
b11 = b9.transform(b8)
b12 = XGBClassifier(
    b13 = 0.3,
    b14 = 2000,
    b15 = 7,
    b16 = 1,
    b17 = 0,
    b18 = 0.8,
    b19 = 0.8,
    b20 = 'binary:logistic',
    b21 = 4,
    b22 = 1,
    a1 = 27
)
b12.fit(b10, b5)
b23 = b12.predict(b11)
b24 = pd.DataFrame(data=b23)
b24.to_csv("output.dat", b25 = False, quoting=3, header=None)