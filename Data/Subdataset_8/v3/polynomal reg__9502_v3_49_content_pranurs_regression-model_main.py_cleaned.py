import pandas as pd
import numpy as np
import preprocess
from linear_regression import Regression_Model
import performance_analysis
def main():
    data = pd.read_csv("3D_spatial_network.txt", header=None, usecols=[1, 2, 3])
    features = data.iloc[:, :-1]
    target = data.iloc[:, -1]
    features_normalized = preprocess.normalize(features.values)
    target_normalized = preprocess.normalize(target.values)
    degree = 1
    x_train, x_test, x_val, y_train, y_test, y_val = preprocess.train_test_val_split(features_normalized, target_normalized)
    feature_matrix_train = preprocess.generate_feature_matrix(x_train, degree)
    model = Regression_Model(feature_matrix_train, y_train)
    cost, alphas = model.batch_gradient_descent()
    feature_matrix_test = preprocess.generate_feature_matrix(x_test, degree)
    predicted = model.hypothesis_function(feature_matrix_test, model.theta)
    performance_analysis.get_performance_info(y_test, predicted, degree, model.theta, 'Batch Gradient Descent')
if __name__ == '__main__':
    main()