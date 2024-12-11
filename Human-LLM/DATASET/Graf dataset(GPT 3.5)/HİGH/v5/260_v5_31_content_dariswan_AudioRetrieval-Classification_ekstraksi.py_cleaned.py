import time
import glob
import numpy as np
import librosa
import librosa.feature
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
b1 = time.time()
def fonk1(file):
    y, b2 = librosa.load(file)
    b3 = librosa.feature.b3(y)
    b3 /= np.amax(np.absolute(b3))
    return np.ndarray.flatten(b3)[:300]
def fonk2():
    b4 = []
    b5 = []
    b6 = ['satu', 'tiga', 'lima', 'tujuh', 'sembilan']
    for odd_number in b6:
        b7 = glob.glob('dataset/' + odd_number + '/*.wav')
        print('Processing %d sound files in %s ...' % (len(b7), odd_number))
        for file in b7:
            b8 = fonk1(file)
            b4.append(b8)
            b5.append(odd_number)
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
b13 = int(len(b12) * a1)
train_data, b14 = b12[:b13, :], b12[b13:, :]
b15 = train_data[:, :-256].astype(np.float)
b16 = train_data[:, -1:]
b17 = b14[:, :-256].astype(np.float)
b18 = b14[:, -1:]
def fonk4():
    b19 = GaussianNB()
    b19.fit(b15, b16)
    b20 = b19.predict(b17)
    print("Predicted Labels:", b20)
    print("True Labels:", b18)
    print('\nEvaluate Naive Bayes')
    print(confusion_matrix(b18, b20))
    print("\nAccuracy:", accuracy_score(b18, b20))
fonk4()
b21 = time.time()
print("Execution Time:", b21 - b1)