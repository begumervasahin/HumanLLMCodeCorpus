import numpy as np
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfTransformer
import matplotlib.pyplot as plt
def load_data(file_path, skip_rows=1):
    return np.loadtxt(file_path, skiprows=skip_rows)
def apply_tfidf_transformation(x_train, x_test, test):
    tfidf = TfidfTransformer()
    tfidf.fit(x_train)
    return tfidf.transform(x_train), tfidf.transform(x_test), tfidf.transform(test)
def train_and_evaluate_svm(x_train, y_train, x_test, y_test, c_values):
    train_err = []
    test_err = []
    c_val = []
    for c in c_values:
        print(f'Running SVM for C = {c}')
        clf = SVC(C=c, gamma=1, kernel='rbf')
        clf.fit(x_train, y_train)
        train_err.append(clf.score(x_train, y_train))
        test_err.append(clf.score(x_test, y_test))
        c_val.append(c)
    return train_err, test_err, c_val
def plot_results(c_val, train_err, test_err, filename='svm_c.png'):
    plt.plot(c_val, train_err, label='Training Accuracy')
    plt.plot(c_val, test_err, label='Testing Accuracy')
    plt.legend()
    plt.xlabel('C value')
    plt.ylabel('Accuracy')
    plt.xscale('log')
    plt.title('SVM Accuracy vs. C Value')
    plt.savefig(filename)
    plt.show()
def write_predictions(filename, predictions):
    with open(filename, 'w') as f:
        f.write('Id,Prediction\n')
        for idx, pred in enumerate(predictions, start=1):
            f.write(f'{idx},{int(pred)}\n')
def main():
    print('Reading training data')
    data = load_data('training_data.txt')
    y_train = data[:, 0]
    x_train = data[:, 1:]
    print('Reading testing data')
    test = load_data('test_data.txt')
    x_test, y_test = x_train[:1000], y_train[:1000]
    x_train, y_train = x_train[1000:], y_train[1000:]
    x_train, x_test, test = apply_tfidf_transformation(x_train, x_test, test)
    c_values = [0.001, 0.01, 0.1, 1, 10, 100]
    train_err, test_err, c_val = train_and_evaluate_svm(x_train, y_train, x_test, y_test, c_values)
    plot_results(c_val, train_err, test_err)
    print('Writing predictions')
    clf = SVC(C=c_values[-1], gamma=1, kernel='rbf')
    clf.fit(x_train, y_train)
    preds = clf.predict(test)
    write_predictions('svm_submissions.txt', preds)
    print('Process completed successfully!')
if __name__ == '__main__':
    main()