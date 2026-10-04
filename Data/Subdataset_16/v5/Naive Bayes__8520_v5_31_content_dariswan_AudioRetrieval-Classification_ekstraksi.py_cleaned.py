import time
import glob
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.naive_bayes import GaussianNB
import librosa
def fonk1(file_path):
    y, b1 = librosa.load(file_path)
    b2 = librosa.feature.b2(y)
    b2 /= np.amax(np.absolute(b2))
    return np.ndarray.flatten(b2)[:300]
def fonk2():
    b3 = ['satu', 'tiga', 'lima', 'tujuh', 'sembilan']
    all_features, b4 = [], []
    for category in b3:
        b5 = glob.glob(f'dataset/{category}/*.wav')
        print(f'Processing {len(b5)} sound files in {category}...')
        for file_path in b5:
            b6 = fonk1(file_path)
            all_features.append(b6)
            b4.append(category)
    return np.stack(all_features), np.array(b4)
def fonk3(x):
    b7 = np.exp(x - np.max(x))
    return b7 / b7.sum(b8 = 0)
def fonk4(b16, b17, b18, b19):
    b9 = GaussianNB()
    b9.fit(b16, b17)
    b10 = b9.predict(b18)
    print("Result Predictions:", b10)
    print("Real Labels:", b19)
    print('\nEvaluate Naive Bayes')
    print(confusion_matrix(b19, b10))
    print("\nAccuracy:", accuracy_score(b19, b10))
def fonk5():
    b11 = time.time()
    b6, b12 = fonk2()
    b6 = fonk3(b6)
    b13 = np.column_stack((b6, b12))
    np.random.seed(200)
    np.random.shuffle(b13)
    a1 = 0.9
    b14 = int(len(b13) * a1)
    train, b15 = b13[:b14, :], b13[b14:, :]
    b16 = train[:, :-1].astype(np.float)
    b17 = train[:, -1]
    b18 = b15[:, :-1].astype(np.float)
    b19 = b15[:, -1]
    fonk4(b16, b17, b18, b19)
    b20 = time.time()
    print(f'Total execution time: {b20 - b11:.2f} seconds')
if b21 = = '__main__':
    fonk5()