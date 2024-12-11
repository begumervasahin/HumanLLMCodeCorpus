import time
import librosa
import librosa.feature
import glob
import numpy as np
import sklearn.metrics
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
b1 = time.time()
def fonk1(f):
    y, b2 = librosa.load(f)
    b3 = librosa.feature.b3(y)
    b3 /= np.amax(np.absolute(b3))
    return np.ndarray.flatten(b3)[:300]
def fonk2():
    b4 = []
    b5 = []
    b6 = ['satu', 'tiga', 'lima', 'tujuh', 'sembilan']
    for ganjil in b6:
        b7 = glob.glob('dataset/'+ganjil+'/*.wav')
        print('Processing %d sound in %s ...' % (len(b7), ganjil))
        for f in b7:
            b8 = fonk1(f)
            b4.append(b8)
            b5.append(ganjil)
    return np.stack(b4), b5
def fonk3(x):
    b9 = np.exp(x - np.max(x))
    return b9 / b9.sum(b10 = 0)
b8, b11 = fonk2()
b8 = fonk3(b8)
b12 = np.column_stack((b8, b11))
np.random.seed(200)
np.random.shuffle(b12)
a1 = 0.9
b13 = int(len(b12)*a1)
train, b14 = b12[:b13, :], b12[b13:, :]
b15 = train[:, :-256]
b15 = b15.astype(np.float)
b16 = train[:, -1:]
b17 = b14[:, :-256]
b17 = b17.astype(np.float)
b18 = b14[:, -1:]
def fonk4():
    b19 = GaussianNB()
    b19.fit(b15, b16)
    b20 = b19.predict(b17)
    print("Result Prediction :", b20)
    print("Real label data :", b18)
    print('\nEvaluate Naive Bayes')
    print(confusion_matrix(b18, b20))
    print("\nAkurasi : ", sklearn.metrics.accuracy_score(b18, b20))
fonk4()
b21 = time.time()
print("Time taken: ", b21 - b1)