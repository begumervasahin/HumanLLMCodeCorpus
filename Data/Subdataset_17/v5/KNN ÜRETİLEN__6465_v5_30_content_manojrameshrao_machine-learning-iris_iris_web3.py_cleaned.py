import os
import psutil
import numpy as np
import matplotlib.pyplot as plt
import mpld3
from sklearn import svm, datasets
from flask import Flask
import timeit
app = Flask(__name__)
def memory_usage_psutil():
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / float(2 ** 20)
    return mem
@app.route("/")
def display_svm_plots():
    start_time = timeit.default_timer()
    iris = datasets.load_iris()
    X = iris.data[:, :2]
    y = iris.target
    step_size = 0.02
    regularization_param = 1.0
    models = [
        ('SVC with linear kernel', svm.SVC(kernel='linear', C=regularization_param).fit(X, y)),
        ('LinearSVC (linear kernel)', svm.LinearSVC(C=regularization_param).fit(X, y)),
        ('SVC with RBF kernel', svm.SVC(kernel='rbf', gamma=0.7, C=regularization_param).fit(X, y)),
        ('SVC with polynomial (degree 3) kernel', svm.SVC(kernel='poly', degree=3, C=regularization_param).fit(X, y))
    ]
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, step_size), np.arange(y_min, y_max, step_size))
    for i, (title, model) in enumerate(models):
        plt.subplot(2, 2, i + 1)
        plt.subplots_adjust(wspace=0.4, hspace=0.4)
        Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm)
        plt.xlabel('Sepal length')
        plt.ylabel('Sepal width')
        plt.xlim(xx.min(), xx.max())
        plt.ylim(yy.min(), yy.max())
        plt.xticks(())
        plt.yticks(())
        plt.title(title)
    fig = plt.gcf()
    d3plot = mpld3.fig_to_html(fig, template_type="simple")
    end_time = timeit.default_timer()
    print("Time(secs):", end_time - start_time)
    print("Memory usage (MB):", memory_usage_psutil())
    return d3plot
if __name__ == "__main__":
    app.run(debug=True)