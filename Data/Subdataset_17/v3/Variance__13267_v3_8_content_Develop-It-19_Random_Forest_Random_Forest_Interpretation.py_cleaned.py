import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import scipy.cluster.hierarchy as hc
from sklearn.ensemble import RandomForestRegressor
from pdpbox import pdp
from plotnine import ggplot, aes, stat_smooth
from treeinterpreter import treeinterpreter as ti
def set_rf_samples(n):
    np.random.seed(n)
set_rf_samples(50000)
def initialize_model(X_train, y_train):
    model = RandomForestRegressor(
        n_estimators=40,
        min_samples_leaf=3,
        max_features=0.5,
        n_jobs=-1,
        oob_score=True
    )
    model.fit(X_train, y_train)
    return model
def get_important_features(fi, threshold=0.005):
    to_keep = fi[fi.imp > threshold].cols
    return to_keep, len(to_keep)
def plot_dendrogram(df_keep):
    corr = np.round(scipy.stats.spearmanr(df_keep).correlation, 4)
    corr_condensed = hc.distance.squareform(1 - corr)
    z = hc.linkage(corr_condensed, method="average")
    plt.figure(figsize=(16, 10))
    hc.dendrogram(z, labels=df_keep.columns, orientation="left", leaf_font_size=16)
    plt.show()
def get_oob_score(df, y_train, n_trn, split_vals):
    def get_oob(df):
        model = RandomForestRegressor(
            n_estimators=40,
            min_samples_leaf=3,
            max_features=0.5,
            n_jobs=-1,
            oob_score=True
        )
        x, _ = split_vals(df, n_trn)
        model.fit(x, y_train)
        return model.oob_score_
    return get_oob(df)
def plot_pdp(model, x, feat, clusters=None, feat_name=None):
    feat_name = feat_name or feat
    p = pdp.pdp_isolate(model=model, dataset=x, model_features=x.columns, feature=feat)
    return pdp.pdp_plot(p, feat_name, plot_lines=True, cluster=clusters is not None, n_cluster_centers=clusters)
def sample_and_plot(df_raw):
    x_all = get_sample(df_raw[df_raw.YearMade > 1930], 500)
    p = ggplot(x_all, aes("YearMade", "SalePrice")) + stat_smooth(se=True, method="loess")
    print(p)
def interpret_tree(model, X_valid, df_keep, df_raw, n_trn, split_vals):
    df_train, df_valid = split_vals(df_raw[df_keep.columns], n_trn)
    row = X_valid.values[None, 0]
    prediction, bias, contributions = ti.predict(model, row)
    idxs = np.argsort(contributions[0])
    interpretation = [(col, val, cont) for col, val, cont in zip(df_keep.columns[idxs], df_valid.iloc[0][idxs], contributions[0][idxs])]
    return prediction[0], bias[0], interpretation
model = initialize_model(X_train, y_train)
print_score(model)
to_keep, num_to_keep = get_important_features(fi)
print(f"Number of important features: {num_to_keep}")
plot_dendrogram(df_keep)
oob_score = get_oob_score(df_keep, y_train, n_trn, split_vals)
print(f"OOB Score: {oob_score}")
to_drop = ['saleYear', 'fiBaseModel', 'Grouser_Tracks']
oob_score_dropped = get_oob_score(df_keep.drop(to_drop, axis=1), y_train, n_trn, split_vals)
print(f"OOB Score after dropping features: {oob_score_dropped}")
sample_and_plot(df_raw)
x_sample = get_sample(X_train[X_train.YearMade > 1930], 500)
plot_pdp(model, x_sample, "YearMade")
plot_pdp(model, x_sample, "YearMade", clusters=5)
prediction, bias, interpretation = interpret_tree(model, X_valid, df_keep, df_raw, n_trn, split_vals)
print(f"Prediction: {prediction}, Bias: {bias}, Interpretation: {interpretation}")