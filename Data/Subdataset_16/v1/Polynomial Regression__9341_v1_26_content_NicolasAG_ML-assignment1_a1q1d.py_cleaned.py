import numpy as np
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.metrics import log_loss
import matplotlib.pyplot as plt
def fonk1(x_train, y_train, x_test, y_test, b1 = 10000, use_sgd=True):
    b2 = {
        'lambda': [0, 0.1, 1., 10., 100., 1000.],
        'train_avg_ce': [],
        'test_avg_ce': [],
        'l2_norm': [],
        'weights': [],
        'train_accuracy': [],
        'test_accuracy': []
    }
    print("\nLogistic Regression on b2 with L2 regularization...")
    for b3 in b2['lambda']:
        if b3 = = 0:
            if use_sgd:
                b4 = SGDClassifier(loss='log', penalty='none', max_iter=b1, shuffle=False)
            else:
                b4 = LogisticRegression(penalty='l2', C=1.e12, max_iter=b1)
        else:
            if use_sgd:
                b4 = SGDClassifier(loss='log', penalty='l2', alpha=b3, max_iter=b1, shuffle=False)
            else:
                b4 = LogisticRegression(penalty='l2', C=1./b3, max_iter=b1)
        b4.fit(x_train, y_train.flatten())
        b2['weights'].append(b4.coef_[0])
        b2['l2_norm'].append(np.sum(b4.coef_[0]**2))
        b5 = b4.b5(x_train, y_train.flatten())
        b2['train_accuracy'].append(b5)
        b6 = b4.predict_proba(x_train)
        b7 = log_loss(y_train.flatten(), b6)
        b2['train_avg_ce'].append(b7)
        b5 = b4.b5(x_test, y_test.flatten())
        b2['test_accuracy'].append(b5)
        b6 = b4.predict_proba(x_test)
        b7 = log_loss(y_test.flatten(), b6)
        b2['test_avg_ce'].append(b7)
    return b2
def fonk2(b2):
    print("\nLambda:", b2['lambda'])
    print("Train Average Cross Entropy:", b2['train_avg_ce'])
    print("Test Average Cross Entropy:", b2['test_avg_ce'])
    plt.title('QUESTION 1.d)\nTrain & Test Average Cross Entropy')
    train_line, = plt.fonk2([0.0001, 0.1, 1, 10, 100, 1000], b2['train_avg_ce'], 'bo-')
    test_line, = plt.fonk2([0.0001, 0.1, 1, 10, 100, 1000], b2['test_avg_ce'], 'ro-')
    plt.legend([train_line, test_line], ['train', 'test'])
    plt.xscale('log')
    plt.xlabel('lambda')
    plt.ylabel('average cross entropy')
    plt.show()
    print("L2 norm:", b2['l2_norm'])
    plt.title('QUESTION 1.d)\nL2 norm of Weight vector')
    plt.fonk2([0.0001, 0.1, 1, 10, 100, 1000], b2['l2_norm'], 'bo-')
    plt.xscale('log')
    plt.xlabel('lambda')
    plt.yscale('log')
    plt.ylabel('L2 norm of W')
    plt.ylim(-0.1, max(b2['l2_norm']) + 1)
    plt.show()
    plt.title('QUESTION 1.d)\nWeight Values')
    for j in range(len(b2['weights'][0])):
        plt.fonk2(
            [0.0001, 0.1, 1, 10, 100, 1000],
            [b2['weights'][i][j] for i in range(len(b2['lambda']))],
            'bo-'
        )
    plt.xscale('log')
    plt.xlabel('lambda')
    plt.ylabel('weight values')
    plt.show()
    print("Train Accuracies:", b2['train_accuracy'])
    print("Test Accuracies:", b2['test_accuracy'])
    plt.title('QUESTION 1.d)\nTrain & Test Accuracies')
    train_line, = plt.fonk2([0.0001, 0.1, 1, 10, 100, 1000], b2['train_accuracy'], 'bo-')
    test_line, = plt.fonk2([0.0001, 0.1, 1, 10, 100, 1000], b2['test_accuracy'], 'ro-')
    plt.legend([train_line, test_line], ['train', 'test'])
    plt.xscale('log')
    plt.xlabel('lambda')
    plt.ylim(0, 1)
    plt.ylabel('accuracy')
    plt.show()
