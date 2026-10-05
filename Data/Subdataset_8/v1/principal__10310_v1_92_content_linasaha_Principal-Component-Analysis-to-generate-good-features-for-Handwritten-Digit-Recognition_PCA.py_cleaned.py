import numpy as np
import pandas as pd
from numpy.linalg import eig
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.linear_model import SGDClassifier
testing_df = pd.read_csv('./usps.test', header=None)
X_testing, y_testing = testing_df.loc[:, 1:], testing_df.loc[:, 0]
training_df = pd.read_csv('./usps.train', header=None)
X_training, y_training = training_df.loc[:, 1:], training_df.loc[:, 0]
validate_df = pd.read_csv('./usps.valid', header=None)
X_validate, y_validate = validate_df.loc[:, 1:], validate_df.loc[:, 0]
X_train = np.array(X_training)
X_valid = np.array(X_validate)
X_test = np.array(X_testing)
y_train = np.array(y_training)
y_valid = np.array(y_validate)
y_test = np.array(y_testing)
covariance_matrix = np.matmul(X_train.transpose(), X_train)
eigenValues, eigenVectors = eig(covariance_matrix)
eig_pairs = [(np.abs(eigenValues[i]), eigenVectors[:, i]) for i in range(len(eigenValues))]
eig_pairs.sort(key=lambda x: x[0], reverse=True)
plt.figure(figsize=(10, 10))
for i in range(16):
    mat = eig_pairs[i][1].reshape(16, 16)
    plt.subplot(4, 4, i+1)
    plt.imshow(mat)
plt.show()
covariance_matrix = PCA(n_components=None)
modes = covariance_matrix.fit(X_train)
variance = modes.explained_variance_ratio_
var = np.cumsum(np.round(-np.sort(-variance), decimals=3) * 100)
plt.grid()
plt.title('PCA Analysis')
plt.ylabel('% Variance')
plt.xlabel('Principal Components')
plt.plot(var, color='k')
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
def predict_labels(alpha_i, X_newTrain, X, y_true):
    clf = SGDClassifier(alpha=alpha_i, loss='hinge', penalty='l2', max_iter=1000, tol=-np.infty).fit(X_newTrain, y_train)
    y_predict = clf.predict(X)
    error = np.mean(y_predict != y_true)
    return error
validation_error = dict()
for alpha_i in alpha_values:
    validation_error[f'k70_{alpha_i}'] = predict_labels(alpha_i, x70[:, :k70], X_validate, y_valid)
    validation_error[f'k80_{alpha_i}'] = predict_labels(alpha_i, x80[:, :k80], X_validate, y_valid)
    validation_error[f'k90_{alpha_i}'] = predict_labels(alpha_i, x90[:, :k90], X_validate, y_valid)
print('Validation Error:')
print(validation_error)
test_error = dict()
for alpha_i in alpha_values:
    test_error[f'k70_{alpha_i}'] = predict_labels(alpha_i, x70[:, :k70], X_test, y_test)
    test_error[f'k80_{alpha_i}'] = predict_labels(alpha_i, x80[:, :k80], X_test, y_test)
    test_error[f'k90_{alpha_i}'] = predict_labels(alpha_i, x90[:, :k90], X_test, y_test)
print('Test Error:')
print(test_error)