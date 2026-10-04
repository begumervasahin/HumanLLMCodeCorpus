import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import scipy.cluster.hierarchy as hc
from sklearn.ensemble import RandomForestRegressor
from pdpbox import pdp
from plotnine import *
from treeinterpreter import treeinterpreter as ti
rf_samples = 50000
model = RandomForestRegressor(n_estimators=40, min_samples_leaf=3, max_features=0.5, n_jobs=-1, oob_score=True)
model.fit(X_train, y_train)
print_score(model)
to_keep = fi[fi.imp > 0.005].cols
print(f"Number of features to keep: {len(to_keep)}")
corr = np.round(scipy.stats.spearmanr(df_keep).correlation, 4)
corr_condensed = hc.distance.squareform(1 - corr)
z = hc.linkage(corr_condensed, method="average")
fig = plt.figure(figsize=(16, 10))
dendrogram = hc.dendrogram(z, labels=df_keep.columns, orientation="left", leaf_font_size=16)
plt.show()
def get_oob(df):
    model = RandomForestRegressor(n_estimators=40, min_samples_leaf=3, max_features=0.5, n_jobs=-1, oob_score=True)
    x, _ = split_vals(df, n_trn)
    model.fit(x, y_train)
    return model.oob_score
oob_score = get_oob(df_keep)
print(f"OOB Score: {oob_score}")
to_drop = ['saleYear', 'fiBaseModel', 'Grouser_Tracks']
oob_score_dropped = get_oob(df_keep.drop(to_drop, axis=1))
print(f"OOB Score after dropping columns: {oob_score_dropped}")
x_all = get_sample(df_raw[df_raw.YearMade > 1930], 500)
ggplot(x_all, aes("YearMade", "SalePrice")) + stat_smooth(se=True, method="loess")
x = get_sample(X_train[X_train.YearMade > 1930], 500)
def plot_pdp(feat, clusters=None, feat_name=None):
    feat_name = feat_name or feat
    p = pdp.pdp_isolate(model, x, feat)
    return pdp.pdp_plot(p, feat_name, plot_lines=True, cluster=clusters is not None, n_cluster_centers=clusters)
plot_pdp("YearMade")
plot_pdp("YearMade", clusters=5)
df_train, df_valid = split_vals(df_raw[df_keep.columns], n_trn)
row = X_valid.values[None, 0]
prediction, bias, contributions = ti.predict(model, row)
print(f"Prediction: {prediction[0]}, Bias: {bias[0]}")
idxs = np.argsort(contributions[0])
contributions_info = [(df_keep.columns[idx], df_valid.iloc[0][idx], contributions[0][idx]) for idx in idxs]
for info in contributions_info:
    print(info)