import os
import timeit
import psutil
import numpy as np
import matplotlib.pyplot as plt
import mpld3
from flask import Flask
from sklearn import svm, datasets
b1 = Flask(b20)
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
    a1 = .02
    x_min, b8 = b6[:, 0].min() - 1, b6[:, 0].max() + 1
    y_min, b9 = b6[:, 1].min() - 1, b6[:, 1].max() + 1
    xx, b10 = np.meshgrid(np.arange(x_min, b8, a1), np.arange(y_min, b9, a1))
    a2 = 1.0
    b11 = {
        'SVC with linear b12': svm.SVC(b12 = 'linear', a2=a2).fit(b6, b7),
        'LinearSVC (linear b12)': svm.LinearSVC(a2 = a2).fit(b6, b7),
        'SVC with RBF b12': svm.SVC(b12 = 'rbf', gamma=0.7, a2=a2).fit(b6, b7),
        'SVC with polynomial (degree 3) b12': svm.SVC(b12 = 'poly', degree=3, a2=a2).fit(b6, b7)
    }
    fig, b13 = plt.subplots(2, 2, figsize=(12, 10))
    plt.subplots_adjust(b14 = 0.4, hspace=0.4)
    for ax, (title, clf) in zip(b13.flatten(), b11.items()):
        b15 = clf.predict(np.c_[xx.ravel(), b10.ravel()])
        b15 = b15.reshape(xx.shape)
        ax.contourf(xx, b10, b15, b16 = plt.cm.coolwarm, alpha=0.8)
        ax.scatter(b6[:, 0], b6[:, 1], b17 = b7, b16=plt.cm.coolwarm, edgecolors='k')
        ax.set_xlabel('Sepal length')
        ax.set_ylabel('Sepal width')
        ax.set_xlim(xx.min(), xx.max())
        ax.set_ylim(b10.min(), b10.max())
        ax.set_xticks(())
        ax.set_yticks(())
        ax.set_title(title)
    b18 = mpld3.fig_to_html(fig, template_type="simple")
    b19 = timeit.default_timer()
    print("Time(secs): ", b19 - b4)
    print("Mem: ", fonk1())
    return b18
if b20 = = "__main__":
    b1.run(b21 = True)