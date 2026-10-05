import time
import glob
import numpy as np
import librosa
import librosa.feature
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
start_time = time.time()
def extract_audio_features(file):
    y, _ = librosa.load(file)
    mfcc = librosa.feature.mfcc(y)
    mfcc /= np.amax(np.absolute(mfcc))
    return np.ndarray.flatten(mfcc)[:300]
def generate_features_and_labels():
    all_features = []
    all_labels = []
    odd_numbers = ['satu', 'tiga', 'lima', 'tujuh', 'sembilan']
    for odd_number in odd_numbers:
        sound_files = glob.glob('dataset/' + odd_number + '/*.wav')
        print('Processing %d sound files in %s ...' % (len(sound_files), odd_number))
        for file in sound_files:
            features = extract_audio_features(file)
            all_features.append(features)
            all_labels.append(odd_number)
    return np.stack(all_features), all_labels
def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)
features, labels = generate_features_and_labels()
features = softmax(features)
all_data = np.column_stack((features, labels))
np.random.seed(200)
np.random.shuffle(all_data)
training_split = 0.9
split_index = int(len(all_data) * training_split)
train_data, test_data = all_data[:split_index, :], all_data[split_index:, :]
train_input = train_data[:, :-256].astype(np.float)
train_labels = train_data[:, -1:]
test_input = test_data[:, :-256].astype(np.float)
test_labels = test_data[:, -1:]
def predict_all():
    nb = GaussianNB()
    nb.fit(train_input, train_labels)
    predictions = nb.predict(test_input)
    print("Predicted Labels:", predictions)
    print("True Labels:", test_labels)
    print('\nEvaluate Naive Bayes')
    print(confusion_matrix(test_labels, predictions))
    print("\nAccuracy:", accuracy_score(test_labels, predictions))
predict_all()
end_time = time.time()
print("Execution Time:", end_time - start_time)