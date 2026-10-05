import numpy as np
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfTransformer
import matplotlib.pyplot as plt
def load_data(file_path, skip_rows=1):
    return np.loadtxt(file_path, skiprows=skip_rows)
def perform_tfidf_transformation(data):
    tfidf = TfidfTransformer()
    tfidf.fit(data)
    return tfidf.transform(data)
def run_svm(x_train, y_train, x_test, y_test, c_values):
    train_errors = []
    test_errors = []
    for c in c_values:
        print(f'Running SVM for C = {c}')
        svm_classifier = SVC(C=c, gamma=1, kernel='rbf')
        svm_classifier.fit(x_train, y_train)
        train_errors.append(svm_classifier.score(x_train, y_train))
        test_errors.append(svm_classifier.score(x_test, y_test))
    return train_errors, test_errors
def plot_accuracy(c_values, train_errors, test_errors):
    plt.plot(c_values, train_errors, label='Training Accuracy')
    plt.plot(c_values, test_errors, label='Testing Accuracy')
    plt.legend()
    plt.xlabel('C value')
    plt.ylabel('Accuracy')
    plt.xscale('log')
    plt.savefig('svm_c.png')
def write_predictions(predictions, file_path='svm_submissions.txt'):
    with open(file_path, 'w') as f:
        f.write('Id,Prediction\n')
        for idx, pred in enumerate(predictions, start=1):
            f.write(f'{idx},{int(pred)}\n')
    print(f'Prediction file "{file_path}" created.')
if __name__ == "__main__":
    print('Reading training data')
    data_train = load_data('training_data.txt')
    y_train = data_train[:, 0]
    x_train = data_train[:, 1:]
    print('Reading testing data')
    data_test = load_data('test_data.txt')
    x_test = x_train[:1000]
    y_test = y_train[:1000]
    x_train = x_train[1000:]
    y_train = y_train[1000:]
    print('Performing TF-IDF transformation')
    x_train_tfidf = perform_tfidf_transformation(x_train)
    x_test_tfidf = perform_tfidf_transformation(x_test)
    test_tfidf = perform_tfidf_transformation(data_test)
    c_values = [0.001, 0.01, 0.1, 1, 10, 100]
    train_errors, test_errors = run_svm(x_train_tfidf, y_train, x_test_tfidf, y_test, c_values)
    plot_accuracy(c_values, train_errors, test_errors)
    print('Writing predictions')
    predictions = SVC(C=c_values[-1], gamma=1, kernel='rbf').fit(x_train_tfidf, y_train).predict(test_tfidf)
    write_predictions(predictions)