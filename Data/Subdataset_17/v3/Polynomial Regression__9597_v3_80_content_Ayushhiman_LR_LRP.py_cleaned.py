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
def create_visualizations(data):
    sns.jointplot(x='Time on Website', y='Yearly Amount Spent', data=data)
    sns.jointplot(x='Time on App', y='Yearly Amount Spent', data=data)
    sns.jointplot(x='Time on App', y='Length of Membership', kind='hex', data=data)
    sns.pairplot(data)
    sns.lmplot(x='Length of Membership', y='Yearly Amount Spent', data=data)
create_visualizations(customers)
y = customers['Yearly Amount Spent']
X = customers[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
poly = PolynomialFeatures(degree=2, interaction_only=False, include_bias=True)
X_poly = poly.fit_transform(X)
f_values, p_values = f_regression(X, y, center=True)
print("F-regression values:", f_values)
print("F-regression p-values:", p_values)
mi_scores = mutual_info_regression(X, y, discrete_features='auto', n_neighbors=3, copy=True, random_state=None)
print("Mutual information scores:", mi_scores)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
X_poly_train, X_poly_test = train_test_split(X_poly, test_size=0.3, random_state=101)
X_reduced = X.drop('Time on App', axis=1)
X_reduced_train, X_reduced_test = train_test_split(X_reduced, test_size=0.3, random_state=101)
def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model
lm = train_model(X_train, y_train)
lm_reduced = train_model(X_reduced_train, y_train)
lm_poly = train_model(X_poly_train, y_train)
def print_coefficients(model, name):
    print(f'{name} Coefficients:', model.coef_)
print_coefficients(lm, 'Model with all features')
print_coefficients(lm_reduced, 'Model without "Time on App"')
print_coefficients(lm_poly, 'Polynomial Features Model')
predictions = lm.predict(X_test)
predictions_reduced = lm_reduced.predict(X_reduced_test)
predictions_poly = lm_poly.predict(X_poly_test)
def plot_predictions(y_test, predictions, title, subplot_position):
    plt.subplot(1, 3, subplot_position)
    plt.scatter(y_test, predictions)
    plt.xlabel('Y Test')
    plt.ylabel('Predicted Y')
    plt.title(title)
plt.figure(figsize=(14, 6))
plot_predictions(y_test, predictions, 'All Features', 1)
plot_predictions(y_test, predictions_reduced, 'Without "Time on App"', 2)
plot_predictions(y_test, predictions_poly, 'Polynomial Features', 3)
plt.tight_layout()
plt.show()
def evaluate_model(model_name, y_test, predictions):
    print(f'{model_name} Model Performance:')
    print('MAE:', metrics.mean_absolute_error(y_test, predictions))
    print('MSE:', metrics.mean_squared_error(y_test, predictions))
    print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))
    print('\n')
evaluate_model('All Features', y_test, predictions)
evaluate_model('Without "Time on App"', y_test, predictions_reduced)
evaluate_model('Polynomial Features', y_test, predictions_poly)