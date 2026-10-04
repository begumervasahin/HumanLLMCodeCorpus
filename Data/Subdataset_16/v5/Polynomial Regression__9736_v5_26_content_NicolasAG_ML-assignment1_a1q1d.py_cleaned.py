import numpy as np
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.metrics import log_loss
import matplotlib.pyplot as plt
def fonk1(x_train, y_train, x_test, y_test, b1 = 10000, use_sgd=True):
    b2 = {
        'lambda': [0, 0.1, 1., 10., 100., 1000.],
        'b9': [],
        'b10': [],
        'b11': [],
        'b12': [],
        'b13': [],
        'b14': []
    }
    print("\nLogistic Regression on b2 with L2 regularization...")
    for b4 in b2['lambda']:
        b3 = fonk2(b4, use_sgd, b1)
        b3.fit(x_train, y_train.flatten())
        b2['b12'].append(b3.coef_[0])
        b2['b11'].append(np.sum(b3.coef_[0]**2))
        b2['b13'].append(fonk3(b3, x_train, y_train))
        b2['b9'].append(fonk4(b3, x_train, y_train))
        b2['b14'].append(fonk3(b3, x_test, y_test))
        b2['b10'].append(fonk4(b3, x_test, y_test))
    return b2
def fonk2(b4, use_sgd, b1):
    if b4 = = 0:
        if use_sgd:
            return SGDClassifier(b5 = 'log', b6='none', max_iter=b1, shuffle=False)
        else:
            return LogisticRegression(b6 = 'none', C=1.e12, max_iter=b1)
    else:
        if use_sgd:
            return SGDClassifier(b5 = 'log', b6='l2', alpha=b4, max_iter=b1, shuffle=False)
        else:
            return LogisticRegression(b6 = 'l2', C=1./b4, max_iter=b1)
def fonk3(model, x, y):
    return model.score(x, y.flatten())
def fonk4(model, x, y):
    b7 = model.predict_proba(x)
    return log_loss(y.flatten(), b7)
def fonk5(b2):
    b8 = b2['lambda']
    b9 = b2['b9']
    b10 = b2['b10']
    b11 = b2['b11']
    b12 = b2['b12']
    b13 = b2['b13']
    b14 = b2['b14']
    print("\nLambda:", b8)
    print("Train Average Cross Entropy:", b9)
    print("Test Average Cross Entropy:", b10)
    fonk6(b8, b9, b10, 'Train & Test Average Cross Entropy', 'average cross entropy')
    print("L2 norm:", b11)
    fonk7(b8, b11, 'L2 norm of Weight vector', 'L2 norm of W')
    fonk8(b8, b12)
    print("Train Accuracies:", b13)
    print("Test Accuracies:", b14)
    fonk6(b8, b13, b14, 'Train & Test Accuracies', 'accuracy')
def fonk6(x, train_metric, test_metric, title, ylabel):
    plt.figure()
    plt.fonk5(x, train_metric, 'bo-', b15 = 'Train')
    plt.fonk5(x, test_metric, 'ro-', b15 = 'Test')
    plt.title(title)
    plt.xscale('log')
    plt.xlabel('lambda')
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()
def fonk7(x, y, title, ylabel):
    plt.figure()
    plt.fonk5(x, y, 'bo-')
    plt.title(title)
    plt.xscale('log')
    plt.xlabel('lambda')
    plt.yscale('log')
    plt.ylabel(ylabel)
    plt.ylim(-0.1, max(y) + 1)
    plt.show()
def fonk8(b8, b12):
    plt.figure()
    plt.title('Weight Values')
    for j in range(len(b12[0])):
        plt.fonk5(b8, [b12[i][j] for i in range(len(b8))], 'bo-')
    plt.xscale('log')
    plt.xlabel('lambda')
    plt.ylabel('weight values')
    plt.show()