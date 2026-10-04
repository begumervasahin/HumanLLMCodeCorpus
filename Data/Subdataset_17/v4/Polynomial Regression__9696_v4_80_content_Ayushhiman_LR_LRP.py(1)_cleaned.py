import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
from sklearn.feature_selection import f_regression, mutual_info_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
customers = pd.read_csv("Ecommerce Customers")
print(customers.head())
print(customers.describe())
sns.set_palette("GnBu_d")
sns.set_style('whitegrid')
sns.jointplot(x='Time on Website', y='Yearly Amount Spent', data=customers)
sns.jointplot(x='Time on App', y='Yearly Amount Spent', data=customers)
sns.jointplot(x='Time on App', y='Length of Membership', kind='hex', data=customers)
sns.pairplot(customers)
sns.lmplot(x='Length of Membership', y='Yearly Amount Spent', data=customers)
y = customers['Yearly Amount Spent']
X = customers[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
poly = PolynomialFeatures(degree=2, interaction_only=False, include_bias=True)
X_poly = poly.fit_transform(X)
f_values, p_values = f_regression(X, y, center=True)
print(f"f_regression: f-values={f_values}, p-values={p_values}")
mi_values = mutual_info_regression(X, y)
print(f"mutual_info_regression: MI values={mi_values}")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
X1 = X.drop('Time on App', axis=1)
X1_train, X1_test, y_train, y_test = train_test_split(X1, y, test_size=0.3, random_state=101)
X2_train, X2_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.3, random_state=101)
lm = LinearRegression()
lm1 = LinearRegression()
lm2 = LinearRegression()
lm.fit(X_train, y_train)
lm1.fit(X1_train, y_train)
lm2.fit(X2_train, y_train)
print('Model 1 Coefficients:', lm.coef_)
print('Model 2 Coefficients:', lm1.coef_)
print('Model 3 Coefficients:', lm2.coef_)
predictions = lm.predict(X_test)
p1 = lm1.predict(X1_test)
p2 = lm2.predict(X2_test)
plt.figure(figsize=(10,6))
plt.scatter(y_test, predictions, label='Model 1')
plt.scatter(y_test, p1, label='Model 2')
plt.scatter(y_test, p2, label='Model 3')
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')
plt.legend()
plt.show()
def print_metrics(model_name, y_test, y_pred):
    print(f'{model_name}')
    print('MAE:', metrics.mean_absolute_error(y_test, y_pred))
    print('MSE:', metrics.mean_squared_error(y_test, y_pred))
    print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
    print('\n')
print_metrics('Model 1', y_test, predictions)
print_metrics('Model 2', y_test, p1)
print_metrics('Model 3', y_test, p2)