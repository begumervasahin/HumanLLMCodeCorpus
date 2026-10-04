import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
b1 = pd.read_csv('50_Startups.csv')
b2 = b1.iloc[:, :-1].values
b3 = b1.iloc[:, 4].values
b4 = LabelEncoder()
b2[:, 3] = b4.fit_transform(b2[:, 3])
b5 = OneHotEncoder()
b2 = b5.fit_transform(b2).toarray()
b2 = b2[:, 1:]
X_train, X_test, y_train, b6 = train_test_split(b2, b3, test_size=0.2, random_state=0)
b7 = LinearRegression()
b7.fit(X_train, y_train)
b8 = b7.predict(X_test)
b2 = np.append(arr=np.ones((50, 1)).astype(int), values=b2, axis=1)
def fonk1(b14, sl):
    b9 = len(b14[0])
    b10 = np.zeros((50, 6)).astype(int)
    for i in range(b9):
        b11 = sm.OLS(b3, b14).fit()
        b12 = max(b11.pvalues).astype(float)
        b13 = b11.rsquared_adj.astype(float)
        if b12 > sl:
            for j in range(b9 - i):
                if (b11.pvalues[j].astype(float) == b12):
                    b10[:, j] = b14[:, j]
                    b14 = np.delete(b14, j, 1)
                    b15 = sm.OLS(b3, b14).fit()
                    b16 = b15.rsquared_adj.astype(float)
                    if (b13 >= b16):
                        b17 = np.hstack((b14, b10[:, [0, j]]))
                        b17 = np.delete(b17, j, 1)
                        return b17
    b11.summary()
    return b14
a1 = 0.05
b18 = b2[:, [0, 1, 2, 3, 4, 5]]
b19 = fonk1(b18, a1)
b11 = sm.OLS(endog=b3, exog=b19).fit()
print(b11.summary())