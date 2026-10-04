import os
import numpy as np
from numpy.random import random
import matplotlib.pyplot as plt
import cv2
import copy
import glob
import sys
import numpy.linalg as LA
import IPython
from plot_functions import *
def fonk1(b6):
    def fonk2(x):
        return fonk3(x, b6)
    return func
def fonk3(x, b6):
    a1 = 0
    for i in range(len(b6)):
        a1 += (b6[i] * (x**i))
    return a1
def fonk4(b4, b6):
    b1 = [fonk3(x, b6) for x in b4]
    return np.array(b1)
def fonk5(d, b6, n, b2 = -100, upper=100):
    assert len(b6) == d+1, "Must pass in d+1 coefficients"
    b3 = upper - b2
    b4 = np.array([b2 + b3*np.random.sample() for i in range(n)])
    b1 = fonk4(b4, b6)
    return b4, b1
def fonk6(x_train, b9, d, b5 = 0, noise_std=1):
    b6 = []
    b7 = []
    for x in x_train:
        b8 = [x**i for i in range(d+1)]
        b7.append(np.array(b8))
    b7 = np.array(b7)
    b9 = np.array([i+np.random.normal(b5, noise_std) for i in b9])
    b6 = np.matmul(np.linalg.inv(np.matmul(b7.T, b7)), np.matmul(b7.T, b9))
    return b6
def fonk7(sample_coefficients, model_degree, n, b5 = 0, noise_std=0.5):
    b10 = len(sample_coefficients) - 1
    x_train, b9 = fonk5(b10, sample_coefficients, n, b2=-5, upper=5)
    b11 = fonk6(x_train, b9, model_degree)
    b12 = fonk1(sample_coefficients)
    b13 = fonk1(b11)
    b14 = fonk4(x_train, b11)
    b15 = sum([(b14[i] - b9[i])**2 for i in range(len(x_train))]) / len(x_train)
    print("\nVariance of the b16 = " + str(b15) + "\n")
    set_axis_ranges(x_train, b9)
    plot_function(x_train, b12, '-', b17 = 'r', label='ground truth function')
    plot_function(x_train, b13, '--', b17 = 'b', label='model fit function')
    plot_data(x_train, b9, '.', b17 = 'g', label='sample points')
    show_all(b18 = 'upper right')
def fonk8():
    b6 = [3, 1, 1, -2]
    fonk7(b6, 3, 6, b5 = 0, noise_std=0.5)
if b19 = = "__main__": fonk8()