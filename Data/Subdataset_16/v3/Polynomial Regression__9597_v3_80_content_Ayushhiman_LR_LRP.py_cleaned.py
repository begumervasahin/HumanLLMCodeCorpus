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
def fonk1(data):
    sns.jointplot(b2 = 'Time on Website', b3='Yearly Amount Spent', data=data)
    sns.jointplot(b2 = 'Time on App', b3='Yearly Amount Spent', data=data)
    sns.jointplot(b2 = 'Time on App', b3='Length of Membership', kind='hex', data=data)
    sns.pairplot(data)
    sns.lmplot(b2 = 'Length of Membership', b3='Yearly Amount Spent', data=data)
fonk1(b1)
b3 = b1['Yearly Amount Spent']
b4 = b1[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
b5 = PolynomialFeatures(degree=2, interaction_only=False, include_bias=True)
b6 = b5.fit_transform(b4)
f_values, b7 = f_regression(b4, b3, center=True)
print("F-regression values:", f_values)
print("F-regression p-values:", b7)
b8 = mutual_info_regression(b4, b3, discrete_features='auto', n_neighbors=3, copy=True, random_state=None)
print("Mutual information scores:", b8)
X_train, X_test, y_train, b9 = train_test_split(b4, b3, test_size=0.3, random_state=101)
X_poly_train, b10 = train_test_split(b6, test_size=0.3, random_state=101)
b11 = b4.drop('Time on App', axis=1)
X_reduced_train, b12 = train_test_split(b11, test_size=0.3, random_state=101)
def fonk2(X_train, y_train):
    b13 = LinearRegression()
    b13.fit(X_train, y_train)
    return b13
b14 = fonk2(X_train, y_train)
b15 = fonk2(X_reduced_train, y_train)
b16 = fonk2(X_poly_train, y_train)
def fonk3(b13, name):
    print(f'{name} Coefficients:', b13.coef_)
fonk3(b14, 'Model with all features')
fonk3(b15, 'Model without "Time on App"')
fonk3(b16, 'Polynomial Features Model')
b17 = b14.predict(X_test)
b18 = b15.predict(b12)
b19 = b16.predict(b10)
def fonk4(b9, b17, title, subplot_position):
    plt.subplot(1, 3, subplot_position)
    plt.scatter(b9, b17)
    plt.xlabel('Y Test')
    plt.ylabel('Predicted Y')
    plt.title(title)
plt.figure(b20 = (14, 6))
fonk4(b9, b17, 'All Features', 1)
fonk4(b9, b18, 'Without "Time on App"', 2)
fonk4(b9, b19, 'Polynomial Features', 3)
plt.tight_layout()
plt.show()
def fonk5(model_name, b9, b17):
    print(f'{model_name} Model Performance:')
    print('MAE:', metrics.mean_absolute_error(b9, b17))
    print('MSE:', metrics.mean_squared_error(b9, b17))
    print('RMSE:', np.sqrt(metrics.mean_squared_error(b9, b17)))
    print('\n')
fonk5('All Features', b9, b17)
fonk5('Without "Time on App"', b9, b18)
fonk5('Polynomial Features', b9, b19)