import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import scipy.cluster.hierarchy as hc
from sklearn.ensemble import RandomForestRegressor
from pdpbox import pdp
from plotnine import *
from treeinterpreter import treeinterpreter as ti
a1 = 50000
b1 = RandomForestRegressor(n_estimators=40, min_samples_leaf=3, max_features=0.5, n_jobs=-1, b9=True)
b1.fit(X_train, y_train)
print_score(b1)
b2 = fi[fi.imp > 0.005].cols
print(f"Number of features to keep: {len(b2)}")
b3 = np.round(scipy.stats.spearmanr(df_keep).correlation, 4)
b4 = hc.distance.squareform(1 - b3)
b5 = hc.linkage(b4, method="average")
b6 = plt.figure(figsize=(16, 10))
b7 = hc.b7(b5, labels=df_keep.columns, orientation="left", leaf_font_size=16)
plt.show()
def fonk1(df):
    b1 = RandomForestRegressor(n_estimators=40, min_samples_leaf=3, max_features=0.5, n_jobs=-1, b9=True)
    b14, b8 = split_vals(df, n_trn)
    b1.fit(b14, y_train)
    return b1.b9
b9 = fonk1(df_keep)
print(f"OOB Score: {b9}")
b10 = ['saleYear', 'fiBaseModel', 'Grouser_Tracks']
b11 = fonk1(df_keep.drop(b10, axis=1))
print(f"OOB Score after dropping columns: {b11}")
b12 = get_sample(df_raw[df_raw.YearMade > 1930], 500)
ggplot(b12, aes("YearMade", "SalePrice")) + stat_smooth(b13 = True, method="loess")
b14 = get_sample(X_train[X_train.YearMade > 1930], 500)
def fonk2(feat, b15 = None, b16=None):
    b16 = b16 or feat
    b17 = pdp.pdp_isolate(b1, b14, feat)
    return pdp.pdp_plot(b17, b16, b18 = True, cluster=b15 is not None, n_cluster_centers=b15)
fonk2("YearMade")
fonk2("YearMade", b15 = 5)
df_train, b19 = split_vals(df_raw[df_keep.columns], n_trn)
b20 = X_valid.values[None, 0]
prediction, bias, b21 = ti.predict(b1, b20)
print(f"Prediction: {prediction[0]}, Bias: {bias[0]}")
b22 = np.argsort(b21[0])
b23 = [(df_keep.columns[idx], b19.iloc[0][idx], b21[0][idx]) for idx in b22]
for info in b23:
    print(info)