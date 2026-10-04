import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis, chisquare
from statsmodels.formula.api import ols
import statsmodels.api as sm
from matplotlib import pyplot as plt
from pandas.plotting import table
def numerical_categorical_division(df):
    numerical, categorical = [], []
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            numerical.append(col)
        else:
            categorical.append(col)
    return numerical, categorical
def edd(data, dv=None, regression=True, percentiles=[.01, .05, .1, .5, .9, .95, .99], cv=[2, 3]):
    numerical, categorical = numerical_categorical_division(data)
    df_desc = data.describe().transpose()
    df_desc['Var'] = df_desc.index
    df_desc.reset_index(drop=True, inplace=True)
    df_desc.drop('count', axis=1, inplace=True)
    df_desc['skewness'] = df_desc['Var'].apply(lambda x: skew(data[x].dropna()))
    df_desc['kurtosis'] = df_desc['Var'].apply(lambda x: kurtosis(data[x].dropna(), fisher=False))
    for pct in percentiles:
        df_desc[f'p{int(pct * 100)}'] = df_desc['Var'].apply(lambda x: data[x].quantile(pct))
    for dev in cv:
        df_desc[f'mean-{dev}sigma'] = df_desc['mean'] - dev * df_desc['std']
        df_desc[f'mean+{dev}sigma'] = df_desc['mean'] + dev * df_desc['std']
    df_desc['type'] = 'numeric'
    df_categorical = pd.DataFrame({'Var': categorical, 'type': 'categorical'})
    for col in [c for c in df_desc.columns if c not in ['Var', 'type']]:
        df_categorical[col] = np.nan
    for col in categorical:
        df_var = data[col].value_counts(ascending=True, dropna=False).cumsum() / data.shape[0]
        df_cat = pd.DataFrame(df_var).reset_index()
        df_cat.columns = ['categories', 'cum_pct']
        df_categorical.loc[df_categorical['Var'] == col, 'min'] = df_cat['categories'].iloc[0]
        df_categorical.loc[df_categorical['Var'] == col, 'max'] = df_cat['categories'].iloc[-1]
        for pct in percentiles:
            df_categorical.loc[df_categorical['Var'] == col, f'p{int(pct * 100)}'] = df_cat.loc[df_cat['cum_pct'] >= pct, 'categories'].iloc[0]
    df_categorical = df_categorical[df_desc.columns]
    edd = pd.concat([df_desc, df_categorical], ignore_index=True)
    edd['count'] = edd['Var'].apply(lambda x: data[x].notnull().sum())
    edd['nmiss'] = data.shape[0] - edd['count']
    edd['missing_rate'] = edd['nmiss'] / data.shape[0] * 100
    edd['unique'] = edd['Var'].apply(lambda x: data[x].nunique())
    col_list = ['Var', 'type', 'count', 'nmiss', 'missing_rate', 'unique', 'std', 'skewness', 'kurtosis', 'mean', 'min'] + \
               [f'mean-{dev}sigma' for dev in cv] + [f'p{int(pct * 100)}' for pct in percentiles] + \
               [f'mean+{dev}sigma' for dev in cv] + ['max']
    edd = edd[col_list]
    if dv:
        edd['correlation/p_value'] = np.nan
        if regression:
            corr_matrix = data.corr()
            for col in numerical:
                edd.loc[edd['Var'] == col, 'correlation/p_value'] = corr_matrix.loc[col, dv]
            for col in categorical:
                mod = ols(f'{dv} ~ C({col})', data=data).fit()
                aov_table = sm.stats.anova_lm(mod, type=2)
                edd.loc[edd['Var'] == col, 'correlation/p_value'] = aov_table.loc[col, 'PR(>F)']
        else:
            for col in numerical:
                mod = ols(f'{col} ~ C({dv})', data=data).fit()
                aov_table = sm.stats.anova_lm(mod, type=2)
                edd.loc[edd['Var'] == col, 'correlation/p_value'] = aov_table.loc[dv, 'PR(>F)']
            for col in categorical:
                f = pd.crosstab(data[dv], data[col], dropna=False)
                edd.loc[edd['Var'] == col, 'correlation/p_value'] = chisquare(f.to_numpy().ravel()).pvalue
    edd.reset_index(drop=True, inplace=True)
    return edd
def graphical_analysis(data, dv, path='', regression=True):
    numerical, categorical = numerical_categorical_division(data)
    if regression:
        for col in numerical:
            if col != dv:
                ax = data.plot(x=col, y=dv, kind='scatter')
                fig = ax.get_figure()
                fig.savefig(f'{path}{col}.png', dpi=1000)
        for col in categorical:
            if col != dv:
                ax = data.boxplot(column=dv, by=col)
                fig = ax.get_figure()
                fig.savefig(f'{path}{col}.png', dpi=1000)
    else:
        for col in numerical:
            if col != dv:
                ax = data.boxplot(column=col, by=dv)
                fig = ax.get_figure()
                fig.savefig(f'{path}{col}.png', dpi=1000)
        for col in categorical:
            if col != dv:
                f = pd.crosstab(data[dv], data[col], dropna=False)
                for cat in f.columns:
                    f[cat] = f[cat] / f[cat].sum() * 100
                ax = plt.subplot(111, frame_on=False)
                ax.xaxis.set_visible(False)
                ax.yaxis.set_visible(False)
                table(ax, f)
                plt.savefig(f'{path}{col}.png', dpi=1000)