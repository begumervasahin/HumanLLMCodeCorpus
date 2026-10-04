import numpy as np
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.metrics import log_loss
import matplotlib.pyplot as plt
def fonk1(x_train, y_train, x_test, y_test, b1 = 10000, use_sgd=True):
    b2 = {
        'lambda': [0, 0.1, 1., 10., 100., 1000.],
        'b7': [],
        'b10': [],
        'b12': [],
        'b13': [],
        'b14': [],
        'b15': []
    }
    print("\nLogistic Regression on b2 with L2 regularization...")
    for b3 in b2['lambda']:
        if b3 = = 0:
            if use_sgd:
                b4 = SGDClassifier(loss='log', penalty='none', max_iter=b1, shuffle=False)
            else:
                b4 = LogisticRegression(penalty='none', C=1.e12, max_iter=b1)
        else:
            if use_sgd:
                b4 = SGDClassifier(loss='log', penalty='l2', alpha=b3, max_iter=b1, shuffle=False)
            else:
                b4 = LogisticRegression(penalty='l2', C=1./b3, max_iter=b1)
        b4.fit(x_train, y_train.flatten())
        b2['b13'].append(b4.coef_[0])
        b2['b12'].append(np.sum(b4.coef_[0]**2))
        b5 = b4.score(x_train, y_train.flatten())
        b2['b14'].append(b5)
        b6 = b4.predict_proba(x_train)
        b7 = log_loss(y_train.flatten(), b6)
        b2['b7'].append(b7)
        b8 = b4.score(x_test, y_test.flatten())
        b2['b15'].append(b8)
        b9 = b4.predict_proba(x_test)
        b10 = log_loss(y_test.flatten(), b9)
        b2['b10'].append(b10)
    return b2
def fonk2(b2):
    b11 = b2['lambda']
    b7 = b2['b7']
    b10 = b2['b10']
    b12 = b2['b12']
    b13 = b2['b13']
    b14 = b2['b14']
    b15 = b2['b15']
    print("\nLambda:", b11)
    print("Train Average Cross Entropy:", b7)
    print("Test Average Cross Entropy:", b10)
    plt.figure()
    plt.fonk2(b11, b7, 'bo-', b16 = 'Train')
    plt.fonk2(b11, b10, 'ro-', b16 = 'Test')
    plt.title('Train & Test Average Cross Entropy')
    plt.xscale('log')
    plt.xlabel('lambda')
    plt.ylabel('average cross entropy')
    plt.legend()
    plt.show()
    print("L2 norm:", b12)
    plt.figure()
    plt.fonk2(b11, b12, 'bo-')
    plt.title('L2 norm of Weight vector')
    plt.xscale('log')
    plt.xlabel('lambda')
    plt.yscale('log')
    plt.ylabel('L2 norm of W')
    plt.ylim(-0.1, max(b12)+1)
    plt.show()
    plt.figure()
    plt.title('Weight Values')
    for j in range(len(b13[0])):
        plt.fonk2(b11, [b13[i][j] for i in range(len(b11))], 'bo-')
    plt.xscale('log')
    plt.xlabel('lambda')
    plt.ylabel('weight values')
    plt.show()
    print("Train Accuracies:", b14)
    print("Test Accuracies:", b15)
    plt.figure()
    plt.fonk2(b11, b14, 'bo-', b16 = 'Train')
    plt.fonk2(b11, b15, 'ro-', b16 = 'Test')
    plt.title('Train & Test Accuracies')
    plt.xscale('log')
    plt.xlabel('lambda')
    plt.ylim(0, 1)
    plt.ylabel('accuracy')
    plt.legend()
    plt.show()