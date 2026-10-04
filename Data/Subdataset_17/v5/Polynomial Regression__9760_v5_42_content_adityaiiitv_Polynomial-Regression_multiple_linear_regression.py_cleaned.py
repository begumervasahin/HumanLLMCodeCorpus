import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder()
X = onehotencoder.fit_transform(X).toarray()
X = X[:, 1:]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
X = np.append(arr=np.ones((X.shape[0], 1)).astype(int), values=X, axis=1)
def backward_elimination(X, y, sl):
    num_vars = len(X[0])
    for i in range(num_vars):
        regressor_OLS = sm.OLS(y, X).fit()
        max_p_value = max(regressor_OLS.pvalues).astype(float)
        if max_p_value > sl:
            for j in range(num_vars - i):
                if regressor_OLS.pvalues[j].astype(float) == max_p_value:
                    X = np.delete(X, j, 1)
    regressor_OLS.summary()
    return X
SL = 0.05
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
X_Modeled = backward_elimination(X_opt, y, SL)
regressor_OLS = sm.OLS(endog=y, exog=X_Modeled).fit()
print(regressor_OLS.summary())