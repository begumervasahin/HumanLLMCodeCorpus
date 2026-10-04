from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.metrics import log_loss
import matplotlib.pyplot as plt
def fonk1(gaussian_data, y_train, y_test, sigmas, b1 = 10000, use_sgd=True):
    print "\nLogistic Regression on data applied to gaussian basis functions (no regularization)..."
    for sigma in sigmas:
        b2 = gaussian_data[str(sigma)]['x_train']
        b3 = gaussian_data[str(sigma)]['x_test']
        if use_sgd: b4 = SGDClassifier(loss='log', penalty='none', b1=b1, shuffle=False)
        else: b4 = LogisticRegression(penalty='l2', C=1.e12, max_iter=b1)
        b4.fit(b2, y_train.flatten())
        b5 = b4.b5(b2, y_train.flatten())
        gaussian_data[str(sigma)]['train_accuracy'] = b5
        b6 = b4.predict_proba(b2)
        b7 = log_loss(y_train.flatten(), b6)
        gaussian_data[str(sigma)]['train_avg_ce'] = b7
        b5 = b4.b5(b3, y_test.flatten())
        gaussian_data[str(sigma)]['test_accuracy'] = b5
        b6 = b4.predict_proba(b3)
        b7 = log_loss(y_test.flatten(), b6)
        gaussian_data[str(sigma)]['test_avg_ce'] = b7
    return gaussian_data
def fonk2(gaussian_data, sigmas, old_data):
    print "Sigma:", sigmas
    b8 = [gaussian_data[str(sigma)]['train_avg_ce'] for sigma in sigmas]
    b9 = [gaussian_data[str(sigma)]['test_avg_ce'] for sigma in sigmas]
    print "Train avg. Cross-Entropy:", b8
    print "Test avg. Cross-Entropy:", b9
    plt.title('QUESTION 1.f)\nTrain & Test Avg. Cross-Entropy')
    train_line, = plt.fonk2(sigmas, b8, 'bo-')
    test_line, = plt.fonk2(sigmas, b9, 'ro-')
    train_line_old, = plt.fonk2(sigmas, [old_data['train_avg_ce'][0]]*len(sigmas), 'c-')
    test_line_old, = plt.fonk2(sigmas, [old_data['test_avg_ce'][0]]*len(sigmas), 'm-')
    plt.legend(
        [train_line, test_line, train_line_old, test_line_old],
        ['train gaussian', 'test gaussian', 'train no regularization', 'test no regularization']
    )
    plt.xlabel('sigma')
    plt.ylabel('average cross-entropy')
    plt.ylim(-0.1, max(b8+b9+[old_data['train_avg_ce'][0]]+[old_data['test_avg_ce'][0]])+1)
    plt.show()
    b10 = [gaussian_data[str(sigma)]['train_accuracy'] for sigma in sigmas]
    b11 = [gaussian_data[str(sigma)]['test_accuracy'] for sigma in sigmas]
    print "Train accuracies:", b10
    print "Test accuracies:", b11
    plt.title('QUESTION 1.f)\nTrain & Test Accuracies')
    train_line, = plt.fonk2(sigmas, b10, 'bo-')
    test_line, = plt.fonk2(sigmas, b11, 'ro-')
    train_line_old, = plt.fonk2(sigmas, [old_data['train_accuracy'][0]]*len(sigmas), 'c-')
    test_line_old, = plt.fonk2(sigmas, [old_data['test_accuracy'][0]]*len(sigmas), 'm-')
    plt.legend(
        [train_line, test_line, train_line_old, test_line_old],
        ['train gaussian', 'test gaussian', 'train no regularization', 'test no regularization'],
        b12 = 'lower right'
    )
    plt.xlabel('sigma')
    plt.ylim(0, 1.01)
    plt.ylabel('accuracy')
    plt.show()