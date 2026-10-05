import pandas as pd
import numpy as np
import preprocess
from linear_regression import Regression_Model
import performance_analysis
if __name__ == '__main__':
    data = pd.read_csv("3D_spatial_network.txt", header=None, usecols=[1, 2, 3])
    x1 = data.iloc[:, 0]
    x2 = data.iloc[:, 1]
    Y = data.iloc[:, 2]
    x1 = np.asarray(x1)
    x2 = np.asarray(x2)
    Y = np.asarray(Y)
    x1_normalized = preprocess.normalize(x1)
    x2_normalized = preprocess.normalize(x2)
    Y_normalized = preprocess.normalize(Y)
    degree = 1
    x1_train, x1_test, x1_val, x2_train, x2_test, x2_val, Y_train, Y_test, Y_val = preprocess.train_test_val_split(
        x1_normalized, x2_normalized, Y)
    feature_matrix = preprocess.generate_feature_matrix(x1_train, x2_train, degree)
    model = Regression_Model(feature_matrix, Y_train)
    cost, alphas = model.batch_gradient_descent()
    test_feature_matrix = preprocess.generate_feature_matrix(x1_test, x2_test, degree)
    predicted = model.hypothesis_function(test_feature_matrix, model.theta)
    performance_analysis.get_performance_info(Y_test, predicted, degree, model.theta, 'Batch Gradient Descent')