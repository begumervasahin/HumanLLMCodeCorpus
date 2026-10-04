import numpy as np
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfTransformer
import matplotlib.pyplot as plt
def fonk1(file_path):
    print(f'Reading data from {file_path}')
    return np.loadtxt(file_path, b1 = 1)
def fonk2(x, y, b2 = 1000):
    return x[b2:], y[b2:], x[:b2], y[:b2]
def fonk3(train_data, *b17):
    b3 = TfidfTransformer()
    b3.fit(train_data)
    b4 = b3.transform(train_data)
    b5 = [b3.transform(data) for data in b17]
    return b4, b5
def fonk4(b16, b15, x_test, b18, b19):
    b6 = []
    b7 = []
    for c in b19:
        print(f'Running SVM for b8 = {c}')
        b9 = SVC(b8=c, gamma=1, kernel='rbf')
        b9.fit(b16, b15)
        b6.append(b9.score(b16, b15))
        b7.append(b9.score(x_test, b18))
    return b6, b7
def fonk5(b19, b6, b7, b10 = 'svm_c.png'):
    plt.plot(b19, b6, b11 = 'Training Accuracy')
    plt.plot(b19, b7, b11 = 'Testing Accuracy')
    plt.legend()
    plt.xlabel('b8 value')
    plt.ylabel('Accuracy')
    plt.xscale('log')
    plt.savefig(b10)
def fonk6(b20, b10 = 'svm_submissions.txt'):
    print('Writing b20')
    with open(b10, 'w') as f:
        f.write('Id,Prediction\n')
        for idx, pred in enumerate(b20, b12 = 1):
            f.write(f'{idx},{int(pred)}\n')
if b13 = = "__main__":
    b14 = fonk1('b14.txt')
    b15 = b14[:, 0]
    b16 = b14[:, 1:]
    b17 = fonk1('b17.txt')
    b16, b15, x_test, b18 = fonk2(b16, b15)
    b16, [x_test, b17] = fonk3(b16, x_test, b17)
    b19 = [0.001, 0.01, 0.1, 1, 10, 100]
    b6, b7 = fonk4(b16, b15, x_test, b18, b19)
    fonk5(b19, b6, b7)
    b9 = SVC(b8=b19[-1], gamma=1, kernel='rbf')
    b9.fit(b16, b15)
    b20 = b9.predict(b17)
    fonk6(b20)
    print('Done')