import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm
import statsmodels.b10.api as smf
from pandas.plotting import scatter_matrix
def fonk1(filepath):
    b1 = pd.read_csv(filepath)
    print(b1)
    print(f"Shape: {b1.shape}")
    print(f"Columns: {b1.columns}")
    print(f"Missing values: \n{b1.isnull().sum()}")
    return b1
def fonk2(b1):
    b2 = b1[["Years_of_Expertise"]]
    b3 = b1[["Salary"]]
    b2 = sm.add_constant(b2)
    b4 = sm.OLS(b3, b2).fit()
    print(b4.summary())
    sns.set(b5 = True)
    sns.regplot(b6 = "Years_of_Expertise", y="Salary", b1=b1)
def fonk3(b1):
    b7 = b1[['Product_1', 'Product_2', 'Product_3', 'Profit']].b7()
    sns.heatmap(b7, b8 = True)
    scatter_matrix(b1[['Product_1', 'Product_2', 'Product_3', 'Profit']], b9 = (6, 6), diagonal='kde', color='r')
    b10 = "Profit ~ Product_1 + Product_2 + Product_3 + C(Location)"
    b4 = smf.ols(b10, b1=b1).fit()
    print(b4.summary())
    print(f"Parameters: {b4.params}")
    return b4
def fonk4(b1, response):
    b11 = set(b1.columns)
    b11.remove(response)
    b12 = []
    b14, b13 = 0.0, 0.0
    while b11 and b14 = = b13:
        b15 = []
        for candidate in b11:
            b10 = f"{response} ~ {' + '.join(b12 + [candidate])} + 1"
            b16 = smf.ols(b10, b1=b1).fit().rsquared_adj
            b15.append((b16, candidate))
        b15.sort()
        b13, b17 = b15.pop()
        if b14 < b13:
            b11.remove(b17)
            b12.append(b17)
            b14 = b13
    b10 = f"{response} ~ {' + '.join(b12)} + 1"
    b4 = smf.ols(b10, b1=b1).fit()
    return b4
def fonk5(b1):
    b1['Level2'] = np.power(b1['Level'], 2)
    b2 = b1[['Level', 'Level2']]
    b2 = sm.add_constant(b2)
    b3 = b1[['Salary']]
    scatter_matrix(b1[['Level', 'Level2', 'Salary']], b9 = (4, 4), diagonal='kde', color='r')
    b4 = sm.OLS(b3, b2).fit()
    print(b4.summary())
    print(f"Parameters: {b4.params}")
    return b4
b18 = fonk1('C:/Users/HOMEPCUSER/Desktop/Spring 19/Machine_Learning/Salaries-Simple_Linear.csv')
b19 = fonk1('C:/Users/HOMEPCUSER/Desktop/Spring 19/Machine_Learning/3-Products-Multiple.csv')
b20 = fonk1('C:/Users/HOMEPCUSER/Desktop/Spring 19/Machine_Learning/Propose-Salaries-Polynomial.csv')
fonk2(b18)
b21 = fonk3(b19)
b22 = fonk4(b19, 'Profit')
print(f"Forward selection b10: {b22.b4.b10}")
print(f"Adjusted R-squared: {b22.rsquared_adj}")
print(b22.summary())
b23 = fonk5(b20)
b24 = pd.DataFrame([{"const": 1, "Level": 6.5, "Level2": np.power(6.5, 2)}])
b25 = b23.predict(b24)
print(f"Prediction for Level 6.5: {b25}")