import psutil
import os
import numpy as np
import matplotlib.pyplot as plt
import mpld3
from sklearn import svm, datasets
import timeit
from flask import Flask
def memory_usage_psutil():
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / float(2 ** 20)
    return mem
app = Flask(__name__)
def train_svm_models(X, y):
    C = 1.0
    svc = svm.SVC(kernel='linear', C=C).fit(X, y)
    rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X, y)
    poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X, y)
    lin_svc = svm.LinearSVC(C=C).fit(X, y)
    return svc, lin_svc, rbf_svc, poly_svc
def plot_decision_boundaries(X, y, models):
    h = .02
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    titles = ['SVC with linear kernel', 'LinearSVC (linear kernel)',
              'SVC with RBF kernel', 'SVC with polynomial (degree 3) kernel']
    for i, clf in enumerate(models):
        plt.subplot(2, 2, i + 1)
        plt.subplots_adjust(wspace=0.4, hspace=0.4)
        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm)
        plt.xlabel('Sepal length')
        plt.ylabel('Sepal width')
        plt.xlim(xx.min(), xx.max())
        plt.ylim(yy.min(), yy.max())
        plt.xticks(())
        plt.yticks(())
        plt.title(titles[i])
        fig = plt.gcf()
        d3plot = mpld3.fig_to_html(fig, template_type="simple")
    return d3plot
@app.route("/")
def hello():
    start_time = timeit.default_timer()
    iris = datasets.load_iris()
    X = iris.data[:, :2]
    y = iris.target
    models = train_svm_models(X, y)
    d3plot = plot_decision_boundaries(X, y, models)
    stop_time = timeit.default_timer()
    print("Time(secs): ", stop_time - start_time)
    print("Mem: ", memory_usage_psutil())
    return d3plot
if __name__ == "__main__":
    app.run()