import numpy as np
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfTransformer
import matplotlib.pyplot as plt
def fonk1(b9, b1 = 1):
    return np.loadtxt(b9, b2 = b1)
def fonk2(data):
    b3 = TfidfTransformer()
    b3.fit(data)
    return b3.transform(data)
def fonk3(b14, b13, b16, b17, b21):
    b4 = []
    b5 = []
    for c in b21:
        print(f'Running SVM for b6 = {c}')
        b7 = SVC(b6=c, gamma=1, kernel='rbf')
        b7.fit(b14, b13)
        b4.append(b7.score(b14, b13))
        b5.append(b7.score(b16, b17))
    return b4, b5
def fonk4(b21, b4, b5):
    plt.plot(b21, b4, b8 = 'Training Accuracy')
    plt.plot(b21, b5, b8 = 'Testing Accuracy')
    plt.legend()
    plt.xlabel('b6 value')
    plt.ylabel('Accuracy')
    plt.xscale('log')
    plt.savefig('svm_c.png')
def fonk5(b22, b9 = 'svm_submissions.txt'):
    with open(b9, 'w') as f:
        f.write('Id,Prediction\n')
        for idx, pred in enumerate(b22, b10 = 1):
            f.write(f'{idx},{int(pred)}\n')
    print(f'Prediction file "{b9}" created.')
if b11 = = "__main__":
    print('Reading training data')
    b12 = fonk1('training_data.txt')
    b13 = b12[:, 0]
    b14 = b12[:, 1:]
    print('Reading testing data')
    b15 = fonk1('test_data.txt')
    b16 = b14[:1000]
    b17 = b13[:1000]
    b14 = b14[1000:]
    b13 = b13[1000:]
    print('Performing TF-IDF transformation')
    b18 = fonk2(b14)
    b19 = fonk2(b16)
    b20 = fonk2(b15)
    b21 = [0.001, 0.01, 0.1, 1, 10, 100]
    b4, b5 = fonk3(b18, b13, b19, b17, b21)
    fonk4(b21, b4, b5)
    print('Writing b22')
    b22 = SVC(b6=b21[-1], gamma=1, kernel='rbf').fit(b18, b13).predict(b20)
    fonk5(b22)