import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import scipy.cluster.hierarchy as hc
from sklearn.ensemble import RandomForestRegressor
from pdpbox import pdp
from plotnine import ggplot, aes, stat_smooth
from treeinterpreter import treeinterpreter as ti
set_rf_samples(50000)
def fonk1(X_train, b24):
    b1 = RandomForestRegressor(
        b2 = 40,
        b3 = 3,
        b4 = 0.5,
        b5 = -1,
        b6 = True
    )
    b1.fit(X_train, b24)
    return b1
def fonk2(fi):
    b7 = fi[fi.imp > 0.005].cols
    return b7, len(b7)
def fonk3(b25):
    b8 = np.round(scipy.stats.spearmanr(b25).correlation, 4)
    b9 = hc.distance.squareform(1 - b8)
    b10 = hc.linkage(b9, method="average")
    b11 = plt.figure(figsize=(16, 10))
    b12 = hc.b12(b10, labels=b25.columns, orientation="left", leaf_font_size=16)
    plt.show()
def fonk4(df, b24, b26):
    def fonk5(df):
        b1 = RandomForestRegressor(
            b2 = 40,
            b3 = 3,
            b4 = 0.5,
            b5 = -1,
            b6 = True
        )
        x, b13 = split_vals(df, b26)
        b1.fit(x, b24)
        return b1.oob_score_
    return fonk5(df)
def fonk6(b1, x, feat, b14 = None, b15=None):
    b15 = b15 or feat
    b16 = pdp.pdp_isolate(b1=b1, dataset=x, model_features=x.columns, feature=feat)
    return pdp.pdp_plot(b16, b15, b17 = True, cluster=b14 is not None, n_cluster_centers=b14)
def fonk7(df_raw):
    b18 = get_sample(df_raw[df_raw.YearMade > 1930], 500)
    b16 = ggplot(b18, aes("YearMade", "SalePrice")) + stat_smooth(se=True, method="loess")
    print(b16)
def fonk8(b1, X_valid, b25, b19, b26):
    df_train, b19 = split_vals(df_raw[b25.columns], b26)
    b20 = X_valid.values[None, 0]
    prediction, bias, b21 = ti.predict(b1, b20)
    b22 = np.argsort(b21[0])
    b23 = [(col, val, cont) for col, val, cont in zip(b25.columns[b22], b19.iloc[0][b22], b21[0][b22])]
    return prediction[0], bias[0], b23
X_train, b24 = fi =
b25 = df_raw =
b26 = b1 = fonk1(X_train, b24)
print_score(b1)
b7, b27 = fonk2(fi)
print(f"Number of important features: {b27}")
fonk3(b25)
b6 = fonk4(b25, b24, b26)
print(f"OOB Score: {b6}")
b28 = ['saleYear', 'fiBaseModel', 'Grouser_Tracks']
b29 = fonk4(b25.drop(b28, axis=1), b24, b26)
print(f"OOB Score after dropping features: {b29}")
fonk7(df_raw)
b30 = get_sample(X_train[X_train.YearMade > 1930], 500)
fonk6(b1, b30, "YearMade")
fonk6(b1, b30, "YearMade", b14 = 5)
prediction, bias, b23 = fonk8(b1, X_valid, b25, b19, b26)
print(f"Prediction: {prediction}, Bias: {bias}, Interpretation: {b23}")