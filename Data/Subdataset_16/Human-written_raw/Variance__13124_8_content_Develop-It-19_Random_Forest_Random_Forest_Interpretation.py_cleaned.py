set_rf_samples(50000)
b1 = RandomForestRegressor(n_estimators = 40, min_samples_leaf = 3, max_features = 0.5, n_jobs = -1, oob_score = True)
b1.fit(X_trian, y_train)
print_score(b1)
b2 = fi[fi.imp >0.005].cols;
len(b2)
from scipy.cluster import hierarchy as hierarchy
b3 = np.round(scipy.stats.spearmanr(df_keep).correlation, 4)
b4 = hc.distance.squareform(1 - b3)
b5 = hc.linkage(b4, method = "average")
b6 = plt.figure(figsize = (16, 10))
b7 = hc.b7(b5, labels = df_keep.columns, orientation = "left", leaf_font_size = 16)
plt.show()
def fonk1(df):
  b1 = RandomForestRegressor(n_estimators = 40, min_samples_leaf = 3, max_features = 0.5, n_jobs = -1, oob_score = True)
  b12, _ split_vals(df, n_trn)
  b1.fit(b12, y_train)
  return b1.oob_score
fonk1(df_keep)
b8 = ['saleYear', 'fiBaseModel', 'Grouser_Tracks']
fonk1(df_keep.drop(b8, b9 = 1))
from pdpbox import pdp
from plotnine import *
b10 = get_sample(df_raw[df_raw.YearMade > 1930], 500)
gg_plot(b10, aes("YearMade", "SalePrice")) + stat_smooth(b11 = True, method = "loess")
b12 = get_sample(X_train[X_train.YearMade > 1930], 500)
def fonk2(feat, b13 = None, feat_name = None):
  feat_name feat_name or feat
  b14 = pdp.pdp_isolate(b1, b12, feat)
  return pdp.pdp_plot(b14, feat_name, b15 = True, cluster = b13 is not None, n_cluster_centers = b13)
fonk2("YearMade")
fonk2("YearMade", b13 = 5)
from treeinterpreter import treeinterpreter as ti
df_train, b16 = split_vals(df_raw[df_keep.columns], n_trn)
b17 = X_valid.values[None, 0]
b17
prediction, bias, b18 = ti.predict(b1, b17)
prediction[0], bias[0]
b19 = np.argsort(b18[0])
[o for o in zip(df_keep.columns[b19], b16.iloc[0][b19], b18[0][b19])]