import time
import glob
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.naive_bayes import GaussianNB
import librosa
def extract_feature_audio(file_path):
    y, _ = librosa.load(file_path)
    mfcc = librosa.feature.mfcc(y)
    mfcc /= np.amax(np.absolute(mfcc))
    return np.ndarray.flatten(mfcc)[:300]
def generate_features_and_labels():
    categories = ['satu', 'tiga', 'lima', 'tujuh', 'sembilan']
    all_features, all_labels = [], []
    for category in categories:
        sound_files = glob.glob(f'dataset/{category}/*.wav')
        print(f'Processing {len(sound_files)} sound files in {category}...')
        for file_path in sound_files:
            features = extract_feature_audio(file_path)
            all_features.append(features)
            all_labels.append(category)
    return np.stack(all_features), np.array(all_labels)
def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)
def predict_all(train_input, train_labels, test_input, test_labels):
    nb = GaussianNB()
    nb.fit(train_input, train_labels)
    predictions = nb.predict(test_input)
    print("Result Predictions:", predictions)
    print("Real Labels:", test_labels)
    print('\nEvaluate Naive Bayes')
    print(confusion_matrix(test_labels, predictions))
    print("\nAccuracy:", accuracy_score(test_labels, predictions))
def main():
    start = time.time()
    features, labels = generate_features_and_labels()
    features = softmax(features)
    all_data = np.column_stack((features, labels))
    np.random.seed(200)
    np.random.shuffle(all_data)
    training_split = 0.9
    split_idx = int(len(all_data) * training_split)
    train, test = all_data[:split_idx, :], all_data[split_idx:, :]
    train_input = train[:, :-1].astype(np.float)
    train_labels = train[:, -1]
    test_input = test[:, :-1].astype(np.float)
    test_labels = test[:, -1]
    predict_all(train_input, train_labels, test_input, test_labels)
    end = time.time()
    print(f'Total execution time: {end - start:.2f} seconds')
if __name__ == '__main__':
    main()