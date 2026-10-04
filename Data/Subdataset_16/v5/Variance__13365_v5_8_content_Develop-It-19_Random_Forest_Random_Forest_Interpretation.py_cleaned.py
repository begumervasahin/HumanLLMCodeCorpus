import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import scipy.cluster.hierarchy as hc
from sklearn.ensemble import RandomForestRegressor
from pdpbox import pdp
from plotnine import *
from treeinterpreter import treeinterpreter as ti
def fonk1(b1):
    pass
def fonk2(df, n):
    return df.sample(n)
def fonk3(df, n):
    return df[:n], df[n:]
def fonk4(X_train, y_train):
    a1 = 50000
    b1 = RandomForestRegressor(n_estimators=40, min_samples_leaf=3, max_features=0.5, n_jobs=-1, b9=True)
    b1.fit(X_train, y_train)
    return b1
b1 = fonk4(X_train, y_train)
fonk1(b1)
a2 = 0.005
b2 = fi[fi.imp > a2].cols
print(f"Number of features to keep: {len(b2)}")
def fonk5(df):
    b3 = np.round(scipy.stats.spearmanr(df).correlation, 4)
    b4 = hc.distance.squareform(1 - b3)
    b5 = hc.linkage(b4, method="average")
    plt.figure(b6 = (16, 10))
    hc.dendrogram(b5, b7 = df.columns, orientation="left", leaf_font_size=16)
    plt.show()
fonk5(df_keep)
def fonk6(df, n_trn, y_train):
    b1 = RandomForestRegressor(n_estimators=40, min_samples_leaf=3, max_features=0.5, n_jobs=-1, b9=True)
    x_train, b8 = fonk3(df, n_trn)
    b1.fit(x_train, y_train)
    return b1.b9
b9 = fonk6(df_keep, n_trn, y_train)
print(f"OOB Score: {b9}")
b10 = ['saleYear', 'fiBaseModel', 'Grouser_Tracks']
b11 = df_keep.drop(columns=b10)
b12 = fonk6(b11, n_trn, y_train)
print(f"OOB Score after dropping columns: {b12}")
def fonk7(df):
    b13 = fonk2(df[df.YearMade > 1930], 500)
    b14 = (ggplot(b13, aes("YearMade", "SalePrice"))
            + stat_smooth(b15 = True, method="loess"))
    print(b14)
fonk7(df_raw)
def fonk8(b1, feature, data, b16 = None, b17=None):
    b17 = b17 or feature
    b18 = pdp.pdp_isolate(b1, data, feature)
    pdp.pdp_plot(b18, b17, b19 = True, cluster=b16 is not None, n_cluster_centers=b16)
b20 = fonk2(X_train[X_train.YearMade > 1930], 500)
fonk8(b1, "YearMade", b20)
fonk8(b1, "YearMade", b20, b16 = 5)
df_train, b21 = fonk3(df_raw[df_keep.columns], n_trn)
b22 = X_valid.values[None, 0]
prediction, bias, b23 = ti.predict(b1, b22)
print(f"Prediction: {prediction[0]}, Bias: {bias[0]}")
def fonk9(df_keep, b21, b23):
    b24 = np.argsort(b23[0])
    b25 = [(df_keep.columns[idx], b21.iloc[0][idx], b23[0][idx]) for idx in b24]
    for info in b25:
        print(info)
fonk9(df_keep, b21, b23)