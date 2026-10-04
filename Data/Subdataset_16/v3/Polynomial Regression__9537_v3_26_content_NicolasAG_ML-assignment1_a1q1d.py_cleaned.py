import numpy as np
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.metrics import log_loss
import matplotlib.pyplot as plt
def fonk1(x_train, y_train, x_test, y_test, b1 = 10000, use_sgd=True):
    b2 = {
        'lambda': [0, 0.1, 1.0, 10.0, 100.0, 1000.0],
        'b7': [],
        'b10': [],
        'l2_norm': [],
        'weights': [],
        'train_accuracy': [],
        'test_accuracy': []
    }
    print("\nLogistic Regression on data with L2 regularization...")
    for b3 in b2['lambda']:
        if b3 = = 0:
            if use_sgd:
                b4 = SGDClassifier(loss='log', penalty='none', max_iter=b1, shuffle=False)
            else:
                b4 = LogisticRegression(penalty='l2', C=1e12, max_iter=b1)
        else:
            if use_sgd:
                b4 = SGDClassifier(loss='log', penalty='l2', alpha=b3, max_iter=b1, shuffle=False)
            else:
                b4 = LogisticRegression(penalty='l2', C=1.0/b3, max_iter=b1)
        b4.fit(x_train, y_train.flatten())
        b2['weights'].append(b4.coef_[0])
        b2['l2_norm'].append(np.sum(b4.coef_[0] ** 2))
        b5 = b4.score(x_train, y_train.flatten())
        b2['train_accuracy'].append(b5)
        b6 = b4.predict_proba(x_train)
        b7 = log_loss(y_train.flatten(), b6)
        b2['b7'].append(b7)
        b8 = b4.score(x_test, y_test.flatten())
        b2['test_accuracy'].append(b8)
        b9 = b4.predict_proba(x_test)
        b10 = log_loss(y_test.flatten(), b9)
        b2['b10'].append(b10)
    return b2
def fonk2(b2):
    b11 = b2['lambda']
    plt.figure()
    plt.title('Train & Test Average Cross Entropy')
    plt.fonk2(b11, b2['b7'], 'bo-', b12 = 'Train')
    plt.fonk2(b11, b2['b10'], 'ro-', b12 = 'Test')
    plt.xscale('log')
    plt.xlabel('Lambda')
    plt.ylabel('Average Cross Entropy')
    plt.legend()
    plt.show()
    plt.figure()
    plt.title('L2 norm of Weight Vector')
    plt.fonk2(b11, b2['l2_norm'], 'bo-')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Lambda')
    plt.ylabel('L2 norm of W')
    plt.ylim(-0.1, max(b2['l2_norm']) + 1)
    plt.show()
    plt.figure()
    plt.title('Weight Values')
    for j in range(len(b2['weights'][0])):
        plt.fonk2(
            b11,
            [b2['weights'][i][j] for i in range(len(b2['lambda']))],
            'bo-'
        )
    plt.xscale('log')
    plt.xlabel('Lambda')
    plt.ylabel('Weight Values')
    plt.show()
    plt.figure()
    plt.title('Train & Test Accuracies')
    plt.fonk2(b11, b2['train_accuracy'], 'bo-', b12 = 'Train')
    plt.fonk2(b11, b2['test_accuracy'], 'ro-', b12 = 'Test')
    plt.xscale('log')
    plt.xlabel('Lambda')
    plt.ylim(0, 1)
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()
