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
    b7, b5 = b3[:1000], b2[:1000]
    b3, b2 = b3[1000:], b2[1000:]
    b6 = StandardScaler()
    b3 = b6.fit_transform(b3)
    b7 = b6.transform(b7)
    b4 = b6.transform(b4)
    b8 = TfidfTransformer()
    b3 = b8.fit_transform(b3)
    b7 = b8.transform(b7)
    b4 = b8.transform(b4)
    return b3, b2, b7, b5, b4
def fonk2(b3, b2, b7, b5):
    b9 = []
    b10 = []
    b11 = [0.001, 0.01, 0.1, 1, 10, 100]
    for c in b11:
        print(f'Running SVM for b12 = {c}')
        b13 = SVC(b12=c, gamma='auto', kernel='rbf')
        b13.fit(b3, b2)
        print('Evaluating scores')
        b10.append(b13.score(b3, b2))
        b9.append(b13.score(b7, b5))
    fonk3(b11, b10, b9)
    return b13
def fonk3(b11, b10, b9):
    plt.figure(b14 = (10, 6))
    plt.plot(b11, b10, b15 = 'Training Accuracy')
    plt.plot(b11, b9, b15 = 'Testing Accuracy')
    plt.legend()
    plt.xlabel('b12 value')
    plt.ylabel('Accuracy')
    plt.xscale('log')
    plt.savefig('svm_c.png')
    plt.show()
def fonk4(b13, b4):
    print('Writing predictions')
    b16 = b13.predict(b4)
    with open('svm_submissions.txt', 'w') as f:
        f.write('Id,Prediction\n')
        for it, pred in enumerate(b16, b17 = 1):
            f.write(f'{it},{int(pred)}\n')
    print('Predictions written to svm_submissions.txt')
def fonk5():
    b3, b2, b7, b5, b4 = fonk1()
    b13 = fonk2(b3, b2, b7, b5)
    fonk4(b13, b4)
if b18 = = "__main__":
    fonk5()