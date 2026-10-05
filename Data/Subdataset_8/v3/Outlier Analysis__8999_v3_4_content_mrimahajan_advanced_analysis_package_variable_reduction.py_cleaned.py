import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.discrete.discrete_model as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
def inter_correlation_clusters(data, cutoff=0.7):
    correlations = data.corr()
    columns = data.columns
    graph = {i: [] for i in range(len(columns))}
    for i in range(len(columns)):
        for j in range(len(columns)):
            if i != j and np.abs(correlations.iloc[i, j]) > cutoff:
                graph[i].append(j)
    tree_set = {}
    component = 0
    visited = [0] * len(columns)
    def dfs(i):
        visited[i] = 1
        tree_set.setdefault(component, []).append(i)
        for j in graph[i]:
            if visited[j] == 0:
                dfs(j)
    for i in range(len(columns)):
        if visited[i] == 0:
            dfs(i)
            component += 1
    tree_cluster = {key: [columns[i] for i in value] for key, value in tree_set.items()}
    return tree_cluster
def varclus(data, cutoff, maxkeep=1, maxdrop=None):
    columns = []
    clusters = inter_correlation_clusters(data, cutoff=cutoff)
    def distance(c1, c2):
        return np.max([[np.abs(correlations.loc[i, j]) for i in clusters[c1]] for j in clusters[c2]])
    def next_closest(c):
        minima = 0
        point = c
        for c1 in [i for i in clusters.keys() if i != c]:
            dist = distance(c, c1)
            if dist > minima:
                minima = dist
                point = c1
        return point
    def get_squared_ratio(col, own_cluster, next_cluster):
        y = np.array(data[col])
        x = np.array(data[own_cluster].drop(col, axis=1))
        model = LinearRegression()
        model.fit(x, y)
        y_pred = model.predict(x)
        r2_own = r2_score(y, y_pred)
        del x, model
        x = np.array(data[next_cluster])
        model = LinearRegression()
        model.fit(x, y)
        y_pred = model.predict(x)
        r2_next = r2_score(y, y_pred)
        del y, y_pred, model
        return float(1 - r2_own) / (1 - r2_next)
    for c1 in clusters.keys():
        clus_len = len(clusters[c1])
        if clus_len > 1:
            own_cluster = clusters[c1]
            next_cluster = clusters[next_closest(c1)]
            ratio_list = []
            for col in clusters[c1]:
                col_ratio = get_squared_ratio(col, own_cluster, next_cluster)
                ratio_list.append((col, col_ratio))
            ratio_list = sorted(ratio_list, key=lambda x: x[1])
            if maxdrop is not None:
                columns += [col[0] for col in ratio_list[:-min(maxdrop, clus_len)]]
            else:
                columns += [col[0] for col in ratio_list[:min(maxkeep, clus_len)]]
        else:
            columns.append(clusters[c1][0])
    return columns
def vif_reduction(data, limit=2.5):
    vif_drop_cols = []
    def variance_inflation(fn_data):
        vif = pd.DataFrame()
        vif['features'] = fn_data.columns
        vif['vif factor'] = [variance_inflation_factor(fn_data.values, i) for i in range(fn_data.shape[1])]
        vif.sort_values(by='vif factor', ascending=False, inplace=True)
        vif.reset_index(inplace=True, drop=True)
        print(vif)
        return vif
    def reduction(fn_data, cutoff=limit):
        vif = variance_inflation(fn_data)
        if vif['vif factor'].iloc[0] <= cutoff:
            return
        else:
            col_to_drop = vif['features'].iloc[0]
            fn_data.drop(col_to_drop, axis=1, inplace=True)
            vif_drop_cols.append(col_to_drop)
            print(col_to_drop + ' dropped')
            reduction(fn_data, cutoff=limit)
    reduction(data)
    return vif_drop_cols
def backward_selection(df, dv, regression=True, alpha=0.05):
    cols_dropped = [dv]
    while True:
        if regression:
            model = sm.OLS(endog=np.array(df[dv]), exog=np.array(df.drop(cols_dropped, axis=1)))
        else:
            model = sm.Logit(endog=np.array(df[dv]), exog=np.array(df.drop(cols_dropped, axis=1)))
        results = model.fit()
        pvalues = results.pvalues
        drop_index = pvalues.argmax()
        col_drop = df.drop(cols_dropped, axis=1).columns[drop_index]
        print(f"{col_drop} - {pvalues[drop_index]}")
        if pvalues[drop_index] > alpha:
            cols_dropped.append(col_drop)
        else:
            break
    cols_dropped.remove(dv)
    return cols_dropped
if __name__ == "__main__":
    clusters = inter_correlation_clusters(data, cutoff=0.7)
    print(clusters)
    reduced_columns = varclus(data, cutoff=0.7)
    print(reduced_columns)
    vif_dropped_cols = vif_reduction(data, limit=2.5)
    print(vif_dropped_cols)
    dropped_cols = backward_selection(data, dv='target_variable', regression=True, alpha=0.05)
    print(dropped_cols)