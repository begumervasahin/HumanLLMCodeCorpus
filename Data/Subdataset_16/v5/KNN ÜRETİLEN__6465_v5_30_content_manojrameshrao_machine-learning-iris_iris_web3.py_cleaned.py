import os
import psutil
import numpy as np
import matplotlib.pyplot as plt
import mpld3
from sklearn import svm, datasets
from flask import Flask
import timeit
b1 = Flask(b21)
def fonk1():
    b2 = psutil.Process(os.getpid())
    b3 = b2.memory_info().rss / float(2 ** 20)
    return b3
@b1.route("/")
def fonk2():
    b4 = timeit.default_timer()
    b5 = datasets.load_iris()
    b6 = b5.data[:, :2]
    b7 = b5.target
    a1 = 0.02
    a2 = 1.0
    b8 = [
        ('SVC with linear b9', svm.SVC(b9 = 'linear', b10=a2).fit(b6, b7)),
        ('LinearSVC (linear b9)', svm.LinearSVC(b10 = a2).fit(b6, b7)),
        ('SVC with RBF b9', svm.SVC(b9 = 'rbf', gamma=0.7, b10=a2).fit(b6, b7)),
        ('SVC with polynomial (degree 3) b9', svm.SVC(b9 = 'poly', degree=3, b10=a2).fit(b6, b7))
    ]
    x_min, b11 = b6[:, 0].min() - 1, b6[:, 0].max() + 1
    y_min, b12 = b6[:, 1].min() - 1, b6[:, 1].max() + 1
    xx, b13 = np.meshgrid(np.arange(x_min, b11, a1), np.arange(y_min, b12, a1))
    for i, (title, model) in enumerate(b8):
        plt.subplot(2, 2, i + 1)
        plt.subplots_adjust(b14 = 0.4, hspace=0.4)
        b15 = model.predict(np.c_[xx.ravel(), b13.ravel()])
        b15 = b15.reshape(xx.shape)
        plt.contourf(xx, b13, b15, b16 = plt.cm.coolwarm, alpha=0.8)
        plt.scatter(b6[:, 0], b6[:, 1], b17 = b7, b16=plt.cm.coolwarm)
        plt.xlabel('Sepal length')
        plt.ylabel('Sepal width')
        plt.xlim(xx.min(), xx.max())
        plt.ylim(b13.min(), b13.max())
        plt.xticks(())
        plt.yticks(())
        plt.title(title)
    b18 = plt.gcf()
    b19 = mpld3.fig_to_html(b18, template_type="simple")
    b20 = timeit.default_timer()
    print("Time(secs):", b20 - b4)
    print("Memory usage (MB):", fonk1())
    return b19
if b21 = = "__main__":
    b1.run(b22 = True)