import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from xgboost import XGBClassifier
b1 = pd.read_csv('b1.dat', header=None, sep=' ', quoting=3)
b2 = pd.read_csv('b1.labels', header=None, sep=' ', quoting=3)
b3 = pd.read_csv('b3.dat', header=None, sep=' ', quoting=3)
b4 = b1.iloc[:,0:887]
b5 = b2.iloc[:,0]
b6 = b3.iloc[:,0:887]
b7 = np.mean(b4, axis=0)
b4 = b4 - b7
b8 = np.mean(b6, axis=0)
b6 = b6 - b8
b9 = PCA(n_components=28)
b10 = b9.fit_transform(b4)
b11 = b9.transform(b6)
b12 = XGBClassifier(learning_rate=0.3, n_estimators=2000, max_depth=7, min_child_weight=1, gamma=0, subsample=0.8, colsample_bytree=0.8, objective='binary:logistic', nthread=4, scale_pos_weight=1, seed=27)
b12.fit(b10, b5)
b13 = b12.predict(b11)
b14 = pd.DataFrame(data=b13)
b14.to_csv("b14.dat", b15 = False, quoting=3, header=None)