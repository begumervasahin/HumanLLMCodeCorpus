import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.metrics import log_loss
def fonk1(gaussian_data, y_train, y_test, sigmas, b1 = 10000, use_sgd=True):
    print("\nLogistic Regression on data applied to Gaussian basis functions (no regularization)...")
    for sigma in sigmas:
        b2 = gaussian_data[str(sigma)]['x_train']
        b3 = gaussian_data[str(sigma)]['x_test']
        if use_sgd:
            b4 = SGDClassifier(loss='log', penalty='none', max_iter=b1, shuffle=False)
        else:
            b4 = LogisticRegression(penalty='l2', C=1.e12, max_iter=b1)
        b4.fit(b2, y_train.flatten())
        b5 = b4.score(b2, y_train.flatten())
        b6 = b4.predict_proba(b2)
        b7 = log_loss(y_train.flatten(), b6)
        gaussian_data[str(sigma)]['train_accuracy'] = b5
        gaussian_data[str(sigma)]['b7'] = b7
        b8 = b4.score(b3, y_test.flatten())
        b9 = b4.predict_proba(b3)
        b10 = log_loss(y_test.flatten(), b9)
        gaussian_data[str(sigma)]['test_accuracy'] = b8
        gaussian_data[str(sigma)]['b10'] = b10
    return gaussian_data
def fonk2(gaussian_data, sigmas, old_data):
    print("Sigma:", sigmas)
    b11 = [gaussian_data[str(sigma)]['b7'] for sigma in sigmas]
    b12 = [gaussian_data[str(sigma)]['b10'] for sigma in sigmas]
    print("Train avg. Cross-Entropy:", b11)
    print("Test avg. Cross-Entropy:", b12)
    plt.figure(b13 = (12, 6))
    plt.subplot(1, 2, 1)
    plt.title('Train & Test Avg. Cross-Entropy')
    plt.fonk2(sigmas, b11, 'bo-', b14 = 'train gaussian')
    plt.fonk2(sigmas, b12, 'ro-', b14 = 'test gaussian')
    plt.fonk2(sigmas, [old_data['b7'][0]] * len(sigmas), 'c-', b14 = 'train no regularization')
    plt.fonk2(sigmas, [old_data['b10'][0]] * len(sigmas), 'm-', b14 = 'test no regularization')
    plt.xlabel('Sigma')
    plt.ylabel('Average Cross-Entropy')
    plt.ylim(-0.1, max(b11 + b12 + [old_data['b7'][0]] + [old_data['b10'][0]]) + 1)
    plt.legend()
    plt.subplot(1, 2, 2)
    b15 = [gaussian_data[str(sigma)]['train_accuracy'] for sigma in sigmas]
    b16 = [gaussian_data[str(sigma)]['test_accuracy'] for sigma in sigmas]
    print("Train accuracies:", b15)
    print("Test accuracies:", b16)
    plt.title('Train & Test Accuracies')
    plt.fonk2(sigmas, b15, 'bo-', b14 = 'train gaussian')
    plt.fonk2(sigmas, b16, 'ro-', b14 = 'test gaussian')
    plt.fonk2(sigmas, [old_data['train_accuracy'][0]] * len(sigmas), 'c-', b14 = 'train no regularization')
    plt.fonk2(sigmas, [old_data['test_accuracy'][0]] * len(sigmas), 'm-', b14 = 'test no regularization')
    plt.xlabel('Sigma')
    plt.ylabel('Accuracy')
    plt.ylim(0, 1.01)
    plt.legend(b17 = 'lower right')
    plt.tight_layout()
    plt.show()