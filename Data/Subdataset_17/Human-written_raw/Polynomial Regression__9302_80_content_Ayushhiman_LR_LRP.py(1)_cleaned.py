import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
customers = pd.read_csv("Ecommerce Customers")
customers.head()
customers.describe()
sns.set_palette("GnBu_d")
sns.set_style('whitegrid')
sns.jointplot(x='Time on Website',y='Yearly Amount Spent',data=customers)
sns.jointplot(x='Time on App',y='Yearly Amount Spent',data=customers)
sns.jointplot(x='Time on App',y='Length of Membership',kind='hex',data=customers)
sns.pairplot(customers)
sns.lmplot(x='Length of Membership',y='Yearly Amount Spent',data=customers)
y = customers['Yearly Amount Spent']
X = customers[['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership']]
from sklearn.preprocessing import PolynomialFeatures
l=PolynomialFeatures(degree=2, interaction_only=False, include_bias=True)
X2=l.fit_transform(X)
from sklearn.feature_selection import f_regression
print(f_regression(X, y, center=True))
from sklearn.feature_selection import mutual_info_regression
print(mutual_info_regression(X, y, discrete_features='auto', n_neighbors=3, copy=True, random_state=None))
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
X1=X.drop('Time on App',axis=1)
X1.head()
X1_train, X1_test, y_train, y_test = train_test_split(X1, y, test_size=0.3, random_state=101)
X2_train, X2_test, y_train, y_test = train_test_split(X2, y, test_size=0.3, random_state=101)
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm1=LinearRegression()
lm2=LinearRegression()
lm.fit(X_train,y_train)
lm1.fit(X1_train,y_train)
lm2.fit(X2_train,y_train)
print('Coefficients: \n', lm.coef_)
print('Coefficients: \n', lm1.coef_)
print('Coefficients: \n', lm2.coef_)
predictions = lm.predict( X_test)
p1=lm1.predict(X1_test)
p2=lm2.predict(X2_test)
plt.scatter(y_test,predictions)
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')
plt.scatter(y_test,p1)
plt.scatter(y_test,p2)
from sklearn import metrics
print('model 1')
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))
print('model2')
print('MAE:', metrics.mean_absolute_error(y_test, p1))
print('MSE:', metrics.mean_squared_error(y_test, p1))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, p1)))
print('model 3')
print('MAE:', metrics.mean_absolute_error(y_test, p2))
print('MSE:', metrics.mean_squared_error(y_test, p2))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, p2)))