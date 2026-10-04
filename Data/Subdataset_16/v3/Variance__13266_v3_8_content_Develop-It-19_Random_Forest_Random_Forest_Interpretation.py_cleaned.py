import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import scipy.cluster.hierarchy as hc
from sklearn.ensemble import RandomForestRegressor
from pdpbox import pdp
from plotnine import ggplot, aes, stat_smooth
from treeinterpreter import treeinterpreter as ti
def fonk1(n):
    np.random.seed(n)
fonk1(50000)
def fonk2(X_train, y_train):
    b1 = RandomForestRegressor(
        b2 = 40,
        b3 = 3,
        b4 = 0.5,
        b5 = -1,
        b6 = True
    )
    b1.fit(X_train, y_train)
    return b1
def fonk3(fi, b7 = 0.005):
    b8 = fi[fi.imp > b7].cols
    return b8, len(b8)
def fonk4(df_keep):
    b9 = np.round(scipy.stats.spearmanr(df_keep).correlation, 4)
    b10 = hc.distance.squareform(1 - b9)
    b11 = hc.linkage(b10, method="average")
    plt.figure(b12 = (16, 10))
    hc.dendrogram(b11, b13 = df_keep.columns, orientation="left", leaf_font_size=16)
    plt.show()
def fonk5(df, y_train, n_trn, split_vals):
    def fonk6(df):
        b1 = RandomForestRegressor(
            b2 = 40,
            b3 = 3,
            b4 = 0.5,
            b5 = -1,
            b6 = True
        )
        x, b14 = split_vals(df, n_trn)
        b1.fit(x, y_train)
        return b1.oob_score_
    return fonk6(df)
def fonk7(b1, x, feat, b15 = None, b16=None):
    b16 = b16 or feat
    b17 = pdp.pdp_isolate(b1=b1, dataset=x, model_features=x.columns, feature=feat)
    return pdp.pdp_plot(b17, b16, b18 = True, cluster=b15 is not None, n_cluster_centers=b15)
def fonk8(df_raw):
    b19 = get_sample(df_raw[df_raw.YearMade > 1930], 500)
    b17 = ggplot(b19, aes("YearMade", "SalePrice")) + stat_smooth(se=True, method="loess")
    print(b17)
def fonk9(b1, X_valid, df_keep, df_raw, n_trn, split_vals):
    df_train, b20 = split_vals(df_raw[df_keep.columns], n_trn)
    b21 = X_valid.values[None, 0]
    prediction, bias, b22 = ti.predict(b1, b21)
    b23 = np.argsort(b22[0])
    b24 = [(col, val, cont) for col, val, cont in zip(df_keep.columns[b23], b20.iloc[0][b23], b22[0][b23])]
    return prediction[0], bias[0], b24
b1 = fonk2(X_train, y_train)
print_score(b1)
b8, b25 = fonk3(fi)
print(f"Number of important features: {b25}")
fonk4(df_keep)
b6 = fonk5(df_keep, y_train, n_trn, split_vals)
print(f"OOB Score: {b6}")
b26 = ['saleYear', 'fiBaseModel', 'Grouser_Tracks']
b27 = fonk5(df_keep.drop(b26, axis=1), y_train, n_trn, split_vals)
print(f"OOB Score after dropping features: {b27}")
fonk8(df_raw)
b28 = get_sample(X_train[X_train.YearMade > 1930], 500)
fonk7(b1, b28, "YearMade")
fonk7(b1, b28, "YearMade", b15 = 5)
prediction, bias, b24 = fonk9(b1, X_valid, df_keep, df_raw, n_trn, split_vals)
print(f"Prediction: {prediction}, Bias: {bias}, Interpretation: {b24}")