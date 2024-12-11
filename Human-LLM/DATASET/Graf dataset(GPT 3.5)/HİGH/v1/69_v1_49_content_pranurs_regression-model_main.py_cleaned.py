import pandas as pd
import numpy as np
import preprocess
from linear_regression import Regression_Model
import performance_analysis
if b1 = = '__main__':
    b2 = pd.read_csv("3D_spatial_network.txt", header=None, usecols=[1, 2, 3])
    b3 = b2.iloc[:, 0]
    b4 = b2.iloc[:, 1]
    b5 = b2.iloc[:, 2]
    b3 = np.asarray(b3)
    b4 = np.asarray(b4)
    b5 = np.asarray(b5)
    b6 = preprocess.normalize(b3)
    b7 = preprocess.normalize(b4)
    b8 = preprocess.normalize(b5)
    a1 = 1
    x1_Train, x1_Test, x1_Val, x2_Train, x2_Test, x2_Val, Y_Train, Y_Test, b9 = preprocess.train_test_val_split(
        b6, b7, b5)
    b10 = preprocess.generate_feature_matrix(x1_Train, x2_Train, a1)
    b11 = Regression_Model(b10, Y_Train)
    cost, b12 = b11.batch_gradient_descent()
    b13 = preprocess.generate_feature_matrix(x1_Test, x2_Test, a1)
    b14 = b11.hypothesis_function(b13, b11.theta)
    performance_analysis.get_performance_info(Y_Test, b14, a1, b11.theta, 'Batch Gradient Descent')