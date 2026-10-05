import pandas as pd
import numpy as np
import preprocess
from linear_regression import Regression_Model
import performance_analysis
def fonk1():
    b1 = pd.read_csv("3D_spatial_network.txt", header=None, usecols=[1, 2, 3])
    x1, x2, b2 = b1.iloc[:, 0], b1.iloc[:, 1], b1.iloc[:, 2]
    x1, x2, b2 = np.asarray(x1), np.asarray(x2), np.asarray(b2)
    b3 = preprocess.normalize(x1)
    b4 = preprocess.normalize(x2)
    b5 = preprocess.normalize(b2)
    a1 = 1
    x1_Train, x1_Test, x1_Val, x2_Train, x2_Test, x2_Val, Y_Train, Y_Test, b6 = preprocess.train_test_val_split(
        b3, b4, b2
    )
    b7 = preprocess.generate_feature_matrix(x1_Train, x2_Train, a1)
    b8 = Regression_Model(b7, Y_Train)
    cost, b9 = b8.batch_gradient_descent()
    b10 = preprocess.generate_feature_matrix(x1_Test, x2_Test, a1)
    b11 = b8.hypothesis_function(b10, b8.theta)
    performance_analysis.get_performance_info(Y_Test, b11, a1, b8.theta, 'Batch Gradient Descent')
if b12 = = '__main__':
    fonk1()