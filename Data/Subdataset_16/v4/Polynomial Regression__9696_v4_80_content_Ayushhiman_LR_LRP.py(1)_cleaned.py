import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
from sklearn.feature_selection import f_regression, mutual_info_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
b1 = pd.read_csv("Ecommerce Customers")
print(b1.head())
print(b1.describe())
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
f_values, b7 = f_regression(b4, b3, center=True)
print(f"f_regression: f-b8 = {f_values}, p-b8={b7}")
b9 = mutual_info_regression(b4, b3)
print(f"mutual_info_regression: MI b8 = {b9}")
X_train, X_test, y_train, b10 = train_test_split(b4, b3, test_size=0.3, random_state=101)
b11 = b4.drop('Time on App', axis=1)
X1_train, X1_test, y_train, b10 = train_test_split(b11, b3, test_size=0.3, random_state=101)
X2_train, X2_test, y_train, b10 = train_test_split(b6, b3, test_size=0.3, random_state=101)
b12 = LinearRegression()
b13 = LinearRegression()
b14 = LinearRegression()
b12.fit(X_train, y_train)
b13.fit(X1_train, y_train)
b14.fit(X2_train, y_train)
print('Model 1 Coefficients:', b12.coef_)
print('Model 2 Coefficients:', b13.coef_)
print('Model 3 Coefficients:', b14.coef_)
b15 = b12.predict(X_test)
b16 = b13.predict(X1_test)
b17 = b14.predict(X2_test)
plt.figure(b18 = (10,6))
plt.scatter(b10, b15, b19 = 'Model 1')
plt.scatter(b10, b16, b19 = 'Model 2')
plt.scatter(b10, b17, b19 = 'Model 3')
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')
plt.legend()
plt.show()
def fonk1(model_name, b10, y_pred):
    print(f'{model_name}')
    print('MAE:', metrics.mean_absolute_error(b10, y_pred))
    print('MSE:', metrics.mean_squared_error(b10, y_pred))
    print('RMSE:', np.sqrt(metrics.mean_squared_error(b10, y_pred)))
    print('\n')
fonk1('Model 1', b10, b15)
fonk1('Model 2', b10, b16)
fonk1('Model 3', b10, b17)