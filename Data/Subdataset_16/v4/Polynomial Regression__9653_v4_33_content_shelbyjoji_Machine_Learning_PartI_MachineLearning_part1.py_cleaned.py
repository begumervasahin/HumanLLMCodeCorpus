import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm
import statsmodels.b17.api as smf
from pandas.plotting import scatter_matrix
b1 = pd.read_csv('C:/Users/HOMEPCUSER/Desktop/Spring 19/Machine_Learning/Salaries-Simple_Linear.csv')
print(b1)
print(b1.shape)
print(b1.columns)
print(b1.isnull().sum())
b2 = b1[["Years_of_Expertise"]]
b3 = b1[["Salary"]]
b2 = sm.add_constant(b2)
b4 = sm.OLS(b3, b2).fit()
print(b4.summary())
sns.set(b5 = True)
sns.regplot(b2["Years_of_Expertise"], b3)
b6 = pd.read_csv('C:/Users/HOMEPCUSER/Desktop/Spring 19/Machine_Learning/3-Products-Multiple.csv')
print(b6)
print(b6.shape)
print(b6.dtypes)
print(b6.columns)
print(b6.isnull().sum())
b7 = b6[['Product_1', 'Product_2', 'Product_3', 'Profit']]
b8 = b7.b8()
sns.heatmap(b8, b9 = b8.columns.values, yticklabels=b8.columns.values)
scatter_matrix(b7, b10 = (6, 6), diagonal='kde', color='r')
b11 = smf.ols("Profit ~ Product_1 + Product_2 + Product_3 + C(Location)", data=b6).fit()
print(b11.summary())
print(b11.params)
def fonk1(data, response):
    b12 = set(data.columns)
    b12.remove(response)
    b13 = []
    b15, b14 = 0.0, 0.0
    while b12 and b15 = = b14:
        b16 = []
        for candidate in b12:
            b17 = "{} ~ {} + 1".format(response, ' + '.join(b13 + [candidate]))
            b18 = smf.ols(b17, data).fit().rsquared_adj
            b16.append((b18, candidate))
        b16.sort()
        b14, b19 = b16.pop()
        if b15 < b14:
            b12.remove(b19)
            b13.append(b19)
            b15 = b14
    b17 = "{} ~ {} + 1".format(response, ' + '.join(b13))
    b4 = smf.ols(b17, data).fit()
    return b4
b4 = fonk1(b6, 'Profit')
print(b4.b4.b17)
print(b4.rsquared_adj)
print(b4.summary())
b20 = pd.read_csv('C:/Users/HOMEPCUSER/Desktop/Spring 19/Machine_Learning/Propose-Salaries-Polynomial.csv')
print(b20)
print(b20.shape)
print(b20.dtypes)
print(b20.columns)
b20['Level2'] = np.power(b20['Level'], 2)
b2 = b20[['Level', 'Level2']]
b2 = sm.add_constant(b2)
b3 = b20[['Salary']]
scatter_matrix(b20, b10 = (4, 4), diagonal='kde', color='r')
b21 = sm.OLS(b3, b2).fit()
print(b21.summary())
print(b21.params)
b22 = pd.DataFrame([{"const": 1, "Level": 6.5, "Level2": np.power(6.5, 2)}])
print(b21.predict(b22))