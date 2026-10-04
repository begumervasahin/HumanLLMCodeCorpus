import numpy as np
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.metrics import log_loss
import matplotlib.pyplot as plt
def log_reg(x_train, y_train, x_test, y_test, n_iter=10000, use_sgd=True):
    data = {
        'lambda': [0, 0.1, 1., 10., 100., 1000.],
        'train_avg_ce': [],
        'test_avg_ce': [],
        'l2_norm': [],
        'weights': [],
        'train_accuracy': [],
        'test_accuracy': []
    }
    print("\nLogistic Regression on data with L2 regularization...")
    for l in data['lambda']:
        logreg = initialize_model(l, use_sgd, n_iter)
        logreg.fit(x_train, y_train.flatten())
        data['weights'].append(logreg.coef_[0])
        data['l2_norm'].append(np.sum(logreg.coef_[0]**2))
        data['train_accuracy'].append(calculate_accuracy(logreg, x_train, y_train))
        data['train_avg_ce'].append(calculate_log_loss(logreg, x_train, y_train))
        data['test_accuracy'].append(calculate_accuracy(logreg, x_test, y_test))
        data['test_avg_ce'].append(calculate_log_loss(logreg, x_test, y_test))
    return data
def initialize_model(l, use_sgd, n_iter):
    if l == 0:
        if use_sgd:
            return SGDClassifier(loss='log', penalty='none', max_iter=n_iter, shuffle=False)
        else:
            return LogisticRegression(penalty='none', C=1.e12, max_iter=n_iter)
    else:
        if use_sgd:
            return SGDClassifier(loss='log', penalty='l2', alpha=l, max_iter=n_iter, shuffle=False)
        else:
            return LogisticRegression(penalty='l2', C=1./l, max_iter=n_iter)
def calculate_accuracy(model, x, y):
    return model.score(x, y.flatten())
def calculate_log_loss(model, x, y):
    predicted_proba = model.predict_proba(x)
    return log_loss(y.flatten(), predicted_proba)
def plot(data):
    lambdas = data['lambda']
    train_avg_ce = data['train_avg_ce']
    test_avg_ce = data['test_avg_ce']
    l2_norm = data['l2_norm']
    weights = data['weights']
    train_accuracy = data['train_accuracy']
    test_accuracy = data['test_accuracy']
    print("\nLambda:", lambdas)
    print("Train Average Cross Entropy:", train_avg_ce)
    print("Test Average Cross Entropy:", test_avg_ce)
    plot_metric(lambdas, train_avg_ce, test_avg_ce, 'Train & Test Average Cross Entropy', 'average cross entropy')
    print("L2 norm:", l2_norm)
    plot_single_metric(lambdas, l2_norm, 'L2 norm of Weight vector', 'L2 norm of W')
    plot_weight_values(lambdas, weights)
    print("Train Accuracies:", train_accuracy)
    print("Test Accuracies:", test_accuracy)
    plot_metric(lambdas, train_accuracy, test_accuracy, 'Train & Test Accuracies', 'accuracy')
def plot_metric(x, train_metric, test_metric, title, ylabel):
    plt.figure()
    plt.plot(x, train_metric, 'bo-', label='Train')
    plt.plot(x, test_metric, 'ro-', label='Test')
    plt.title(title)
    plt.xscale('log')
    plt.xlabel('lambda')
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()
def plot_single_metric(x, y, title, ylabel):
    plt.figure()
    plt.plot(x, y, 'bo-')
    plt.title(title)
    plt.xscale('log')
    plt.xlabel('lambda')
    plt.yscale('log')
    plt.ylabel(ylabel)
    plt.ylim(-0.1, max(y) + 1)
    plt.show()
def plot_weight_values(lambdas, weights):
    plt.figure()
    plt.title('Weight Values')
    for j in range(len(weights[0])):
        plt.plot(lambdas, [weights[i][j] for i in range(len(lambdas))], 'bo-')
    plt.xscale('log')
    plt.xlabel('lambda')
    plt.ylabel('weight values')
    plt.show()