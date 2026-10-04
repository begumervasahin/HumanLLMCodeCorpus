from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.metrics import log_loss
import matplotlib.pyplot as plt
def log_reg(gaussian_data, y_train, y_test, sigmas, n_iter=10000, use_sgd=True):
    print("\nLogistic Regression on data applied to Gaussian basis functions (no regularization)...")
    for sigma in sigmas:
        basis_x_train = gaussian_data[str(sigma)]['x_train']
        basis_x_test = gaussian_data[str(sigma)]['x_test']
        if use_sgd:
            logreg = SGDClassifier(loss='log_loss', penalty='none', max_iter=n_iter, shuffle=False)
        else:
            logreg = LogisticRegression(penalty='l2', C=1.e12, max_iter=n_iter)
        logreg.fit(basis_x_train, y_train.flatten())
        train_score = logreg.score(basis_x_train, y_train.flatten())
        gaussian_data[str(sigma)]['train_accuracy'] = train_score
        train_predicted_proba = logreg.predict_proba(basis_x_train)
        train_avg_ce = log_loss(y_train.flatten(), train_predicted_proba)
        gaussian_data[str(sigma)]['train_avg_ce'] = train_avg_ce
        test_score = logreg.score(basis_x_test, y_test.flatten())
        gaussian_data[str(sigma)]['test_accuracy'] = test_score
        test_predicted_proba = logreg.predict_proba(basis_x_test)
        test_avg_ce = log_loss(y_test.flatten(), test_predicted_proba)
        gaussian_data[str(sigma)]['test_avg_ce'] = test_avg_ce
    return gaussian_data
def plot(gaussian_data, sigmas, old_data):
    print("Sigma values:", sigmas)
    train_ce = [gaussian_data[str(sigma)]['train_avg_ce'] for sigma in sigmas]
    test_ce = [gaussian_data[str(sigma)]['test_avg_ce'] for sigma in sigmas]
    print("Train average Cross-Entropy:", train_ce)
    print("Test average Cross-Entropy:", test_ce)
    plt.figure()
    plt.title('QUESTION 1.f)\nTrain & Test Avg. Cross-Entropy')
    train_line, = plt.plot(sigmas, train_ce, 'bo-', label='train gaussian')
    test_line, = plt.plot(sigmas, test_ce, 'ro-', label='test gaussian')
    train_line_old, = plt.plot(sigmas, [old_data['train_avg_ce'][0]]*len(sigmas), 'c-', label='train no regularization')
    test_line_old, = plt.plot(sigmas, [old_data['test_avg_ce'][0]]*len(sigmas), 'm-', label='test no regularization')
    plt.legend()
    plt.xlabel('sigma')
    plt.ylabel('average cross-entropy')
    plt.ylim(-0.1, max(train_ce + test_ce + [old_data['train_avg_ce'][0], old_data['test_avg_ce'][0]]) + 1)
    plt.show()
    train_acc = [gaussian_data[str(sigma)]['train_accuracy'] for sigma in sigmas]
    test_acc = [gaussian_data[str(sigma)]['test_accuracy'] for sigma in sigmas]
    print("Train accuracies:", train_acc)
    print("Test accuracies:", test_acc)
    plt.figure()
    plt.title('QUESTION 1.f)\nTrain & Test Accuracies')
    train_line, = plt.plot(sigmas, train_acc, 'bo-', label='train gaussian')
    test_line, = plt.plot(sigmas, test_acc, 'ro-', label='test gaussian')
    train_line_old, = plt.plot(sigmas, [old_data['train_accuracy'][0]]*len(sigmas), 'c-', label='train no regularization')
    test_line_old, = plt.plot(sigmas, [old_data['test_accuracy'][0]]*len(sigmas), 'm-', label='test no regularization')
    plt.legend(loc='lower right')
    plt.xlabel('sigma')
    plt.ylim(0, 1.01)
    plt.ylabel('accuracy')
    plt.show()
