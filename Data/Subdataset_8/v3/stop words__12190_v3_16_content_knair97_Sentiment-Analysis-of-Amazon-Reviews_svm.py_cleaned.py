import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfTransformer
import matplotlib.pyplot as plt
def load_and_preprocess_data():
    print('Reading training data')
    data = np.loadtxt('training_data.txt', skiprows=1)
    y_train = data[:, 0]
    x_train = data[:, 1:]
    print('Reading testing data')
    test_data = np.loadtxt('test_data.txt', skiprows=1)
    x_test, y_test = x_train[:1000], y_train[:1000]
    x_train, y_train = x_train[1000:], y_train[1000:]
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)
    test_data_scaled = scaler.transform(test_data)
    tfidf = TfidfTransformer()
    x_train_tfidf = tfidf.fit_transform(x_train_scaled)
    x_test_tfidf = tfidf.transform(x_test_scaled)
    test_data_tfidf = tfidf.transform(test_data_scaled)
    return x_train_tfidf, y_train, x_test_tfidf, y_test, test_data_tfidf
def run_svm_and_evaluate(x_train, y_train, x_test, y_test):
    test_errors = []
    train_errors = []
    c_values = [0.001, 0.01, 0.1, 1, 10, 100]
    for c in c_values:
        print(f'Running SVM for C = {c}')
        clf = SVC(C=c, gamma='auto', kernel='rbf')
        clf.fit(x_train, y_train)
        print('Evaluating scores')
        train_accuracy = clf.score(x_train, y_train)
        test_accuracy = clf.score(x_test, y_test)
        train_errors.append(train_accuracy)
        test_errors.append(test_accuracy)
    plot_accuracy_vs_c(c_values, train_errors, test_errors)
    return clf
def plot_accuracy_vs_c(c_values, train_errors, test_errors):
    plt.figure(figsize=(10, 6))
    plt.plot(c_values, train_errors, label='Training Accuracy')
    plt.plot(c_values, test_errors, label='Testing Accuracy')
    plt.legend()
    plt.xlabel('C value')
    plt.ylabel('Accuracy')
    plt.xscale('log')
    plt.savefig('svm_c.png')
    plt.show()
def write_predictions(clf, test_data):
    print('Writing predictions')
    preds = clf.predict(test_data)
    with open('svm_submissions.txt', 'w') as f:
        f.write('Id,Prediction\n')
        for idx, pred in enumerate(preds, start=1):
            f.write(f'{idx},{int(pred)}\n')
    print('Predictions written to svm_submissions.txt')
def main():
    x_train, y_train, x_test, y_test, test_data = load_and_preprocess_data()
    clf = run_svm_and_evaluate(x_train, y_train, x_test, y_test)
    write_predictions(clf, test_data)
if __name__ == "__main__":
    main()