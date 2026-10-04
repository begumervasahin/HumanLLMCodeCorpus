import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm
def inter_correlation_clusters(data, cutoff=0.7):
    correlations = data.corr()
    graph = {i: [] for i in range(len(data.columns))}
    for i in range(len(data.columns)):
        for j in range(len(data.columns)):
            if i != j and np.abs(correlations.iloc[i, j]) > cutoff:
                graph[i].append(j)
    def dfs(node, component):
        visited[node] = True
        tree_set[component].append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, component)
    tree_set = {}
    component = 0
    visited = [False] * len(data.columns)
    for i in range(len(data.columns)):
        if not visited[i]:
            tree_set[component] = []
            dfs(i, component)
            component += 1
    tree_cluster = {key: [data.columns[i] for i in indices] for key, indices in tree_set.items()}
    return tree_cluster
def varclus(data, cutoff=0.7, maxkeep=1, maxdrop=None):
    clusters = inter_correlation_clusters(data, cutoff=cutoff)
    columns = []
    def distance(cluster1, cluster2):
        return np.max([[np.abs(correlations.loc[i, j]) for i in clusters[cluster1]] for j in clusters[cluster2]])
    def next_closest(cluster):
        max_dist = 0
        closest_cluster = cluster
        for other_cluster in [c for c in clusters.keys() if c != cluster]:
            dist = distance(cluster, other_cluster)
            if dist > max_dist:
                max_dist = dist
                closest_cluster = other_cluster
        return closest_cluster
    def get_squared_ratio(col, own_cluster, next_cluster):
        y = data[col].values
        x_own = data[own_cluster].drop(columns=[col]).values
        x_next = data[next_cluster].values
        model_own = LinearRegression().fit(x_own, y)
        r2_own = r2_score(y, model_own.predict(x_own))
        model_next = LinearRegression().fit(x_next, y)
        r2_next = r2_score(y, model_next.predict(x_next))
        return (1 - r2_own) / (1 - r2_next)
    correlations = data.corr()
    for cluster in clusters.keys():
        cluster_size = len(clusters[cluster])
        if cluster_size > 1:
            own_cluster = clusters[cluster]
            next_cluster = clusters[next_closest(cluster)]
            ratio_list = [(col, get_squared_ratio(col, own_cluster, next_cluster)) for col in clusters[cluster]]
            ratio_list.sort(key=lambda x: x[1])
            if maxdrop is not None:
                columns += [col for col, _ in ratio_list[:-min(maxdrop, cluster_size)]]
            else:
                columns += [col for col, _ in ratio_list[:min(maxkeep, cluster_size)]]
        else:
            columns.append(clusters[cluster][0])
    return columns
def vif_reduction(data, limit=2.5):
    dropped_columns = []
    def calculate_vif(df):
        vif_data = pd.DataFrame()
        vif_data['feature'] = df.columns
        vif_data['VIF'] = [variance_inflation_factor(df.values, i) for i in range(df.shape[1])]
        return vif_data
    def reduce_vif(df):
        while True:
            vif_data = calculate_vif(df)
            max_vif = vif_data['VIF'].max()
            if max_vif <= limit:
                break
            max_vif_feature = vif_data.loc[vif_data['VIF'].idxmax(), 'feature']
            df.drop(columns=[max_vif_feature], inplace=True)
            dropped_columns.append(max_vif_feature)
    reduce_vif(data.copy())
    return dropped_columns
def backward_selection(df, dependent_var, regression=True, alpha=0.05):
    cols_dropped = [dependent_var]
    while True:
        if regression:
            model = sm.OLS(df[dependent_var], df.drop(columns=cols_dropped)).fit()
        else:
            model = sm.Logit(df[dependent_var], df.drop(columns=cols_dropped)).fit()
        pvalues = model.pvalues
        max_pvalue = pvalues.max()
        if max_pvalue > alpha:
            drop_column = pvalues.idxmax()
            cols_dropped.append(drop_column)
        else:
            break
    cols_dropped.remove(dependent_var)
    return cols_dropped