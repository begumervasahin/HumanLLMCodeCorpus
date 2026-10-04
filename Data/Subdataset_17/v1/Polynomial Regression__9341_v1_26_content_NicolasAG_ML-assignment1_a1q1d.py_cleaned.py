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
        if l == 0:
            if use_sgd:
                logreg = SGDClassifier(loss='log', penalty='none', max_iter=n_iter, shuffle=False)
            else:
                logreg = LogisticRegression(penalty='l2', C=1.e12, max_iter=n_iter)
        else:
            if use_sgd:
                logreg = SGDClassifier(loss='log', penalty='l2', alpha=l, max_iter=n_iter, shuffle=False)
            else:
                logreg = LogisticRegression(penalty='l2', C=1./l, max_iter=n_iter)
        logreg.fit(x_train, y_train.flatten())
        data['weights'].append(logreg.coef_[0])
        data['l2_norm'].append(np.sum(logreg.coef_[0]**2))
        score = logreg.score(x_train, y_train.flatten())
        data['train_accuracy'].append(score)
        predicted_proba = logreg.predict_proba(x_train)
        avg_ce = log_loss(y_train.flatten(), predicted_proba)
        data['train_avg_ce'].append(avg_ce)
        score = logreg.score(x_test, y_test.flatten())
        data['test_accuracy'].append(score)
        predicted_proba = logreg.predict_proba(x_test)
        avg_ce = log_loss(y_test.flatten(), predicted_proba)
        data['test_avg_ce'].append(avg_ce)
    return data
def plot(data):
    print("\nLambda:", data['lambda'])
    print("Train Average Cross Entropy:", data['train_avg_ce'])
    print("Test Average Cross Entropy:", data['test_avg_ce'])
    plt.title('QUESTION 1.d)\nTrain & Test Average Cross Entropy')
    train_line, = plt.plot([0.0001, 0.1, 1, 10, 100, 1000], data['train_avg_ce'], 'bo-')
    test_line, = plt.plot([0.0001, 0.1, 1, 10, 100, 1000], data['test_avg_ce'], 'ro-')
    plt.legend([train_line, test_line], ['train', 'test'])
    plt.xscale('log')
    plt.xlabel('lambda')
    plt.ylabel('average cross entropy')
    plt.show()
    print("L2 norm:", data['l2_norm'])
    plt.title('QUESTION 1.d)\nL2 norm of Weight vector')
    plt.plot([0.0001, 0.1, 1, 10, 100, 1000], data['l2_norm'], 'bo-')
    plt.xscale('log')
    plt.xlabel('lambda')
    plt.yscale('log')
    plt.ylabel('L2 norm of W')
    plt.ylim(-0.1, max(data['l2_norm']) + 1)
    plt.show()
    plt.title('QUESTION 1.d)\nWeight Values')
    for j in range(len(data['weights'][0])):
        plt.plot(
            [0.0001, 0.1, 1, 10, 100, 1000],
            [data['weights'][i][j] for i in range(len(data['lambda']))],
            'bo-'
        )
    plt.xscale('log')
    plt.xlabel('lambda')
    plt.ylabel('weight values')
    plt.show()
    print("Train Accuracies:", data['train_accuracy'])
    print("Test Accuracies:", data['test_accuracy'])
    plt.title('QUESTION 1.d)\nTrain & Test Accuracies')
    train_line, = plt.plot([0.0001, 0.1, 1, 10, 100, 1000], data['train_accuracy'], 'bo-')
    test_line, = plt.plot([0.0001, 0.1, 1, 10, 100, 1000], data['test_accuracy'], 'ro-')
    plt.legend([train_line, test_line], ['train', 'test'])
    plt.xscale('log')
    plt.xlabel('lambda')
    plt.ylim(0, 1)
    plt.ylabel('accuracy')
    plt.show()
