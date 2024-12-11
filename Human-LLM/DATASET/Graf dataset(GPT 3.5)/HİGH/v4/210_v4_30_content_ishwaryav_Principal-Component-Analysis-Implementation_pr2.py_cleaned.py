
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from xgboost import XGBClassifier
b1 = pd.read_csv('train.dat', header=None, sep=' ', quoting=3)
b2 = pd.read_csv('train.b2', header=None, sep=' ', quoting=3)
b3 = pd.read_csv('test.dat', header=None, sep=' ', quoting=3)
b4 = b1.iloc[:, 0:887]
b5 = b2.iloc[:, 0]
b6 = b3.iloc[:, 0:887]
b7 = np.mean(b4, axis=0)
b4 -= b7
b8 = np.mean(b6, axis=0)
b6 -= b8
b9 = PCA(n_components=28)
b4 = b9.fit_transform(b4)
b6 = b9.transform(b6)
b10 = XGBClassifier(learning_rate=0.3, n_estimators=2000, max_depth=7,
                    b11 = 1, gamma=0, subsample=0.8, colsample_bytree=0.8,
                    b12 = 'binary:logistic', nthread=4, scale_pos_weight=1, seed=27)
b10.fit(b4, b5)
b13 = b10.predict(b6)
b14 = pd.DataFrame(data=b13)
b14.to_csv("b14.dat", b15 = False, quoting=3, header=None)