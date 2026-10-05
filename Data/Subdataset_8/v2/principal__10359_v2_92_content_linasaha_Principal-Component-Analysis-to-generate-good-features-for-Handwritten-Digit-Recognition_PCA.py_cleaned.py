import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.linalg import eig
from sklearn.decomposition import PCA
from sklearn.linear_model import SGDClassifier
testing_df = pd.read_csv('./usps.test', header=None)
training_df = pd.read_csv('./usps.train', header=None)
validate_df = pd.read_csv('./usps.valid', header=None)
X_testing, y_testing = testing_df.iloc[:, 1:], testing_df.iloc[:, 0]
X_training, y_training = training_df.iloc[:, 1:], training_df.iloc[:, 0]
X_validate, y_validate = validate_df.iloc[:, 1:], validate_df.iloc[:, 0]
X_train, X_valid, X_test = np.array(X_training), np.array(X_validate), np.array(X_testing)
y_train, y_valid, y_test = np.array(y_training), np.array(y_validate), np.array(y_testing)
covariance_matrix = np.matmul(X_train.transpose(), X_train)
eigen_values, eigen_vectors = eig(covariance_matrix)
eig_pairs = [(np.abs(eigen_values[i]), eigen_vectors[:, i]) for i in range(len(eigen_values))]
eig_pairs.sort(key=lambda x: x[0], reverse=True)
plt.figure(figsize=(10, 10))
for i in range(16):
    mat = eig_pairs[i][1].reshape(16, 16)
    plt.subplot(4, 4, i+1)
    plt.imshow(mat)
plt.show()
pca = PCA(n_components=None)
modes = pca.fit(X_train)
variance = modes.explained_variance_ratio_
cumulative_variance = np.cumsum(np.round(variance, decimals=3) * 100)
plt.grid()
plt.title('PCA Analysis')
plt.ylabel('% Variance Explained')
plt.xlabel('Number of Principal Components')
plt.plot(cumulative_variance, color='k')
plt.show()
pca_70 = PCA(0.7)
x70 = pca_70.fit_transform(X_train)
pca_80 = PCA(0.8)
x80 = pca_80.fit_transform(X_train)
pca_90 = PCA(0.9)
x90 = pca_90.fit_transform(X_train)
k70 = np.argmax(np.cumsum(pca_70.explained_variance_ratio_) >= 0.7)
k80 = np.argmax(np.cumsum(pca_80.explained_variance_ratio_) >= 0.8)
k90 = np.argmax(np.cumsum(pca_90.explained_variance_ratio_) >= 0.9)
alpha_values = [0.0001, 0.001, 0.01, 0.1]
def calculate_error(alpha_i, X_newTrain, X, y_true):
    clf = SGDClassifier(alpha=alpha_i, loss='hinge', penalty='l2', max_iter=1000, tol=-np.infty).fit(X_newTrain, y_train)
    y_predict = clf.predict(X)
    error = np.mean(y_predict != y_true)
    return error
validation_error = dict()
for alpha_i in alpha_values:
    validation_error[f'k70_{alpha_i}'] = calculate_error(alpha_i, x70[:, :k70], X_validate, y_valid)
    validation_error[f'k80_{alpha_i}'] = calculate_error(alpha_i, x80[:, :k80], X_validate, y_valid)
    validation_error[f'k90_{alpha_i}'] = calculate_error(alpha_i, x90[:, :k90], X_validate, y_valid)
print('Validation Error:')
print(validation_error)
test_error = dict()
for alpha_i in alpha_values:
    test_error[f'k70_{alpha_i}'] = calculate_error(alpha_i, x70[:, :k70], X_test, y_test)
    test_error[f'k80_{alpha_i}'] = calculate_error(alpha_i, x80[:, :k80], X_test, y_test)
    test_error[f'k90_{alpha_i}'] = calculate_error(alpha_i, x90[:, :k90], X_test, y_test)
print('Test Error:')
print(test_error)