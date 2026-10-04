import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import scipy.cluster.hierarchy as hc
from sklearn.ensemble import RandomForestRegressor
from pdpbox import pdp
from plotnine import *
from treeinterpreter import treeinterpreter as ti
def print_model_score(model):
    pass
def get_sample(df, n):
    return df.sample(n)
def split_vals(df, n):
    return df[:n], df[n:]
def train_random_forest(X_train, y_train):
    rf_samples = 50000
    model = RandomForestRegressor(n_estimators=40, min_samples_leaf=3, max_features=0.5, n_jobs=-1, oob_score=True)
    model.fit(X_train, y_train)
    return model
model = train_random_forest(X_train, y_train)
print_model_score(model)
feature_importance_threshold = 0.005
to_keep = fi[fi.imp > feature_importance_threshold].cols
print(f"Number of features to keep: {len(to_keep)}")
def plot_dendrogram(df):
    corr = np.round(scipy.stats.spearmanr(df).correlation, 4)
    corr_condensed = hc.distance.squareform(1 - corr)
    z = hc.linkage(corr_condensed, method="average")
    plt.figure(figsize=(16, 10))
    hc.dendrogram(z, labels=df.columns, orientation="left", leaf_font_size=16)
    plt.show()
plot_dendrogram(df_keep)
def get_oob_score(df, n_trn, y_train):
    model = RandomForestRegressor(n_estimators=40, min_samples_leaf=3, max_features=0.5, n_jobs=-1, oob_score=True)
    x_train, _ = split_vals(df, n_trn)
    model.fit(x_train, y_train)
    return model.oob_score
oob_score = get_oob_score(df_keep, n_trn, y_train)
print(f"OOB Score: {oob_score}")
columns_to_drop = ['saleYear', 'fiBaseModel', 'Grouser_Tracks']
df_keep_dropped = df_keep.drop(columns=columns_to_drop)
oob_score_dropped = get_oob_score(df_keep_dropped, n_trn, y_train)
print(f"OOB Score after dropping columns: {oob_score_dropped}")
def plot_ggplot(df):
    x_all = get_sample(df[df.YearMade > 1930], 500)
    plot = (ggplot(x_all, aes("YearMade", "SalePrice"))
            + stat_smooth(se=True, method="loess"))
    print(plot)
plot_ggplot(df_raw)
def plot_partial_dependence(model, feature, data, clusters=None, feature_name=None):
    feature_name = feature_name or feature
    pdp_isolated = pdp.pdp_isolate(model, data, feature)
    pdp.pdp_plot(pdp_isolated, feature_name, plot_lines=True, cluster=clusters is not None, n_cluster_centers=clusters)
x_sample = get_sample(X_train[X_train.YearMade > 1930], 500)
plot_partial_dependence(model, "YearMade", x_sample)
plot_partial_dependence(model, "YearMade", x_sample, clusters=5)
df_train, df_valid = split_vals(df_raw[df_keep.columns], n_trn)
row = X_valid.values[None, 0]
prediction, bias, contributions = ti.predict(model, row)
print(f"Prediction: {prediction[0]}, Bias: {bias[0]}")
def print_feature_contributions(df_keep, df_valid, contributions):
    idxs = np.argsort(contributions[0])
    contributions_info = [(df_keep.columns[idx], df_valid.iloc[0][idx], contributions[0][idx]) for idx in idxs]
    for info in contributions_info:
        print(info)
print_feature_contributions(df_keep, df_valid, contributions)