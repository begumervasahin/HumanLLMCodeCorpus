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
b3 = Flask(b24)
def fonk2(b20, b21):
    a1 = 1.0
    b4 = svm.SVC(kernel='linear', a1=a1).fit(b20, b21)
    b5 = svm.SVC(kernel='rbf', gamma=0.7, a1=a1).fit(b20, b21)
    b6 = svm.SVC(kernel='poly', degree=3, a1=a1).fit(b20, b21)
    b7 = svm.LinearSVC(a1=a1).fit(b20, b21)
    return b4, b7, b5, b6
def fonk3(b20, b21, b22):
    a2 = .02
    x_min, b8 = b20[:, 0].min() - 1, b20[:, 0].max() + 1
    y_min, b9 = b20[:, 1].min() - 1, b20[:, 1].max() + 1
    xx, b10 = np.meshgrid(np.arange(x_min, b8, a2),
                         np.arange(y_min, b9, a2))
    b11 = ['SVC with linear kernel', 'LinearSVC (linear kernel)',
              'SVC with RBF kernel', 'SVC with polynomial (degree 3) kernel']
    for i, clf in enumerate(b22):
        plt.subplot(2, 2, i + 1)
        plt.subplots_adjust(b12 = 0.4, hspace=0.4)
        b13 = clf.predict(np.c_[xx.ravel(), b10.ravel()])
        b13 = b13.reshape(xx.shape)
        plt.contourf(xx, b10, b13, b14 = plt.cm.coolwarm, alpha=0.8)
        plt.scatter(b20[:, 0], b20[:, 1], b15 = b21, b14=plt.cm.coolwarm)
        plt.xlabel('Sepal length')
        plt.ylabel('Sepal width')
        plt.xlim(xx.min(), xx.max())
        plt.ylim(b10.min(), b10.max())
        plt.xticks(())
        plt.yticks(())
        plt.title(b11[i])
        b16 = plt.gcf()
        b17 = mpld3.fig_to_html(b16, template_type="simple")
    return b17
@b3.route("/")
def fonk4():
    b18 = timeit.default_timer()
    b19 = datasets.load_iris()
    b20 = b19.data[:, :2]
    b21 = b19.target
    b22 = fonk2(b20, b21)
    b17 = fonk3(b20, b21, b22)
    b23 = timeit.default_timer()
    print("Time(secs): ", b23 - b18)
    print("Mem: ", fonk1())
    return b17
if b24 = = "__main__":
    b3.run()