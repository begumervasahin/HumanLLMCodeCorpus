import pandas as pd
import numpy as np
import preprocess
from linear_regression import Regression_Model
import performance_analysis
def fonk1():
    b1 = pd.read_csv("3D_spatial_network.txt", header=None, usecols=[1, 2, 3])
    b2 = b1.iloc[:, :-1]
    b3 = b1.iloc[:, -1]
    b4 = preprocess.normalize(b2.values)
    b5 = preprocess.normalize(b3.values)
    a1 = 1
    x_train, x_test, x_val, y_train, y_test, b6 = preprocess.train_test_val_split(b4, b5)
    b7 = preprocess.generate_feature_matrix(x_train, a1)
    b8 = Regression_Model(b7, y_train)
    cost, b9 = b8.batch_gradient_descent()
    b10 = preprocess.generate_feature_matrix(x_test, a1)
    b11 = b8.hypothesis_function(b10, b8.theta)
    performance_analysis.get_performance_info(y_test, b11, a1, b8.theta, 'Batch Gradient Descent')
if b12 = = '__main__':
    fonk1()