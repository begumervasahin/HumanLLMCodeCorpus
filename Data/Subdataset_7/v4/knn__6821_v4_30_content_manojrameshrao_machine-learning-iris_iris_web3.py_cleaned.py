import psutil
import os
import numpy as np
import matplotlib.pyplot as plt
import mpld3
from sklearn import svm, datasets
import timeit
from flask import Flask
def fonk1():
    b1 = psutil.Process(os.getpid())
    b2 = b1.memory_info()[0] / float(2 ** 20)
    return b2
b3 = Flask(__name__)
@b3.route("/")
def fonk2():
    b4 = timeit.default_timer()
    b5 = datasets.load_iris()
    b6 = b5.data[:, :2]
    b7 = b5.target
    a1 = .02
    a2 = 1.0
    b8 = svm.SVC(kernel='linear', a2=a2).fit(b6, b7)
    b9 = svm.SVC(kernel='rbf', gamma=0.7, a2=a2).fit(b6, b7)
    b10 = svm.SVC(kernel='poly', degree=3, a2=a2).fit(b6, b7)
    b11 = svm.LinearSVC(a2=a2).fit(b6, b7)
    x_min, b12 = b6[:, 0].min() - 1, b6[:, 0].max() + 1
    y_min, b13 = b6[:, 1].min() - 1, b6[:, 1].max() + 1
    xx, b14 = np.meshgrid(np.arange(x_min, b12, a1),
                         np.arange(y_min, b13, a1))
    b15 = ['SVC with linear kernel',
              'LinearSVC (linear kernel)',
              'SVC with RBF kernel',
              'SVC with polynomial (degree 3