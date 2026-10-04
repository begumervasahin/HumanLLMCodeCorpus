from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.metrics import log_loss
import matplotlib.pyplot as plt
def fonk1(gaussian_data, y_train, y_test, sigmas, b1 = 10000, use_sgd=True):
    print("\nLogistic Regression on data applied to Gaussian basis functions (no regularization)...")
    for sigma in sigmas:
        b2 = gaussian_data[str(sigma)]['x_train']
        b3 = gaussian_data[str(sigma)]['x_test']
        if use_sgd:
            b4 = SGDClassifier(loss='log_loss', penalty='none', max_iter=b1, shuffle=False)
        else:
            b4 = LogisticRegression(penalty='l2', C=1.e12, max_iter=b1)
        b4.fit(b2, y_train.flatten())
        b5 = b4.score(b2, y_train.flatten())
        gaussian_data[str(sigma)]['train_accuracy'] = b5
        b6 = b4.predict_proba(b2)
        b7 = log_loss(y_train.flatten(), b6)
        gaussian_data[str(sigma)]['b7'] = b7
        b8 = b4.score(b3, y_test.flatten())
        gaussian_data[str(sigma)]['test_accuracy'] = b8
        b9 = b4.predict_proba(b3)
        b10 = log_loss(y_test.flatten(), b9)
        gaussian_data[str(sigma)]['b10'] = b10
    return gaussian_data
def fonk2(gaussian_data, sigmas, old_data):
    print("Sigma values:", sigmas)
    b11 = [gaussian_data[str(sigma)]['b7'] for sigma in sigmas]
    b12 = [gaussian_data[str(sigma)]['b10'] for sigma in sigmas]
    print("Train average Cross-Entropy:", b11)
    print("Test average Cross-Entropy:", b12)
    plt.figure()
    plt.title('QUESTION 1.f)\nTrain & Test Avg. Cross-Entropy')
    train_line, = plt.fonk2(sigmas, b11, 'bo-', b13 = 'train gaussian')
    test_line, = plt.fonk2(sigmas, b12, 'ro-', b13 = 'test gaussian')
    train_line_old, = plt.fonk2(sigmas, [old_data['b7'][0]]*len(sigmas), 'c-', b13 = 'train no regularization')
    test_line_old, = plt.fonk2(sigmas, [old_data['b10'][0]]*len(sigmas), 'm-', b13 = 'test no regularization')
    plt.legend()
    plt.xlabel('sigma')
    plt.ylabel('average cross-entropy')
    plt.ylim(-0.1, max(b11 + b12 + [old_data['b7'][0], old_data['b10'][0]]) + 1)
    plt.show()
    b14 = [gaussian_data[str(sigma)]['train_accuracy'] for sigma in sigmas]
    b15 = [gaussian_data[str(sigma)]['test_accuracy'] for sigma in sigmas]
    print("Train accuracies:", b14)
    print("Test accuracies:", b15)
    plt.figure()
    plt.title('QUESTION 1.f)\nTrain & Test Accuracies')
    train_line, = plt.fonk2(sigmas, b14, 'bo-', b13 = 'train gaussian')
    test_line, = plt.fonk2(sigmas, b15, 'ro-', b13 = 'test gaussian')
    train_line_old, = plt.fonk2(sigmas, [old_data['train_accuracy'][0]]*len(sigmas), 'c-', b13 = 'train no regularization')
    test_line_old, = plt.fonk2(sigmas, [old_data['test_accuracy'][0]]*len(sigmas), 'm-', b13 = 'test no regularization')
    plt.legend(b16 = 'lower right')
    plt.xlabel('sigma')
    plt.ylim(0, 1.01)
    plt.ylabel('accuracy')
    plt.show()
