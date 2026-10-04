import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
from sklearn.feature_selection import f_regression, mutual_info_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
customers = pd.read_csv("Ecommerce Customers.csv")
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
f_scores, p_values = f_regression(X, y, center=True)
mi_scores = mutual_info_regression(X, y, discrete_features='auto', n_neighbors=3, copy=True, random_state=None)
print("F-regression scores:", f_scores)
print("Mutual Information Regression scores:", mi_scores)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
X_reduced = X.drop('Time on App', axis=1)
X_reduced_train, X_reduced_test, _, _ = train_test_split(X_reduced, y, test_size=0.3, random_state=101)
X_poly_train, X_poly_test, _, _ = train_test_split(X_poly, y, test_size=0.3, random_state=101)
lm = LinearRegression()
lm_reduced = LinearRegression()
lm_poly = LinearRegression()
lm.fit(X_train, y_train)
lm_reduced.fit(X_reduced_train, y_train)
lm_poly.fit(X_poly_train, y_train)
print('Coefficients for model with all features: \n', lm.coef_)
print('Coefficients for model without Time on App: \n', lm_reduced.coef_)
print('Coefficients for model with polynomial features: \n', lm_poly.coef_)
predictions = lm.predict(X_test)
predictions_reduced = lm_reduced.predict(X_reduced_test)
predictions_poly = lm_poly.predict(X_poly_test)
plt.figure(figsize=(10, 6))
plt.scatter(y_test, predictions, label='Model with all features')
plt.scatter(y_test, predictions_reduced, label='Model without Time on App')
plt.scatter(y_test, predictions_poly, label='Model with polynomial features')
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')
plt.legend()
plt.show()
def print_metrics(y_true, y_pred, model_name):
    print(f'{model_name}')
    print('MAE:', metrics.mean_absolute_error(y_true, y_pred))
    print('MSE:', metrics.mean_squared_error(y_true, y_pred))
    print('RMSE:', np.sqrt(metrics.mean_squared_error(y_true, y_pred)))
    print()
print_metrics(y_test, predictions, 'Model with all features')
print_metrics(y_test, predictions_reduced, 'Model without Time on App')
print_metrics(y_test, predictions_poly, 'Model with polynomial features')