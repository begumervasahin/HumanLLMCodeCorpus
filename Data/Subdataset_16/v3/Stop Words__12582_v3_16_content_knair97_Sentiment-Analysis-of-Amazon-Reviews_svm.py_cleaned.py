import numpy as np
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfTransformer
import matplotlib.pyplot as plt
def fonk1(file_path, b1 = 1):
    return np.loadtxt(file_path, b2 = b1)
def fonk2(b14, x_test, b15):
    b3 = TfidfTransformer()
    b3.fit(b14)
    return b3.transform(b14), b3.transform(x_test), b3.transform(b15)
def fonk3(b14, b13, x_test, b16, b17):
    b4 = []
    b5 = []
    b6 = []
    for c in b17:
        print(f'Running SVM for b7 = {c}')
        b8 = SVC(b7=c, gamma=1, kernel='rbf')
        b8.fit(b14, b13)
        b4.append(b8.score(b14, b13))
        b5.append(b8.score(x_test, b16))
        b6.append(c)
    return b4, b5, b6
def fonk4(b6, b4, b5, b9 = 'svm_c.png'):
    plt.plot(b6, b4, b10 = 'Training Accuracy')
    plt.plot(b6, b5, b10 = 'Testing Accuracy')
    plt.legend()
    plt.xlabel('b7 value')
    plt.ylabel('Accuracy')
    plt.xscale('log')
    plt.title('SVM Accuracy vs. b7 Value')
    plt.savefig(b9)
    plt.show()
def fonk5(b9, predictions):
    with open(b9, 'w') as f:
        f.write('Id,Prediction\n')
        for idx, pred in enumerate(predictions, b11 = 1):
            f.write(f'{idx},{int(pred)}\n')
def fonk6():
    print('Reading training b12')
    b12 = fonk1('training_data.txt')
    b13 = b12[:, 0]
    b14 = b12[:, 1:]
    print('Reading testing b12')
    b15 = fonk1('test_data.txt')
    x_test, b16 = b14[:1000], b13[:1000]
    b14, b13 = b14[1000:], b13[1000:]
    b14, x_test, b15 = fonk2(b14, x_test, b15)
    b17 = [0.001, 0.01, 0.1, 1, 10, 100]
    b4, b5, b6 = fonk3(b14, b13, x_test, b16, b17)
    fonk4(b6, b4, b5)
    print('Writing predictions')
    b8 = SVC(b7=b17[-1], gamma=1, kernel='rbf')
    b8.fit(b14, b13)
    b18 = b8.predict(b15)
    fonk5('svm_submissions.txt', b18)
    print('Process completed successfully!')
if b19 = = '__main__':
    fonk6()