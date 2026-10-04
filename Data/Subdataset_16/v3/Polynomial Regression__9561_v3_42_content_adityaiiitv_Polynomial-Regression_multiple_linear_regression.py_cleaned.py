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
b2 = np.append(arr=np.ones((b2.shape[0], 1)).astype(int), values=b2, axis=1)
def fonk1(b12, b3, sl):
    b9 = b12.shape[1]
    while b9 > 0:
        b10 = sm.OLS(b3, b12).fit()
        b11 = max(b10.pvalues).astype(float)
        if b11 > sl:
            for j in range(b9):
                if (b10.pvalues[j].astype(float) == b11):
                    b12 = np.delete(b12, j, 1)
                    b9 -= 1
        else:
            break
    b10.summary()
    return b12
a1 = 0.05
b13 = b2[:, [0, 1, 2, 3, 4, 5]]
b14 = fonk1(b13, b3, a1)
b10 = sm.OLS(endog=b3, exog=b14).fit()
print(b10.summary())