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
def fonk1(b3, b4, b2 = 'scatter', **kwargs):
    sns.jointplot(b3 = b3, b4=b4, data=b1, b2=b2, **kwargs)
fonk1(b3 = 'Time on Website', b4='Yearly Amount Spent')
fonk1(b3 = 'Time on App', b4='Yearly Amount Spent')
fonk1(b3 = 'Time on App', b4='Length of Membership', b2='hex')
sns.pairplot(b1)
sns.lmplot(b3 = 'Length of Membership', b4='Yearly Amount Spent', data=b1)
b4 = b1['Yearly Amount Spent']
b5 = b1[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
b6 = PolynomialFeatures(degree=2, include_bias=True)
b7 = b6.fit_transform(b5)
f_values, b8 = f_regression(b5, b4, center=True)
print(f"f_regression: f-b9 = {f_values}, p-b9={b8}")
b10 = mutual_info_regression(b5, b4)
print(f"mutual_info_regression: MI b9 = {b10}")
def fonk2(b5):
    return train_test_split(b5, b4, b11 = 0.3, random_state=101)
X_train, X_test, y_train, b12 = fonk2(b5)
b13 = b5.drop('Time on App', axis=1)
X1_train, X1_test, y_train, b12 = fonk2(b13)
X2_train, X2_test, y_train, b12 = fonk2(b7)
def fonk3(X_train, y_train):
    b14 = LinearRegression()
    b14.fit(X_train, y_train)
    return b14
b15 = fonk3(X_train, y_train)
b16 = fonk3(X1_train, y_train)
b17 = fonk3(X2_train, y_train)
def fonk4(model_name, b14):
    print(f'{model_name} Coefficients:', b14.coef_)
fonk4('Model 1', b15)
fonk4('Model 2', b16)
fonk4('Model 3', b17)
b18 = b15.predict(X_test)
b19 = b16.predict(X1_test)
b20 = b17.predict(X2_test)
def fonk5(b12, b18, model_name):
    plt.scatter(b12, b18, b21 = model_name)
plt.figure(b22 = (10, 6))
fonk5(b12, b18, 'Model 1')
fonk5(b12, b19, 'Model 2')
fonk5(b12, b20, 'Model 3')
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')
plt.legend()
plt.show()
def fonk6(model_name, b12, y_pred):
    print(f'{model_name}')
    print('MAE:', metrics.mean_absolute_error(b12, y_pred))
    print('MSE:', metrics.mean_squared_error(b12, y_pred))
    print('RMSE:', np.sqrt(metrics.mean_squared_error(b12, y_pred)))
    print('\n')
fonk6('Model 1', b12, b18)
fonk6('Model 2', b12, b19)
fonk6('Model 3', b12, b20)