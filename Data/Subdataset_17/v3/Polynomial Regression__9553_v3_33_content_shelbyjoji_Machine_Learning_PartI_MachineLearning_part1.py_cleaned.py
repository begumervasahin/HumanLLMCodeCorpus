import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
def forward_selected(data, response):
    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score, best_new_score = 0.0, 0.0
    while remaining and current_score == best_new_score:
        scores_with_candidates = []
        for candidate in remaining:
            formula = f"{response} ~ {' + '.join(selected + [candidate])} + 1"
            score = smf.ols(formula, data).fit().rsquared_adj
            scores_with_candidates.append((score, candidate))
        scores_with_candidates.sort()
        best_new_score, best_candidate = scores_with_candidates.pop()
        if current_score < best_new_score:
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score
    formula = f"{response} ~ {' + '.join(selected)} + 1"
    model = smf.ols(formula, data).fit()
    return model
def analyze_simple_linear_regression(file_path):
    data = pd.read_csv(file_path)
    print(data)
    print(data.shape)
    print(data.columns)
    print(data.isnull().sum())
    X = sm.add_constant(data[["Years_of_Expertise"]])
    Y = data["Salary"]
    model = sm.OLS(Y, X).fit()
    print(model.summary())
    sns.set(color_codes=True)
    sns.regplot(x="Years_of_Expertise", y="Salary", data=data)
    plt.show()
def analyze_multiple_linear_regression(file_path):
    data = pd.read_csv(file_path)
    print(data)
    print(data.shape)
    print(data.dtypes)
    print(data.columns)
    print(data.isnull().sum())
    selected_data = data[['Product_1', 'Product_2', 'Product_3', 'Profit']]
    corr = selected_data.corr()
    sns.heatmap(corr, annot=True, xticklabels=corr.columns.values, yticklabels=corr.columns.values)
    plt.show()
    scatter_matrix(selected_data, figsize=(6, 6), diagonal='kde', color='r')
    plt.show()
    model = smf.ols("Profit ~ Product_1 + Product_2 + Product_3 + C(Location)", data=data).fit()
    print(model.summary())
    print(model.params)
    forward_model = forward_selected(data, 'Profit')
    print(forward_model.model.formula)
    print(forward_model.rsquared_adj)
    print(forward_model.summary())
def analyze_polynomial_regression(file_path):
    data = pd.read_csv(file_path)
    print(data)
    print(data.shape)
    print(data.dtypes)
    print(data.columns)
    data['Level2'] = np.power(data['Level'], 2)
    X = sm.add_constant(data[['Level', 'Level2']])
    Y = data["Salary"]
    scatter_matrix(data, figsize=(4, 4), diagonal='kde', color='r')
    plt.show()
    model = sm.OLS(Y, X).fit()
    print(model.summary())
    print(model.params)
    prediction_input = pd.DataFrame([{"const": 1, "Level": 6.5, "Level2": np.power(6.5, 2)}])
    prediction = model.predict(prediction_input)
    print(prediction)
file_path1 = 'C:/Users/HOMEPCUSER/Desktop/Spring 19/Machine_Learning/Salaries-Simple_Linear.csv'
file_path2 = 'C:/Users/HOMEPCUSER/Desktop/Spring 19/Machine_Learning/3-Products-Multiple.csv'
file_path3 = 'C:/Users/HOMEPCUSER/Desktop/Spring 19/Machine_Learning/Propose-Salaries-Polynomial.csv'
analyze_simple_linear_regression(file_path1)
analyze_multiple_linear_regression(file_path2)
analyze_polynomial_regression(file_path3)