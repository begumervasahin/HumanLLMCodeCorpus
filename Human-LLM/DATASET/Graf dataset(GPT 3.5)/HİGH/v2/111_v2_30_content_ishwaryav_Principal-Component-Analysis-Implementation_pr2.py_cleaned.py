import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from xgboost import XGBClassifier
b1 = pd.read_csv('train.dat', header=None, sep=' ', quoting=3)
b2 = pd.read_csv('train.labels', header=None, sep=' ', quoting=3)
b3 = pd.read_csv('test.dat', header=None, sep=' ', quoting=3)
b4 = b1.iloc[:, 0:887]
b5 = b2.iloc[:, 0]
b6 = b3.iloc[:, 0:887]
b7 = np.mean(b4, axis=0)
b8 = b4 - b7
b9 = np.mean(b6, axis=0)
b10 = b6 - b9
b11 = PCA(n_components=28)
b12 = b11.fit_transform(b8)
b13 = b11.transform(b10)
b14 = XGBClassifier(
    b15 = 0.3,
    b16 = 2000,
    b17 = 7,
    b18 = 1,
    b19 = 0,
    b20 = 0.8,
    b21 = 0.8,
    b22 = 'binary:logistic',
    b23 = 4,
    b24 = 1,
    a1 = 27
)
b14.fit(b12, b5)
b25 = b14.predict(b13)
b26 = pd.DataFrame(data=b25)
b26.to_csv("output.dat", b27 = False, quoting=3, header=None)