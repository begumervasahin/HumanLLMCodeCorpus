import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
d1 = pd.read_csv('C:/Users/HOMEPCUSER/Desktop/Spring 19/Machine_Learning/Salaries-Simple_Linear.csv')
print(d1)
d1.shape
print(d1.columns)
d1.isnull().sum()
X = d1[["Years_of_Expertise"]]
Y = d1[["Salary"]]
X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()
model.summary()
X = d1[["Years_of_Expertise"]]
sns.set(color_codes=True)
sns.regplot(X, Y)
d2 = pd.read_csv('C:/Users/HOMEPCUSER/Desktop/Spring 19/Machine_Learning/3-Products-Multiple.csv')
print(d2)
d2.shape
d2.dtypes
print(d2.columns)
d2.isnull().sum()
d3 = d2[['Product_1','Product_2','Product_3','Profit']]
corr = d3.corr()
sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values)
from pandas.plotting import scatter_matrix
scatter_matrix(d3, figsize=(6, 6), diagonal='kde',color = 'r')
mod = smf.ols("Profit ~ Product_1+Product_2+Product_3+C(Location)", data=d2).fit()
mod.summary()
mod.params
def forward_selected(data, response):
    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score, best_new_score = 0.0, 0.0
    while remaining and current_score == best_new_score:
        scores_with_candidates = []
        for candidate in remaining:
            formula = "{} ~ {} + 1".format(response,
                                           ' + '.join(selected + [candidate]))
            score = smf.ols(formula, data).fit().rsquared_adj
            scores_with_candidates.append((score, candidate))
        scores_with_candidates.sort()
        best_new_score, best_candidate = scores_with_candidates.pop()
        if current_score < best_new_score:
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score
    formula = "{} ~ {} + 1".format(response,
                                   ' + '.join(selected))
    model = smf.ols(formula, data).fit()
    return model
model = forward_selected(d2, 'Profit')
print(model.model.formula)
print(model.rsquared_adj)
model.summary()
d4 = pd.read_csv('C:/Users/HOMEPCUSER/Desktop/Spring 19/Machine_Learning/Propose-Salaries-Polynomial.csv')
print(d4)
d4.shape
d4.dtypes
print(d4.columns)
d4['Level2'] = np.power(d4[['Level']],2)
X = d4[['Level','Level2']]
X = sm.add_constant(X)
Y = d4[['Salary']]
from pandas.plotting import scatter_matrix
scatter_matrix(d4, figsize=(4, 4), diagonal='kde',color = 'r')
lm = sm.OLS(Y, X).fit()
lm.summary()
lm.params
x0 = pd.DataFrame([{"Const":1,"Level": 6.5, "Level2": np.power(6.5, 2)}])
lm.predict(x0)