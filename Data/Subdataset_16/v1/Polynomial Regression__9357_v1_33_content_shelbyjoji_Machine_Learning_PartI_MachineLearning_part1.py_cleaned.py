import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm
import statsmodels.b18.api as smf
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
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
sns.regplot(b6 = "Years_of_Expertise", y="Salary", data=b1)
plt.show()
b7 = pd.read_csv('C:/Users/HOMEPCUSER/Desktop/Spring 19/Machine_Learning/3-Products-Multiple.csv')
print(b7)
print(b7.shape)
print(b7.dtypes)
print(b7.columns)
print(b7.isnull().sum())
b8 = b7[['Product_1', 'Product_2', 'Product_3', 'Profit']]
b9 = b8.b9()
sns.heatmap(b9, b10 = True, xticklabels=b9.columns.values, yticklabels=b9.columns.values)
plt.show()
scatter_matrix(b8, b11 = (6, 6), diagonal='kde', color='r')
plt.show()
b12 = smf.ols("Profit ~ Product_1 + Product_2 + Product_3 + C(Location)", data=b7).fit()
print(b12.summary())
print(b12.params)
def fonk1(data, response):
    b13 = set(data.columns)
    b13.remove(response)
    b14 = []
    b16, b15 = 0.0, 0.0
    while b13 and b16 = = b15:
        b17 = []
        for candidate in b13:
            b18 = "{} ~ {} + 1".format(response, ' + '.join(b14 + [candidate]))
            b19 = smf.ols(b18, data).fit().rsquared_adj
            b17.append((b19, candidate))
        b17.sort()
        b15, b20 = b17.pop()
        if b16 < b15:
            b13.remove(b20)
            b14.append(b20)
            b16 = b15
    b18 = "{} ~ {} + 1".format(response, ' + '.join(b14))
    b4 = smf.ols(b18, data).fit()
    return b4
b4 = fonk1(b7, 'Profit')
print(b4.b4.b18)
print(b4.rsquared_adj)
print(b4.summary())
b21 = pd.read_csv('C:/Users/HOMEPCUSER/Desktop/Spring 19/Machine_Learning/Propose-Salaries-Polynomial.csv')
print(b21)
print(b21.shape)
print(b21.dtypes)
print(b21.columns)
b21['Level2'] = np.power(b21['Level'], 2)
b2 = b21[['Level', 'Level2']]
b2 = sm.add_constant(b2)
b3 = b21[['Salary']]
scatter_matrix(b21, b11 = (4, 4), diagonal='kde', color='r')
plt.show()
b22 = sm.OLS(b3, b2).fit()
print(b22.summary())
print(b22.params)
b23 = pd.DataFrame([{"const": 1, "Level": 6.5, "Level2": np.power(6.5, 2)}])
print(b22.predict(b23))