import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler, PolynomialFeatures
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
dataset = pd.read_csv('insurance.csv')
X = dataset.iloc[:, :5].values
y = dataset.iloc[:, 6].values
labelencoder = LabelEncoder()
X[:, 1] = labelencoder.fit_transform(X[:, 1])
X[:, 4] = labelencoder.fit_transform(X[:, 4])
onehotencoder = OneHotEncoder(categorical_features=[1, 4])
X = onehotencoder.fit_transform(X).toarray()
X = X[:, [1, 3, 4, 5, 6]]
scaler_X = StandardScaler()
X = scaler_X.fit_transform(X)
scaler_y = StandardScaler()
y = scaler_y.fit_transform(y.reshape(-1, 1))
poly_features = PolynomialFeatures(degree=4)
X_poly = poly_features.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=0)
lasso_regressor = Lasso(alpha=0.01, fit_intercept=False)
lasso_regressor.fit(X_train, y_train)
y_train_pred = lasso_regressor.predict(X_train)
y_train_pred = scaler_y.inverse_transform(y_train_pred)
y_train = scaler_y.inverse_transform(y_train)
y_test_pred = lasso_regressor.predict(X_test)
y_test_pred = scaler_y.inverse_transform(y_test_pred)
y_test = scaler_y.inverse_transform(y_test)
r2_score_train = r2_score(y_train, y_train_pred) * 100
r2_score_test = r2_score(y_test, y_test_pred) * 100
print(f'R2 Score for Training Set: {r2_score_train:.2f}%')
print(f'R2 Score for Testing Set: {r2_score_test:.2f}%')
plt.scatter(y_test, y_test_pred, color='blue', label='Predicted vs Actual')
plt.xlabel('Actual values')
plt.ylabel('Predicted values')
plt.title('Lasso Regression Predicted vs Actual')
plt.legend()
plt.show()