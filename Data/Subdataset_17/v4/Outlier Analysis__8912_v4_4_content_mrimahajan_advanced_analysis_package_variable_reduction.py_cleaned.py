import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm
def inter_correlation_clusters(data, cutoff=0.7):
    correlations = data.corr()
    columns = data.columns
    graph = {i: [j for j in range(len(columns)) if i != j and np.abs(correlations.iloc[i, j]) > cutoff] for i in range(len(columns))}
    tree_set = {}
    component = 0
    visited = [0] * len(columns)
    def dfs(i):
        visited[i] = 1
        tree_set.setdefault(component, []).append(i)
        for j in graph[i]:
            if not visited[j]:
                dfs(j)
    for i in range(len(columns)):
        if not visited[i]:
            dfs(i)
            component += 1
    tree_cluster = {key: [columns[i] for i in indices] for key, indices in tree_set.items()}
    return tree_cluster
def varclus(data, cutoff, maxkeep=1, maxdrop=None):
    clusters = inter_correlation_clusters(data, cutoff)
    columns = []
    def distance(c1, c2):
        return np.max([[np.abs(data.corr().loc[i, j]) for i in clusters[c1]] for j in clusters[c2]])
    def next_closest(c):
        return max([(distance(c, c1), c1) for c1 in clusters if c1 != c], key=lambda x: x[0])[1]
    def get_squared_ratio(col, own_cluster, next_cluster):
        y = data[col].values
        x_own = data[own_cluster].drop(col, axis=1).values
        x_next = data[next_cluster].values
        model = LinearRegression().fit(x_own, y)
        r2_own = r2_score(y, model.predict(x_own))
        model = LinearRegression().fit(x_next, y)
        r2_next = r2_score(y, model.predict(x_next))
        return (1 - r2_own) / (1 - r2_next)
    for c1 in clusters:
        own_cluster = clusters[c1]
        if len(own_cluster) > 1:
            next_cluster = clusters[next_closest(c1)]
            ratio_list = [(col, get_squared_ratio(col, own_cluster, next_cluster)) for col in own_cluster]
            ratio_list.sort(key=lambda x: x[1])
            if maxdrop:
                columns += [col[0] for col in ratio_list[:-min(maxdrop, len(own_cluster))]]
            else:
                columns += [col[0] for col in ratio_list[:min(maxkeep, len(own_cluster))]]
        else:
            columns.append(own_cluster[0])
    return columns
def vif_reduction(data, limit=2.5):
    vif_drop_cols = []
    def calculate_vif(df):
        vif = pd.DataFrame()
        vif['features'] = df.columns
        vif['vif factor'] = [variance_inflation_factor(df.values, i) for i in range(df.shape[1])]
        return vif.sort_values(by='vif factor', ascending=False).reset_index(drop=True)
    def reduce_vif(df, threshold):
        while True:
            vif = calculate_vif(df)
            if vif.loc[0, 'vif factor'] <= threshold:
                break
            else:
                drop_col = vif.loc[0, 'features']
                df.drop(columns=drop_col, inplace=True)
                vif_drop_cols.append(drop_col)
                print(f"{drop_col} dropped due to high VIF")
    reduce_vif(data.copy(), limit)
    return vif_drop_cols
def backward_selection(df, target_var, regression=True, alpha=0.05):
    dropped_columns = []
    remaining_columns = list(df.columns)
    remaining_columns.remove(target_var)
    while True:
        if regression:
            model = sm.OLS(df[target_var], sm.add_constant(df[remaining_columns])).fit()
        else:
            model = sm.Logit(df[target_var], sm.add_constant(df[remaining_columns])).fit()
        pvalues = model.pvalues.iloc[1:]
        max_pvalue = pvalues.max()
        if max_pvalue > alpha:
            drop_col = pvalues.idxmax()
            remaining_columns.remove(drop_col)
            dropped_columns.append(drop_col)
            print(f"Dropped {drop_col} with p-value {max_pvalue}")
        else:
            break
    return dropped_columns