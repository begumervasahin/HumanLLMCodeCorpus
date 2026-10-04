import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
from sklearn.feature_selection import f_regression, mutual_info_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
b1 = pd.read_csv("Ecommerce Customers.csv")
sns.set_palette("GnBu_d")
sns.set_style('whitegrid')
sns.jointplot(b2 = 'Time on Website', b3='Yearly Amount Spent', data=b1)
sns.jointplot(b2 = 'Time on App', b3='Yearly Amount Spent', data=b1)
sns.jointplot(b2 = 'Time on App', b3='Length of Membership', kind='hex', data=b1)
sns.pairplot(b1)
sns.lmplot(b2 = 'Length of Membership', b3='Yearly Amount Spent', data=b1)
b3 = b1['Yearly Amount Spent']
b4 = b1[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
b5 = PolynomialFeatures(degree=2, interaction_only=False, include_bias=True)
b6 = b5.fit_transform(b4)
f_scores, b7 = f_regression(b4, b3, center=True)
b8 = mutual_info_regression(b4, b3, discrete_features='auto', n_neighbors=3, copy=True, random_state=None)
print("F-regression scores:", f_scores)
print("Mutual Information Regression scores:", b8)
X_train, X_test, y_train, b9 = train_test_split(b4, b3, test_size=0.3, random_state=101)
b10 = b4.drop('Time on App', axis=1)
X_reduced_train, X_reduced_test, b11, b11 = train_test_split(b10, b3, test_size=0.3, random_state=101)
X_poly_train, X_poly_test, b11, b11 = train_test_split(b6, b3, test_size=0.3, random_state=101)
b12 = LinearRegression()
b13 = LinearRegression()
b14 = LinearRegression()
b12.fit(X_train, y_train)
b13.fit(X_reduced_train, y_train)
b14.fit(X_poly_train, y_train)
print('Coefficients for model with all features: \n', b12.coef_)
print('Coefficients for model without Time on App: \n', b13.coef_)
print('Coefficients for model with polynomial features: \n', b14.coef_)
b15 = b12.predict(X_test)
b16 = b13.predict(X_reduced_test)
b17 = b14.predict(X_poly_test)
plt.figure(b18 = (10, 6))
plt.scatter(b9, b15, b19 = 'Model with all features')
plt.scatter(b9, b16, b19 = 'Model without Time on App')
plt.scatter(b9, b17, b19 = 'Model with polynomial features')
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')
plt.legend()
plt.show()
def fonk1(y_true, y_pred, model_name):
    print(f'{model_name}')
    print('MAE:', metrics.mean_absolute_error(y_true, y_pred))
    print('MSE:', metrics.mean_squared_error(y_true, y_pred))
    print('RMSE:', np.sqrt(metrics.mean_squared_error(y_true, y_pred)))
    print()
fonk1(b9, b15, 'Model with all features')
fonk1(b9, b16, 'Model without Time on App')
fonk1(b9, b17, 'Model with polynomial features')