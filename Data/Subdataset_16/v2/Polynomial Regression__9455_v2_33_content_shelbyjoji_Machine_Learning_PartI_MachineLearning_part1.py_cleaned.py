import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm
import statsmodels.b6.api as smf
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
def fonk1(data, response):
    b1 = set(data.columns)
    b1.remove(response)
    b2 = []
    b4, b3 = 0.0, 0.0
    while b1 and b4 = = b3:
        b5 = []
        for candidate in b1:
            b6 = f"{response} ~ {' + '.join(b2 + [candidate])} + 1"
            b7 = smf.ols(b6, data).fit().rsquared_adj
            b5.append((b7, candidate))
        b5.sort()
        b3, b8 = b5.pop()
        if b4 < b3:
            b1.remove(b8)
            b2.append(b8)
            b4 = b3
    b6 = f"{response} ~ {' + '.join(b2)} + 1"
    b9 = smf.ols(b6, data).fit()
    return b9
b10 = pd.read_csv('C:/Users/HOMEPCUSER/Desktop/Spring 19/Machine_Learning/Salaries-Simple_Linear.csv')
print(b10)
print(b10.shape)
print(b10.columns)
print(b10.isnull().sum())
b11 = sm.add_constant(b10[["Years_of_Expertise"]])
b12 = b10["Salary"]
b13 = sm.OLS(b12, b11).fit()
print(b13.summary())
sns.set(b14 = True)
sns.regplot(b15 = "Years_of_Expertise", y="Salary", data=b10)
plt.show()
b16 = pd.read_csv('C:/Users/HOMEPCUSER/Desktop/Spring 19/Machine_Learning/3-Products-Multiple.csv')
print(b16)
print(b16.shape)
print(b16.dtypes)
print(b16.columns)
print(b16.isnull().sum())
b17 = b16[['Product_1', 'Product_2', 'Product_3', 'Profit']]
b18 = b17.b18()
sns.heatmap(b18, b19 = True, xticklabels=b18.columns.values, yticklabels=b18.columns.values)
plt.show()
scatter_matrix(b17, b20 = (6, 6), diagonal='kde', color='r')
plt.show()
b21 = smf.ols("Profit ~ Product_1 + Product_2 + Product_3 + C(Location)", data=b16).fit()
print(b21.summary())
print(b21.params)
b22 = fonk1(b16, 'Profit')
print(b22.b9.b6)
print(b22.rsquared_adj)
print(b22.summary())
b23 = pd.read_csv('C:/Users/HOMEPCUSER/Desktop/Spring 19/Machine_Learning/Propose-Salaries-Polynomial.csv')
print(b23)
print(b23.shape)
print(b23.dtypes)
print(b23.columns)
b23['Level2'] = np.power(b23['Level'], 2)
b24 = sm.add_constant(b23[['Level', 'Level2']])
b25 = b23["Salary"]
scatter_matrix(b23, b20 = (4, 4), diagonal='kde', color='r')
plt.show()
b26 = sm.OLS(b25, b24).fit()
print(b26.summary())
print(b26.params)
b27 = pd.DataFrame([{"const": 1, "Level": 6.5, "Level2": np.power(6.5, 2)}])
print(b26.predict(b27))