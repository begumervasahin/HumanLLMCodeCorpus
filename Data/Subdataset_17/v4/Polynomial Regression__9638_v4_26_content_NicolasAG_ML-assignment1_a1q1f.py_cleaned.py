import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.metrics import log_loss
def log_reg(gaussian_data, y_train, y_test, sigmas, n_iter=10000, use_sgd=True):
    print("\nLogistic Regression on data applied to Gaussian basis functions (no regularization)...")
    for sigma in sigmas:
        basis_x_train = gaussian_data[str(sigma)]['x_train']
        basis_x_test = gaussian_data[str(sigma)]['x_test']
        if use_sgd:
            logreg = SGDClassifier(loss='log', penalty='none', max_iter=n_iter, shuffle=False)
        else:
            logreg = LogisticRegression(penalty='l2', C=1.e12, max_iter=n_iter)
        logreg.fit(basis_x_train, y_train.flatten())
        train_score = logreg.score(basis_x_train, y_train.flatten())
        predicted_proba_train = logreg.predict_proba(basis_x_train)
        train_avg_ce = log_loss(y_train.flatten(), predicted_proba_train)
        gaussian_data[str(sigma)]['train_accuracy'] = train_score
        gaussian_data[str(sigma)]['train_avg_ce'] = train_avg_ce
        test_score = logreg.score(basis_x_test, y_test.flatten())
        predicted_proba_test = logreg.predict_proba(basis_x_test)
        test_avg_ce = log_loss(y_test.flatten(), predicted_proba_test)
        gaussian_data[str(sigma)]['test_accuracy'] = test_score
        gaussian_data[str(sigma)]['test_avg_ce'] = test_avg_ce
    return gaussian_data
def plot(gaussian_data, sigmas, old_data):
    print("Sigma:", sigmas)
    train_ce = [gaussian_data[str(sigma)]['train_avg_ce'] for sigma in sigmas]
    test_ce = [gaussian_data[str(sigma)]['test_avg_ce'] for sigma in sigmas]
    print("Train avg. Cross-Entropy:", train_ce)
    print("Test avg. Cross-Entropy:", test_ce)
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.title('Train & Test Avg. Cross-Entropy')
    plt.plot(sigmas, train_ce, 'bo-', label='train gaussian')
    plt.plot(sigmas, test_ce, 'ro-', label='test gaussian')
    plt.plot(sigmas, [old_data['train_avg_ce'][0]] * len(sigmas), 'c-', label='train no regularization')
    plt.plot(sigmas, [old_data['test_avg_ce'][0]] * len(sigmas), 'm-', label='test no regularization')
    plt.xlabel('Sigma')
    plt.ylabel('Average Cross-Entropy')
    plt.ylim(-0.1, max(train_ce + test_ce + [old_data['train_avg_ce'][0]] + [old_data['test_avg_ce'][0]]) + 1)
    plt.legend()
    plt.subplot(1, 2, 2)
    train_acc = [gaussian_data[str(sigma)]['train_accuracy'] for sigma in sigmas]
    test_acc = [gaussian_data[str(sigma)]['test_accuracy'] for sigma in sigmas]
    print("Train accuracies:", train_acc)
    print("Test accuracies:", test_acc)
    plt.title('Train & Test Accuracies')
    plt.plot(sigmas, train_acc, 'bo-', label='train gaussian')
    plt.plot(sigmas, test_acc, 'ro-', label='test gaussian')
    plt.plot(sigmas, [old_data['train_accuracy'][0]] * len(sigmas), 'c-', label='train no regularization')
    plt.plot(sigmas, [old_data['test_accuracy'][0]] * len(sigmas), 'm-', label='test no regularization')
    plt.xlabel('Sigma')
    plt.ylabel('Accuracy')
    plt.ylim(0, 1.01)
    plt.legend(loc='lower right')
    plt.tight_layout()
    plt.show()