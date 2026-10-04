import time
import librosa
import glob
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.naive_bayes import GaussianNB
b1 = time.time()
def fonk1(f):
    y, b2 = librosa.load(f)
import time
import librosa
import glob
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.naive_bayes import GaussianNB
b1 = time.time()
def fonk2(f):
    y, b2 = librosa.load(f)
    b3 = librosa.feature.b3(y)
    b3 /= np.amax(np.absolute(b3))
    return np.ndarray.flatten(b3)[:300]
def fonk3():
    b4 = []
    b5 = []
    b6 = ['satu','tiga','lima','tujuh','sembilan']
    for ganjil in b6:
        b7 = glob.glob('dataset/' + ganjil + '/*.wav')
        print('Processing %d sound files in %s ...' % (len(b7), ganjil))
        for f in b7:
            b8 = fonk2(f)
            b4.append(b8)
            b5.append(ganjil)
    return np.stack(b4), b5
def fonk4(x):
    b9 = np.exp(x - np.max(x))
    return b9 / b9.sum(b10 = 0)
b8, b11 = fonk3()
b8 = fonk4(b8)
b12 = np.column_stack((b8, b11))
np.random.seed(200)
np.random.shuffle(b12)
a1 = 0.9
b13 = int(len(b12) * a1)
train, b14 = b12[:b13, :], b12[b13:, :]
b15 = train[:, :-1].astype(np.float)
b16 = train[:, -1]
b17 = b14[:, :-1].astype(np.float)
b18 = b14[:, -1]
def fonk5():
    b19 = GaussianNB()
    b19.fit(b15, b16)
    b20 = b19.predict(b17)
    print("Result Prediction: ", b20)
    print("Real label data: ", b18)
    print('\nEvaluate Naive Bayes')
    print(confusion_matrix(b18, b20))
    print("\nAccuracy: ", accuracy_score(b18, b20))
fonk5()
b21 = time.time()
print("Execution time: ", b21 - b1)