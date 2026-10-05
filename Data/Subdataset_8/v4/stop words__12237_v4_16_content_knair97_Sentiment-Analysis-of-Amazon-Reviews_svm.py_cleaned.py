import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import StratifiedKFold
import matplotlib.pyplot as plt
print('Reading training data')
data = np.loadtxt('training_data.txt', skiprows=1)
y_train = data[:, 0]
x_train = data[:, 1:]
print('Reading testing data')
test = np.loadtxt('test_data.txt', skiprows=1)
x_test = x_train[:1000]
y_test = y_train[:1000]
x_train = x_train[1000:]
y_train = y_train[1000:]
print('Performing TF-IDF transformation')
tfidf = TfidfTransformer()
tfidf.fit(x_train)
x_train = tfidf.transform(x_train)
x_test = tfidf.transform(x_test)
test = tfidf.transform(test)
test_err = []
train_err = []
c_values = []
for c in [0.001, 0.01, 0.1, 1, 10, 100]:
    print('Running SVM for C =', c)
    svm_classifier = SVC(C=c, gamma=1, kernel='rbf')
    svm_classifier.fit(x_train, y_train)
    print('Evaluating scores')
    train_err.append(svm_classifier.score(x_train, y_train))
    test_err.append(svm_classifier.score(x_test, y_test))
    c_values.append(c)
plt.plot(c_values, train_err, label='Training Accuracy')
plt.plot(c_values, test_err, label='Testing Accuracy')
plt.legend()
plt.xlabel('C value')
plt.ylabel('Accuracy')
plt.xscale('log')
plt.savefig('svm_c.png')
print('Writing predictions')
predictions = svm_classifier.predict(test)
with open('svm_submissions.txt', 'w') as f:
    f.write('Id,Prediction\n')
    for idx, pred in enumerate(predictions, start=1):
        f.write(f'{idx},{int(pred)}\n')
print('Prediction file "svm_submissions.txt" created.')