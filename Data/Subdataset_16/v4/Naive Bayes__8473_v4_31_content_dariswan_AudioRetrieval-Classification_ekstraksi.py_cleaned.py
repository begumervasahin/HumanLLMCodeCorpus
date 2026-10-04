import time
import glob
import numpy as np
import sklearn.metrics
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
import librosa
import librosa.feature
def fonk1(file_path):
    y, b1 = librosa.load(file_path)
    b2 = librosa.feature.b2(y)
    b2 /= np.amax(np.absolute(b2))
    return np.ndarray.flatten(b2)[:300]
def fonk2():
    b3 = []
    b4 = []
    b5 = ['satu', 'tiga', 'lima', 'tujuh', 'sembilan']
    for category in b5:
        b6 = glob.glob(f'dataset/{category}/*.wav')
        print(f'Processing {len(b6)} sound files in {category}...')
        for file_path in b6:
            b7 = fonk1(file_path)
            b3.append(b7)
            b4.append(category)
    return np.stack(b3), b4
def fonk3(x):
    b8 = np.exp(x - np.max(x))
    return b8 / b8.sum(b9 = 0)
b10 = time.time()
b7, b11 = fonk2()
b7 = fonk3(b7)
b12 = np.column_stack((b7, b11))
np.random.seed(200)
np.random.shuffle(b12)
a1 = 0.9
b13 = int(len(b12) * a1)
train, b14 = b12[:b13, :], b12[b13:, :]
b15 = train[:, :-1].astype(np.float)
b16 = train[:, -1]
b17 = b14[:, :-1].astype(np.float)
b18 = b14[:, -1]
def fonk4():
    b19 = GaussianNB()
    b19.fit(b15, b16)
    b20 = b19.predict(b17)
    print("Result Predictions:", b20)
    print("Real Labels:", b18)
    print('\nEvaluate Naive Bayes')
    print(confusion_matrix(b18, b20))
    print("\nAccuracy:", sklearn.metrics.accuracy_score(b18, b20))
fonk4()
b21 = time.time()
print(f'Total execution time: {b21 - b10:.2f} seconds')