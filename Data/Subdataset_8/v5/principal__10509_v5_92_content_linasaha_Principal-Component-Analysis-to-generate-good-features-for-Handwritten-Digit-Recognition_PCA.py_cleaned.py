import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.linear_model import SGDClassifier
def load_datasets():
    testing_df = pd.read_csv('./usps.test', header=None)
    training_df = pd.read_csv('./usps.train', header=None)
    validate_df = pd.read_csv('./usps.valid', header=None)
    X_testing, y_testing = testing_df.loc[:, 1:], testing_df.loc[:, 0]
    X_training, y_training = training_df.loc[:, 1:], training_df.loc[:, 0]
    X_validate, y_validate = validate_df.loc[:, 1:], validate_df.loc[:, 0]
    X_train, X_valid, X_test = np.array(X_training), np.array(X_validate), np.array(X_testing)
    y_train, y_valid, y_test = np.array(y_training), np.array(y_validate), np.array(y_testing)
    return X_train, y_train, X_valid, y_valid, X_test, y_test
def calculate_covariance(X):
    covariance = np.matmul(X.transpose(), X)
    eigenValues, eigenVectors = np.linalg.eig(covariance)
    eig_pairs = [(np.abs(eigenValues[i]), eigenVectors[:, i]) for i in range(len(eigenValues))]
    eig_pairs.sort(key=lambda x: x[0], reverse=True)
    return eig_pairs
def plot_eigenfaces(eig_pairs):
    for i in range(0, 16):
        mat = eig_pairs[i][1].reshape(16, 16)
        plt.subplot(4, 4, i + 1)
        plt.imshow(mat)
    plt.show()
def perform_pca_analysis(X_train):
    pca = PCA(n_components=None)
    modes = pca.fit(X_train)
    variance = modes.explained_variance_ratio_
    var = np.cumsum(np.round(-np.sort(-variance), decimals=3) * 100)
    plt.grid()
    plt.title('PCA Analysis')
    plt.ylabel('% Variance')
    plt.xlabel('Principal Components')
    plt.plot(var, color='k')
    plt.show()
    return pca
def select_principal_components(pca):
    k70 = pca.explained_variance_ratio_[pca.explained_variance_ratio_.cumsum() < 0.7].shape[0]
    k80 = pca.explained_variance_ratio_[pca.explained_variance_ratio_.cumsum() < 0.8].shape[0]
    k90 = pca.explained_variance_ratio_[pca.explained_variance_ratio_.cumsum() < 0.9].shape[0]
    return k70, k80, k90
def reduce_dimensionality(X, pca, k):
    pca_fit = pca.fit(X)
    reduced_X = pca_fit.inverse_transform(pca_fit.transform(X))
    return reduced_X, pca_fit
def train_model(alpha, X_train, y_train):
    clf = SGDClassifier(alpha=alpha, loss='hinge', penalty='l2', max_iter=1000, tol=-np.infty)
    clf.fit(X_train, y_train)
    return clf
def predict_labels(clf, X):
    y_predict = clf.predict(X)
    return y_predict
def calculate_error(y_true, y_predict):
    error_count = np.sum(y_true != y_predict)
    return error_count / len(y_true)
def validate_model(X_validate, y_validate, alphas, X_reduced, pca_fit, k_values, eig_pairs):
    validation_error = {}
    for alpha in alphas:
        for i, X_red in enumerate(X_reduced):
            clf = train_model(alpha, X_red, y_train)
            y_predict = predict_labels(clf, pca_fit.inverse_transform(X_validate[:, :k_values[i]]))
            error = calculate_error(y_validate, y_predict)
            validation_error[f'k{k_values[i]}', alpha] = error
    print('Validation Error:', validation_error)
def test_model(X_test, y_test, alphas, X_reduced, pca_fit, k_values):
    test_error = {}
    for alpha in alphas:
        for i, X_red in enumerate(X_reduced):
            clf = train_model(alpha, X_red, y_train)
            y_predict = predict_labels(clf, pca_fit.inverse_transform(X_test[:, :k_values[i]]))
            error = calculate_error(y_test, y_predict)
            test_error[f'k{k_values[i]}', alpha] = error
    print('Test Error:', test_error)
if __name__ == "__main__":
    X_train, y_train, X_validate, y_validate, X_test, y_test = load_datasets()
    eig_pairs = calculate_covariance(X_train)
    plot_eigenfaces(eig_pairs)
    pca = perform_pca_analysis(X_train)
    k70, k80, k90 = select_principal_components(pca)
    X_reduced, pca_fit = reduce_dimensionality(X_train, pca, [k70, k80, k90])
    alphas = [0.0001, 0.001, 0.01, 0.1]
    k_values = [k70, k80, k90]
    validate_model(X_validate, y_validate, alphas, X_reduced, pca_fit, k_values, eig_pairs)
    test_model(X_test, y_test, alphas, X_reduced, pca_fit, k_values)