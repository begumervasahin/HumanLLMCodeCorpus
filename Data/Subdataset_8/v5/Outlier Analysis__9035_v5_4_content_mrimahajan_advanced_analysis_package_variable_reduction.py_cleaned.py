import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.discrete.discrete_model as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
def inter_correlation_clusters(data, cutoff=0.7):
    correlations = data.corr()
    clusters = {}
    columns = data.columns
    def dfs(i, component):
        visited[i] = True
        clusters.setdefault(component, []).append(i)
        for j in graph[i]:
            if not visited[j]:
                dfs(j, component)
    graph = {i: [] for i in range(len(columns))}
    for i in range(len(columns)):
        for j in range(len(columns)):
            if i != j and abs(correlations.iloc[i, j]) > cutoff:
                graph[i].append(j)
    visited = [False] * len(columns)
    component = 0
    for i in range(len(columns)):
        if not visited[i]:
            dfs(i, component)
            component += 1
    tree_cluster = {key: [columns[i] for i in val] for key, val in clusters.items()}
    return tree_cluster
def varclus(data, cutoff, maxkeep=1, maxdrop=None):
    columns = []
    correlations = data.corr()
    clusters = inter_correlation_clusters(data, cutoff=cutoff)
    def distance(c1, c2):
        return np.max([[abs(correlations.loc[i, j]) for i in clusters[c1]] for j in clusters[c2]])
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
        y = data[col].values
        x = data[own_cluster].drop(col, axis=1).values
        model = LinearRegression().fit(x, y)
        y_pred = model.predict(x)
        r2_own = r2_score(y, y_pred)
        x = data[next_cluster].values
        model = LinearRegression().fit(x, y)
        y_pred = model.predict(x)
        r2_next = r2_score(y, y_pred)
        return float(1 - r2_own) / (1 - r2_next)
    for c1, own_cluster in clusters.items():
        clus_len = len(own_cluster)
        if clus_len > 1:
            next_cluster = clusters[next_closest(c1)]
            ratio_list = [(col, get_squared_ratio(col, own_cluster, next_cluster)) for col in own_cluster]
            ratio_list = sorted(ratio_list, key=lambda x: x[1])
            if maxdrop is not None:
                columns += [col[0] for col in ratio_list[:-min(maxdrop, clus_len)]]
            else:
                columns += [col[0] for col in ratio_list[:min(maxkeep, clus_len)]]
        else:
            columns.append(own_cluster[0])
    return columns
def vif_reduction(data, limit=2.5):
    vif_drop_cols = []
    def variance_inflation(fn_data):
        vif = pd.DataFrame({'features': fn_data.columns,
                            'vif factor': [variance_inflation_factor(fn_data.values, i) for i in range(fn_data.shape[1])]})
        vif.sort_values(by='vif factor', ascending=False, inplace=True)
        return vif.iloc[0]
    def reduction(fn_data, cutoff=limit):
        vif = variance_inflation(fn_data)
        if vif['vif factor'] <= cutoff:
            return
        else:
            fn_data.drop(vif['features'], axis=1, inplace=True)
            vif_drop_cols.append(vif['features'])
            reduction(fn_data, cutoff=limit)
    reduction(data)
    return vif_drop_cols
def backward_selection(df, dv, regression=True, alpha=0.05):
    cols_dropped = [dv]
    model_func = sm.OLS if regression else sm.Logit
    while True:
        model = model_func(endog=df[dv].values, exog=df.drop(cols_dropped, axis=1).values)
        results = model.fit()
        pvalues = list(results.pvalues)
        drop_index = pvalues.index(max(pvalues))
        col_drop = df.drop(cols_dropped, axis=1).columns[drop_index]
        if pvalues[drop_index] > alpha:
            cols_dropped.append(col_drop)
        else:
            break
    cols_dropped.remove(dv)
    return cols_dropped