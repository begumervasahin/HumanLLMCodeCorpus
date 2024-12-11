import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfTransformer
import matplotlib.pyplot as plt
def fonk1():
    print('Reading training b1')
    b1 = np.loadtxt('training_data.txt', skiprows=1)
    b2 = b1[:, 0]
    b3 = b1[:, 1:]
    print('Reading testing b1')
    b4 = np.loadtxt('b4.txt', skiprows=1)
    x_test, b5 = b3[:1000], b2[:1000]
    b3, b2 = b3[1000:], b2[1000:]
    b6 = StandardScaler()
    b7 = b6.fit_transform(b3)
    b8 = b6.transform(x_test)
    b9 = b6.transform(b4)
    b10 = TfidfTransformer()
    b11 = b10.fit_transform(b7)
    b12 = b10.transform(b8)
    b13 = b10.transform(b9)
    return b11, b2, b12, b5, b13
def fonk2(b3, b2, x_test, b5):
    b14 = []
    b15 = []
    b16 = [0.001, 0.01, 0.1, 1, 10, 100]
    for c in b16:
        print(f'Running SVM for b17 = {c}')
        b18 = SVC(b17=c, gamma='auto', kernel='rbf')
        b18.fit(b3, b2)
        print('Evaluating scores')
        b19 = b18.score(b3, b2)
        b20 = b18.score(x_test, b5)
        b15.append(b19)
        b14.append(b20)
    fonk3(b16, b15, b14)
    return b18
def fonk3(b16, b15, b14):
    plt.figure(b21 = (10, 6))
    plt.plot(b16, b15, b22 = 'Training Accuracy')
    plt.plot(b16, b14, b22 = 'Testing Accuracy')
    plt.legend()
    plt.xlabel('b17 value')
    plt.ylabel('Accuracy')
    plt.xscale('log')
    plt.savefig('svm_c.png')
    plt.show()
def fonk4(b18, b4):
    print('Writing predictions')
    b23 = b18.predict(b4)
    with open('svm_submissions.txt', 'w') as f:
        f.write('Id,Prediction\n')
        for idx, pred in enumerate(b23, b24 = 1):
            f.write(f'{idx},{int(pred)}\n')
    print('Predictions written to svm_submissions.txt')
def fonk5():
    b3, b2, x_test, b5, b4 = fonk1()
    b18 = fonk2(b3, b2, x_test, b5)
    fonk4(b18, b4)
if b25 = = "__main__":
    fonk5()