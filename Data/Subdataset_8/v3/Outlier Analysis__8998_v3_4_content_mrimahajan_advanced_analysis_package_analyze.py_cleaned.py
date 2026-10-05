import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis, chisquare
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
def divide_numerical_categorical(df):
    numerical = []
    categorical = []
    for col in df.columns:
        if df[col].dtype in ['int64', 'float64', 'int32', 'float32']:
            numerical.append(col)
        else:
            categorical.append(col)
    return numerical, categorical
def compute_statistics(data):
    df_desc = data.describe().transpose()
    df_desc['Variable'] = df_desc.index
    df_desc.reset_index(inplace=True, drop=True)
    df_desc.drop('count', axis=1, inplace=True)
    df_desc['skewness'] = df_desc['Variable'].apply(lambda x: skew(np.array(data.loc[data[x].notnull(), x])))
    df_desc['kurtosis'] = df_desc['Variable'].apply(
        lambda x: kurtosis(np.array(data.loc[data[x].notnull(), x]), fisher=False)))
    return df_desc
def calculate_percentiles(data, percentile):
    result = {}
    for pct in percentile:
        result['p' + str(int(pct * 100))] = data.quantile(pct)
    return result
def calculate_mean_and_sigma(data, cv):
    result = {}
    for dev in cv:
        result['mean-' + str(int(dev)) + 'sigma'] = data['mean'] - dev * data['std']
        result['mean+' + str(int(dev)) + 'sigma'] = data['mean'] + dev * data['std']
    return result
def summarize_categorical_data(data, categorical, percentile):
    df_categorical = pd.DataFrame()
    df_categorical['Variable'] = np.array(categorical)
    df_categorical['Type'] = 'Categorical'
    for col in categorical:
        df_var = data[col].value_counts(ascending=True, dropna=False).cumsum() / data.shape[0]
        df_cat = pd.DataFrame(df_var)
        df_cat.reset_index(inplace=True)
        df_cat.columns = ['Categories', 'Cumulative_Percentage']
        df_categorical.loc[df_categorical['Variable'] == col, 'Minimum'] = list(df_cat['Categories'])[0]
        df_categorical.loc[df_categorical['Variable'] == col, 'Maximum'] = list(df_cat['Categories'])[-1]
        for pct in percentile:
            df_categorical.loc[df_categorical['Variable'] == col, 'p' + str(int(pct * 100))] = \
                list(df_cat.loc[df_cat['Cumulative_Percentage'] >= pct, 'Categories'])[0]
        del df_var
        del df_cat
    return df_categorical
def calculate_missing_values(data, edd_summary):
    edd_summary['Count'] = edd_summary['Variable'].apply(lambda x: data[x].count())
    edd_summary['Missing_Values'] = data.shape[0] - edd_summary['Count']
    edd_summary['Missing_Rate'] = (edd_summary['Missing_Values'] / data.shape[0]) * 100
    return edd_summary
def exploratory_data_analysis(data, dependent_variable=None, regression=True, percentile=[.01, .05, .1, .5, .9, .95, .99], cv=[2, 3]):
    numerical, categorical = divide_numerical_categorical(data)
    stats_summary = compute_statistics(data)
    stats_summary['Type'] = 'Numeric'
    categorical_summary = summarize_categorical_data(data, categorical, percentile)
    edd_summary = pd.concat([stats_summary, categorical_summary])
    edd_summary = calculate_missing_values(data, edd_summary)
    if dependent_variable:
        edd_summary['Correlation/P_Value'] = np.nan
        if regression:
            correlation_matrix = data.corr()
            for col in numerical:
                edd_summary.loc[edd_summary['Variable'] == col, 'Correlation/P_Value'] = correlation_matrix.loc[col, dependent_variable]
            for col in categorical:
                model = ols(dependent_variable + ' ~ ' + col, data=data).fit()
                anova_table = sm.stats.anova_lm(model, type=2)
                edd_summary.loc[edd_summary['Variable'] == col, 'Correlation/P_Value'] = anova_table.loc[col, 'PR(>F)']
        else:
            for col in numerical:
                model = ols(col + ' ~ ' + dependent_variable, data=data).fit()
                anova_table = sm.stats.anova_lm(model, type=2)
                edd_summary.loc[edd_summary['Variable'] == col, 'Correlation/P_Value'] = anova_table.loc[dependent_variable, 'PR(>F)']
            for col in categorical:
                cross_table = pd.crosstab(data[dependent_variable], data[col], dropna=False)
                edd_summary.loc[edd_summary['Variable'] == col, 'Correlation/P_Value'] = chisquare(np.reshape(np.array(cross_table), np.product(cross_table.shape))).pvalue
    edd_summary.reset_index(drop=True, inplace=True)
    return edd_summary
def visualize_data(data, dependent_variable, path='', regression=True):
    numerical, categorical = divide_numerical_categorical(data)
    if regression:
        for col in numerical:
            if col != dependent_variable:
                ax = data.plot(col, dependent_variable)
                fig = ax.get_figure()
                fig.savefig(path + col + '.png', dpi=1000)
                plt.close(fig)
        for col in categorical:
            if col != dependent_variable:
                ax = data.boxplot(dependent_variable, by=col)
                fig = ax.get_figure()
                fig.savefig(path + col + '.png', dpi=1000)
                plt.close(fig)
    else:
        for col in numerical:
            if col != dependent_variable:
                ax = data.boxplot(col, by=dependent_variable)
                fig = ax.get_figure()
                fig.savefig(path + col + '.png', dpi=1000)
                plt.close(fig)
        for col in categorical:
            if col != dependent_variable:
                cross_table = pd.crosstab(data[dependent_variable], data[col], dropna=False)
                for cat in cross_table.columns:
                    cross_table[cat] = cross_table[cat].apply(lambda x: x / cross_table[cat].sum() * 100)
                ax = plt.subplot(111, frame_on=False)
                ax.xaxis.set_visible(False)
                ax.yaxis.set_visible(False)
                table(ax, cross_table)
                plt.savefig(path + col + '.png', dpi=1000)
                plt.close()
