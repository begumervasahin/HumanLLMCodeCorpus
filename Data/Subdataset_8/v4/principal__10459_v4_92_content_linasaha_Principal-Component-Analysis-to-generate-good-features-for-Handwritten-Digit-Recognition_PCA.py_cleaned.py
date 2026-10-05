
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.linear_model import SGDClassifier
testing_df = pd.read_csv('./usps.test', header=None)
X_testing, y_testing = testing_df.loc[:, 1:], testing_df.loc[:, 0]
training_df = pd.read_csv('./usps.train', header=None)
X_training, y_training = training_df.loc[:, 1:], training_df.loc[:, 0]
validate_df = pd.read_csv('./usps.valid', header=None)
X_validate, y_validate = validate_df.loc[:, 1:], validate_df.loc[:, 0]
X_train, X_valid, X_test = np.array(X_training), np.array(X_validate), np.array(X_testing)
y_train, y_valid, y_test = np.array(y_training), np.array(y_validate), np.array(y_testing)
covariance = np.matmul(X_train.transpose(), X_train)
eigenValues, eigenVectors = np.linalg.eig(covariance)
eig_pairs = [(np.abs(eigenValues[i]), eigenVectors[:, i]) for i in range(len(eigenValues))]
eig_pairs.sort(key=lambda x: x[0], reverse=True)
for i in range(0, 16):
    mat = eig_pairs[i][1].reshape(16, 16)
    plt.subplot(4, 4, i + 1)
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
pca_80 = PCA(0.8)
pca_90 = PCA(0.9)
k70, k80, k90 = pca_70.fit(X_train).n_components_, pca_80.fit(X_train).n_components_, pca_90.fit(X_train).n_components_
pca_70_fit = pca_70.fit(X_train)
x70 = pca_70_fit.inverse_transform(pca_70_fit.transform(X_train))
pca_80_fit = pca_80.fit(X_train)
x80 = pca_80_fit.inverse_transform(pca_80_fit.transform(X_train))
pca_90_fit = pca_90.fit(X_train)
x90 = pca_90_fit.inverse_transform(pca_90_fit.transform(X_train))
alpha_values = [0.0001, 0.001, 0.01, 0.1]
def predict_labels(alpha_i, X_newTrain, X, eigenVectors, features):
    clf = SGDClassifier(alpha=alpha_i, loss='hinge', penalty='l2', max_iter=1000, tol=-np.infty).fit(X_newTrain, y_train)
    y_predict = clf.predict(X)
    return y_predict
def predict_labels_k100(alpha_i, X_newTrain, X, eigenVectors):
    clf = SGDClassifier(alpha=alpha_i, loss='hinge', penalty='l2', max_iter=1000, tol=-np.infty).fit(X_newTrain, y_train)
    y_predict = clf.predict(X)
    return y_predict
def predict_error(y_true, y_predict):
    error_count = 0
    length_of_y = len(y_true)
    for i in range(0, length_of_y):
        if y_true[i] != y_predict[i]:
            error_count += 1
    return (error_count / length_of_y)
validation_error = dict()
for alpha in alpha_values:
    y_predict = predict_labels(alpha, x70, X_validate, eigenVectors, k70)
    validation_error['k70', alpha] = predict_error(y_valid, y_predict)
for alpha in alpha_values:
    y_predict = predict_labels(alpha, x80, X_validate, eigenVectors, k80)
    validation_error['k80', alpha] = predict_error(y_valid, y_predict)
for alpha in alpha_values:
    y_predict = predict_labels(alpha, x90, X_validate, eigenVectors, k90)
    validation_error['k90', alpha] = predict_error(y_valid, y_predict)
for alpha in alpha_values:
    y_predict = predict_labels_k100(alpha, X_train, X_validate, eigenVectors)
    validation_error['k100', alpha] = predict_error(y_valid, y_predict)
print('Validation Error:', validation_error)
test_error = dict()
for alpha in alpha_values:
    y_predict = predict_labels(alpha, x70, X_test, eigenVectors, k70)
    test_error['k70', alpha] = predict_error(y_test, y_predict)
for alpha in alpha_values:
    y_predict = predict_labels(alpha, x80, X_test, eigenVectors, k80)
    test_error['k80', alpha] = predict_error(y_test, y_predict)
for alpha in alpha_values:
    y_predict = predict_labels(alpha, x90, X_test, eigenVectors, k90)
    test_error['k90', alpha] = predict_error(y_test, y_predict)
for alpha in alpha_values:
    y_predict = predict_labels_k100(alpha, X_train, X_test, eigenVectors)
    test_error['k100', alpha] = predict_error(y_test, y_predict)
print('Test Error:', test_error)