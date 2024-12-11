import time
import glob
import numpy as np
import librosa
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
b1 = time.time()
def fonk1(file_path):
    y, b2 = librosa.load(file_path)
    b3 = librosa.feature.b3(y)
    b3 /= np.amax(np.absolute(b3))
    return np.ndarray.flatten(b3)[:300]
def fonk2():
    b4 = []
    b5 = []
    b6 = ['satu', 'tiga', 'lima', 'tujuh', 'sembilan']
    for number in b6:
        b7 = glob.glob(f'dataset/{number}/*.wav')
        print(f'Processing {len(b7)} sound files for number {number} ...')
        for file in b7:
            b8 = fonk1(file)
            b4.append(b8)
            b5.append(number)
    return np.array(b4), np.array(b5)
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
train_data, b14 = b12[:b13], b12[b13:]
train_input, b15 = train_data[:, :-1].astype(np.float), train_data[:, -1]
test_input, b16 = b14[:, :-1].astype(np.float), b14[:, -1]
def fonk4():
    b17 = GaussianNB()
    b17.fit(train_input, b15)
    b18 = b17.predict(test_input)
    print("Predicted Labels:", b18)
    print("Actual Labels:", b16)
    print('\nEvaluation Results for Naive Bayes:')
    print(confusion_matrix(b16, b18))
    print("\nAccuracy:", accuracy_score(b16, b18))
fonk4()
b19 = time.time()
print("Time taken:", b19 - b1)