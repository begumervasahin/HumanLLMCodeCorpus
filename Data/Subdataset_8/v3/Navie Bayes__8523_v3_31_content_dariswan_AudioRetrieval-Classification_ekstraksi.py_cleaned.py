import time
import glob
import numpy as np
import librosa
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
start_time = time.time()
def extract_mfcc_features(file_path):
    y, _ = librosa.load(file_path)
    mfcc = librosa.feature.mfcc(y)
    mfcc /= np.amax(np.absolute(mfcc))
    return np.ndarray.flatten(mfcc)[:300]
def load_audio_data():
    all_features = []
    all_labels = []
    ganjil_numbers = ['satu', 'tiga', 'lima', 'tujuh', 'sembilan']
    for number in ganjil_numbers:
        sound_files = glob.glob(f'dataset/{number}/*.wav')
        print(f'Processing {len(sound_files)} sound files for number {number} ...')
        for file in sound_files:
            features = extract_mfcc_features(file)
            all_features.append(features)
            all_labels.append(number)
    return np.array(all_features), np.array(all_labels)
def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)
features, labels = load_audio_data()
features = softmax(features)
data = np.column_stack((features, labels))
np.random.seed(200)
np.random.shuffle(data)
training_ratio = 0.9
split_idx = int(len(data) * training_ratio)
train_data, test_data = data[:split_idx], data[split_idx:]
train_input, train_labels = train_data[:, :-1].astype(np.float), train_data[:, -1]
test_input, test_labels = test_data[:, :-1].astype(np.float), test_data[:, -1]
def predict_and_evaluate():
    nb_classifier = GaussianNB()
    nb_classifier.fit(train_input, train_labels)
    predictions = nb_classifier.predict(test_input)
    print("Predicted Labels:", predictions)
    print("Actual Labels:", test_labels)
    print('\nEvaluation Results for Naive Bayes:')
    print(confusion_matrix(test_labels, predictions))
    print("\nAccuracy:", accuracy_score(test_labels, predictions))
predict_and_evaluate()
end_time = time.time()
print("Time taken:", end_time - start_time)