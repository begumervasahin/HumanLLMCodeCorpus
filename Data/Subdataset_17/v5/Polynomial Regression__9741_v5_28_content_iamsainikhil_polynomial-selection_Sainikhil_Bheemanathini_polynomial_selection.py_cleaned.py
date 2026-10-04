import time
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, Lasso
get_ipython().run_line_magic('matplotlib', 'inline')
data_df = pd.read_csv("poly_data.csv")
print(data_df.head(6))
sns.jointplot(x=data_df['X1'], y=data_df['y'])
sns.jointplot(x=data_df['X2'], y=data_df['y'])
sns.jointplot(x=data_df['X1'], y=data_df['X2'])
percentage_for_training = 0.75
number_of_training_data = int(data_df.shape[0] * percentage_for_training)
train_df = data_df[:number_of_training_data]
test_df = data_df[number_of_training_data:]
print(f"Training set shape: {train_df.shape}")
print(f"Testing set shape: {test_df.shape}")
polynomial_features = PolynomialFeatures(degree=3)
X_poly = polynomial_features.fit_transform(data_df[['X1', 'X2']])
X_train = X_poly[:number_of_training_data]
X_test = X_poly[number_of_training_data:]
def mse(X, y, model):
    return ((y - model.predict(X)) ** 2).sum() / y.shape[0]
lm = LinearRegression()
lm.fit(X_train, train_df['y'])
train_mse = mse(X_train, train_df['y'], lm)
test_mse = mse(X_test, test_df['y'], lm)
print(f"Training Data Set's MSE: {train_mse}")
print(f"Testing Data Set's MSE: {test_mse}")
lasso_model = Lasso(alpha=0.15, normalize=True, max_iter=1e5)
lasso_model.fit(X_train, train_df['y'])
train_mse = mse(X_train, train_df['y'], lasso_model)
test_mse = mse(X_test, test_df['y'], lasso_model)
print(f"Training Data Set's MSE (Lasso): {train_mse}")
print(f"Testing Data Set's MSE (Lasso): {test_mse}")
alphas = np.logspace(2, -5, base=10, num=50)
train_mse_array = []
test_mse_array = []
for alpha in alphas:
    lasso_model = Lasso(alpha=alpha, normalize=True, max_iter=1e5)
    lasso_model.fit(X_train, train_df['y'])
    train_mse = mse(X_train, train_df['y'], lasso_model)
    test_mse = mse(X_test, test_df['y'], lasso_model)
    train_mse_array.append(train_mse)
    test_mse_array.append(test_mse)
plt.plot(np.log10(alphas), train_mse_array, label='Train MSE')
plt.plot(np.log10(alphas), test_mse_array, color='r', label='Test MSE')
plt.legend()
plt.xlabel('log10(alpha)')
plt.ylabel('MSE')
plt.title('MSE vs alpha')
plt.show()
alphas = np.linspace(1, 10, 1000)
train_mse_array = []
test_mse_array = []
optimal_alpha = None
optimal_train_mse = None
optimal_test_mse = None
for alpha in alphas:
    lasso_model = Lasso(alpha=alpha, normalize=True, max_iter=1e5)
    lasso_model.fit(X_train, train_df['y'])
    train_mse = mse(X_train, train_df['y'], lasso_model)
    test_mse = mse(X_test, test_df['y'], lasso_model)
    train_mse_array.append(train_mse)
    test_mse_array.append(test_mse)
    if optimal_alpha is None or (train_mse - test_mse > 0):
        optimal_alpha = alpha
        optimal_train_mse = train_mse
        optimal_test_mse = test_mse
print(f"The optimal alpha is {optimal_alpha}")
print(f"Train MSE at optimal alpha: {optimal_train_mse}")
print(f"Test MSE at optimal alpha: {optimal_test_mse}")
plt.plot(alphas, train_mse_array, label='Train MSE')
plt.plot(alphas, test_mse_array, color='r', label='Test MSE')
plt.legend()
plt.xlabel('alpha')
plt.ylabel('MSE')
plt.title('MSE vs alpha')
plt.show()
summary = (
    "From the above diagram, I found that the optimized alpha value is 3.567. "
    "This means that, at this alpha value, we can prevent overfitting and underfitting. "
    "Lasso model with alpha value below 3.567 is underfitting and above 3.567 is overfitting the data. "
    "Instead of using a linear model, I used Lasso linear model which is used to penalize number of features with low variance or correlation. "
    "These features can be found by looking at the coefficients of the Lasso linear model.\n"
    "Overall, from the dataset, I found the polynomial that best fits the data. I checked my model by dividing the dataset into training data and testing data. "
    "I generated the model using the training data of 75% and then tested the model using the testing data of 25%. "
    "To prevent overfitting and underfitting, I generated Lasso linear model with the optimized alpha value to penalize the features and retain only the required features. "
    "Thus, I reached the best alpha value by minimizing the mean square error between training data and testing data."
)
print(summary)