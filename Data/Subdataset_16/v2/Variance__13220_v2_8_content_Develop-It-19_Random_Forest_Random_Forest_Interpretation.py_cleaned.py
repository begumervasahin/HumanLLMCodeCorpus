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
def fonk2(b24, b25):
    b1 = RandomForestRegressor(
        b2 = 40,
        b3 = 3,
        b4 = 0.5,
        b5 = -1,
        b6 = True
    )
    b1.fit(b24, b25)
    return b1
def fonk3(b26):
    b7 = b26[b26.imp > 0.005].cols
    return b7, len(b7)
def fonk4(b27):
    b8 = np.round(scipy.stats.spearmanr(b27).correlation, 4)
    b9 = hc.distance.squareform(1 - b8)
    b10 = hc.linkage(b9, method="average")
    plt.figure(b11 = (16, 10))
    hc.dendrogram(b10, b12 = b27.columns, orientation="left", leaf_font_size=16)
    plt.show()
def fonk5(df, b25, b29, b30):
    def fonk6(df):
        b1 = RandomForestRegressor(
            b2 = 40,
            b3 = 3,
            b4 = 0.5,
            b5 = -1,
            b6 = True
        )
        x, b13 = b30(df, b29)
        b1.fit(x, b25)
        return b1.oob_score_
    return fonk6(df)
def fonk7(b1, x, feat, b14 = None, b15=None):
    b15 = b15 or feat
    b16 = pdp.pdp_isolate(b1=b1, dataset=x, model_features=x.columns, feature=feat)
    return pdp.pdp_plot(b16, b15, b17 = True, cluster=b14 is not None, n_cluster_centers=b14)
def fonk8(b28):
    b18 = get_sample(b28[b28.YearMade > 1930], 500)
    b16 = ggplot(b18, aes("YearMade", "SalePrice")) + stat_smooth(se=True, method="loess")
    print(b16)
def fonk9(b1, X_valid, b27, b28, b29, b30):
    df_train, b19 = b30(b28[b27.columns], b29)
    b20 = X_valid.values[None, 0]
    prediction, bias, b21 = ti.predict(b1, b20)
    b22 = np.argsort(b21[0])
    b23 = [(col, val, cont) for col, val, cont in zip(b27.columns[b22], b19.iloc[0][b22], b21[0][b22])]
    return prediction[0], bias[0], b23
b24 = ...
b25 = ...
b26 = ...
b27 = ...
b28 = ...
b29 = ...
b30 = ...
b1 = fonk2(b24, b25)
print_score(b1)
b7, b31 = fonk3(b26)
print(f"Number of important features: {b31}")
fonk4(b27)
b6 = fonk5(b27, b25, b29, b30)
print(f"OOB Score: {b6}")
b32 = ['saleYear', 'fiBaseModel', 'Grouser_Tracks']
b33 = fonk5(b27.drop(b32, axis=1), b25, b29, b30)
print(f"OOB Score after dropping features: {b33}")
fonk8(b28)
b34 = get_sample(b24[b24.YearMade > 1930], 500)
fonk7(b1, b34, "YearMade")
fonk7(b1, b34, "YearMade", b14 = 5)
prediction, bias, b23 = fonk9(b1, X_valid, b27, b28, b29, b30)
print(f"Prediction: {prediction}, Bias: {bias}, Interpretation: {b23}")