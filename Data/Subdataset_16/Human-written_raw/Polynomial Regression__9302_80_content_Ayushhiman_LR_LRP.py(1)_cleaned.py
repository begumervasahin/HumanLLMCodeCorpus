import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
b1 = pd.read_csv("Ecommerce Customers")
b1.head()
b1.describe()
sns.set_palette("GnBu_d")
sns.set_style('whitegrid')
sns.jointplot(b2 = 'Time on Website',b3='Yearly Amount Spent',data=b1)
sns.jointplot(b2 = 'Time on App',b3='Yearly Amount Spent',data=b1)
sns.jointplot(b2 = 'Time on App',b3='Length of Membership',kind='hex',data=b1)
sns.pairplot(b1)
sns.lmplot(b2 = 'Length of Membership',b3='Yearly Amount Spent',data=b1)
b3 = b1['Yearly Amount Spent']
b4 = b1[['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership']]
from sklearn.preprocessing import PolynomialFeatures
b5 = PolynomialFeatures(degree=2, interaction_only=False, include_bias=True)
b6 = b5.fit_transform(b4)
from sklearn.feature_selection import f_regression
print(f_regression(b4, b3, b7 = True))
from sklearn.feature_selection import mutual_info_regression
print(mutual_info_regression(b4, b3, b8 = 'auto', n_neighbors=3, copy=True, random_state=None))
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, b9 = train_test_split(b4, b3, test_size=0.3, random_state=101)
b10 = b4.drop('Time on App',axis=1)
b10.head()
X1_train, X1_test, y_train, b9 = train_test_split(b10, b3, test_size=0.3, random_state=101)
X2_train, X2_test, y_train, b9 = train_test_split(b6, b3, test_size=0.3, random_state=101)
from sklearn.linear_model import LinearRegression
b11 = LinearRegression()
b12 = LinearRegression()
b13 = LinearRegression()
b11.fit(X_train,y_train)
b12.fit(X1_train,y_train)
b13.fit(X2_train,y_train)
print('Coefficients: \n', b11.coef_)
print('Coefficients: \n', b12.coef_)
print('Coefficients: \n', b13.coef_)
b14 = b11.predict( X_test)
b15 = b12.predict(X1_test)
b16 = b13.predict(X2_test)
plt.scatter(b9,b14)
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')
plt.scatter(b9,b15)
plt.scatter(b9,b16)
from sklearn import metrics
print('model 1')
print('MAE:', metrics.mean_absolute_error(b9, b14))
print('MSE:', metrics.mean_squared_error(b9, b14))
print('RMSE:', np.sqrt(metrics.mean_squared_error(b9, b14)))
print('model2')
print('MAE:', metrics.mean_absolute_error(b9, b15))
print('MSE:', metrics.mean_squared_error(b9, b15))
print('RMSE:', np.sqrt(metrics.mean_squared_error(b9, b15)))
print('model 3')
print('MAE:', metrics.mean_absolute_error(b9, b16))
print('MSE:', metrics.mean_squared_error(b9, b16))
print('RMSE:', np.sqrt(metrics.mean_squared_error(b9, b16)))