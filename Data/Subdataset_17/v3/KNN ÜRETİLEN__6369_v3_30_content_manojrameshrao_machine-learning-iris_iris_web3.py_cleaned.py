import os
import timeit
import psutil
import numpy as np
import matplotlib.pyplot as plt
import mpld3
from flask import Flask
from sklearn import svm, datasets
app = Flask(__name__)
def memory_usage_psutil():
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / float(2 ** 20)
    return mem
@app.route("/")
def hello():
    start_time = timeit.default_timer()
    iris = datasets.load_iris()
    X = iris.data[:, :2]
    y = iris.target
    h = 0.02
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    C = 1.0
    classifiers = {
        'SVC with linear kernel': svm.SVC(kernel='linear', C=C).fit(X, y),
        'LinearSVC (linear kernel)': svm.LinearSVC(C=C).fit(X, y),
        'SVC with RBF kernel': svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X, y),
        'SVC with polynomial (degree 3) kernel': svm.SVC(kernel='poly', degree=3, C=C).fit(X, y)
    }
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    plt.subplots_adjust(wspace=0.4, hspace=0.4)
    for ax, (title, clf) in zip(axes.flatten(), classifiers.items()):
        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        ax.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
        ax.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, edgecolors='k')
        ax.set_xlabel('Sepal length')
        ax.set_ylabel('Sepal width')
        ax.set_xlim(xx.min(), xx.max())
        ax.set_ylim(yy.min(), yy.max())
        ax.set_xticks(())
        ax.set_yticks(())
        ax.set_title(title)
    d3plot = mpld3.fig_to_html(fig, template_type="simple")
    stop_time = timeit.default_timer()
    elapsed_time = stop_time - start_time
    mem_usage = memory_usage_psutil()
    print(f"Time (secs): {elapsed_time:.6f}")
    print(f"Memory (MB): {mem_usage:.2f}")
    return d3plot
if __name__ == "__main__":
    app.run(debug=True)