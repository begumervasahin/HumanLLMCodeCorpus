import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, Lasso
def load_and_display_data(file_path):
    data = pd.read_csv(file_path)
    print("First 6 rows of the dataset:\n", data.head(6))
    return data
def visualize_data(data):
    sns.jointplot(data=data, x='X1', y='y', kind='scatter')
    sns.jointplot(data=data, x='X2', y='y', kind='scatter')
    sns.jointplot(data=data, x='X1', y='X2', kind='scatter')
    plt.show()
def split_data(data, train_percentage=0.75):
    train_size = int(data.shape[0] * train_percentage)
    train_data = data.iloc[:train_size]
    test_data = data.iloc[train_size:]
    print("Training data shape:", train_data.shape)
    print("Testing data shape:", test_data.shape)
    return train_data, test_data
def generate_polynomial_features(data, degree=3):
    poly_features = PolynomialFeatures(degree=degree)
    X_poly = poly_features.fit_transform(data[['X1', 'X2']])
    return X_poly
def mse(X, y, model):
    return ((y - model.predict(X)) ** 2).mean()
def train_linear_regression(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model
def train_lasso_regression(X_train, y_train, alpha=0.15):
    model = Lasso(alpha=alpha, normalize=True, max_iter=1e5)
    model.fit(X_train, y_train)
    return model
def find_optimal_alpha(X_train, y_train, X_test, y_test, alphas):
    train_mse_array = []
    test_mse_array = []
    optimal_alpha = None
    optimal_train_mse = None
    optimal_test_mse = None
    optimal_alpha_found = False
    for alpha in alphas:
        model = train_lasso_regression(X_train, y_train, alpha)
        train_mse = mse(X_train, y_train, model)
        test_mse = mse(X_test, y_test, model)
        train_mse_array.append(train_mse)
        test_mse_array.append(test_mse)
        if train_mse > test_mse and not optimal_alpha_found:
            optimal_alpha = alpha
            optimal_train_mse = train_mse
            optimal_test_mse = test_mse
            optimal_alpha_found = True
    return optimal_alpha, optimal_train_mse, optimal_test_mse, train_mse_array, test_mse_array
def plot_mse_vs_alpha(alphas, train_mse_array, test_mse_array, xlabel, title):
    plt.plot(alphas, train_mse_array, label='Train MSE')
    plt.plot(alphas, test_mse_array, color='r', label='Test MSE')
    plt.xlabel(xlabel)
    plt.ylabel('MSE')
    plt.title(title)
    plt.legend()
    plt.show()
def main():
    data_df = load_and_display_data("poly_data.csv")
    visualize_data(data_df)
    train_df, test_df = split_data(data_df)
    X_poly = generate_polynomial_features(data_df)
    X_train, X_test = X_poly[:train_df.shape[0]], X_poly[train_df.shape[0]:]
    y_train, y_test = train_df['y'], test_df['y']
    lm = train_linear_regression(X_train, y_train)
    print("Linear Regression Model:")
    print("Training Data Set's MSE:", mse(X_train, y_train, lm))
    print("Testing Data Set's MSE :", mse(X_test, y_test, lm))
    lasso_model = train_lasso_regression(X_train, y_train)
    print("Lasso Regression Model Coefficients:", lasso_model.coef_)
    print("Lasso Regression Model:")
    print("Training Data Set's MSE:", mse(X_train, y_train, lasso_model))
    print("Testing Data Set's MSE :", mse(X_test, y_test, lasso_model))
    alphas_log = np.logspace(2, -5, base=10, num=50)
    optimal_alpha, optimal_train_mse, optimal_test_mse, train_mse_log_array, test_mse_log_array = find_optimal_alpha(
        X_train, y_train, X_test, y_test, alphas_log)
    plot_mse_vs_alpha(np.log10(alphas_log), train_mse_log_array, test_mse_log_array, 'log10(alpha)', 'MSE vs log10(alpha)')
    alphas_lin = np.linspace(1, 10, 1000)
    optimal_alpha, optimal_train_mse, optimal_test_mse, train_mse_lin_array, test_mse_lin_array = find_optimal_alpha(
        X_train, y_train, X_test, y_test, alphas_lin)
    plot_mse_vs_alpha(alphas_lin, train_mse_lin_array, test_mse_lin_array, 'alpha', 'MSE vs alpha')
    print("\nConclusion:")
    print(f"The optimized alpha value is {optimal_alpha}. This value helps in preventing overfitting and underfitting.")
    print("A Lasso model with alpha value below this is underfitting and above this is overfitting the data.")
    print("Using the Lasso model, we penalize features with low variance or correlation, retaining only the necessary features.")
    print("Overall, the polynomial features were generated, and the model was validated by splitting the dataset into training (75%) and testing (25%) sets.")
    print("The best alpha value was determined by minimizing the mean square error between training and testing data.")
if __name__ == "__main__":
    main()