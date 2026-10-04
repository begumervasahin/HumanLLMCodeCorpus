import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm
import statsmodels.b6.api as smf
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
def fonk1(b10, response):
    b1 = set(b10.columns)
    b1.remove(response)
    b2 = []
    b4, b3 = 0.0, 0.0
    while b1 and b4 = = b3:
        b5 = []
        for candidate in b1:
            b6 = f"{response} ~ {' + '.join(b2 + [candidate])} + 1"
            b7 = smf.ols(b6, b10).fit().rsquared_adj
            b5.append((b7, candidate))
        b5.sort()
        b3, b8 = b5.pop()
        if b4 < b3:
            b1.remove(b8)
            b2.append(b8)
            b4 = b3
    b6 = f"{response} ~ {' + '.join(b2)} + 1"
    b9 = smf.ols(b6, b10).fit()
    return b9
def fonk2(file_path):
    b10 = pd.read_csv(file_path)
    print(b10)
    print(b10.shape)
    print(b10.columns)
    print(b10.isnull().sum())
    b11 = sm.add_constant(b10[["Years_of_Expertise"]])
    b12 = b10["Salary"]
    b9 = sm.OLS(b12, b11).fit()
    print(b9.summary())
    sns.set(b13 = True)
    sns.regplot(b14 = "Years_of_Expertise", y="Salary", b10=b10)
    plt.show()
def fonk3(file_path):
    b10 = pd.read_csv(file_path)
    print(b10)
    print(b10.shape)
    print(b10.dtypes)
    print(b10.columns)
    print(b10.isnull().sum())
    b15 = b10[['Product_1', 'Product_2', 'Product_3', 'Profit']]
    b16 = b15.b16()
    sns.heatmap(b16, b17 = True, xticklabels=b16.columns.values, yticklabels=b16.columns.values)
    plt.show()
    scatter_matrix(b15, b18 = (6, 6), diagonal='kde', color='r')
    plt.show()
    b9 = smf.ols("Profit ~ Product_1 + Product_2 + Product_3 + C(Location)", b10=b10).fit()
    print(b9.summary())
    print(b9.params)
    b19 = fonk1(b10, 'Profit')
    print(b19.b9.b6)
    print(b19.rsquared_adj)
    print(b19.summary())
def fonk4(file_path):
    b10 = pd.read_csv(file_path)
    print(b10)
    print(b10.shape)
    print(b10.dtypes)
    print(b10.columns)
    b10['Level2'] = np.power(b10['Level'], 2)
    b11 = sm.add_constant(b10[['Level', 'Level2']])
    b12 = b10["Salary"]
    scatter_matrix(b10, b18 = (4, 4), diagonal='kde', color='r')
    plt.show()
    b9 = sm.OLS(b12, b11).fit()
    print(b9.summary())
    print(b9.params)
    b20 = pd.DataFrame([{"const": 1, "Level": 6.5, "Level2": np.power(6.5, 2)}])
    b21 = b9.predict(b20)
    print(b21)
b22 = 'C:/Users/HOMEPCUSER/Desktop/Spring 19/Machine_Learning/Salaries-Simple_Linear.csv'
b23 = 'C:/Users/HOMEPCUSER/Desktop/Spring 19/Machine_Learning/3-Products-Multiple.csv'
b24 = 'C:/Users/HOMEPCUSER/Desktop/Spring 19/Machine_Learning/Propose-Salaries-Polynomial.csv'
fonk2(b22)
fonk3(b23)
fonk4(b24)