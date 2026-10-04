
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from keras.models import Sequential
from keras.layers import Dense
from math import log
def load_and_preprocess_data(filename):
    dataset = pd.read_csv(filename)
    attack_types = [
        'back.', 'buffer_overflow.', 'ftp_write.', 'guess_passwd.', 'imap.', 'ipsweep.',
        'land.', 'loadmodule.', 'multihop.', 'neptune.', 'nmap.', 'perl.', 'phf.',
        'pod.', 'portsweep.', 'rootkit.', 'satan.', 'smurf.', 'spy.', 'teardrop.',
        'warezclient.', 'warezmaster.'
    ]
    dataset['normal.'] = dataset['normal.'].replace(attack_types, 'attack')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    label_encoders = [LabelEncoder() for _ in range(3)]
    for i in range(1, 4):
        X[:, i] = label_encoders[i - 1].fit_transform(X[:, i])
    onehot_encoders = [OneHotEncoder(categorical_features=[i]) for i in [1, 4, 70]]
    for encoder in onehot_encoders:
        X = encoder.fit_transform(X).toarray()
    label_encoder_y = LabelEncoder()
    y = label_encoder_y.fit_transform(y)
    return X, y
def build_ann(input_dim):
    model = Sequential()
    model.add(Dense(units=60, kernel_initializer='uniform', activation='relu', input_dim=input_dim))
    model.add(Dense(units=60, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(units=60, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(units=1, kernel_initializer='uniform', activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model
def evaluate_model(y_test, y_pred):
    cm = confusion_matrix(y_test, y_pred)
    accuracy = (cm[0, 0] + cm[1, 1]) / np.sum(cm)
    recall = cm[1, 1] / (cm[0, 1] + cm[1, 1])
    false_positive_rate = cm[1, 0] / (cm[0, 0] + cm[1, 0])
    precision = cm[1, 1] / (cm[1, 0] + cm[1, 1])
    f_measure = 2 * ((precision * recall) / (precision + recall))
    entropy = -precision * log(precision)
    return {
        "accuracy": accuracy,
        "recall": recall,
        "false_positive_rate": false_positive_rate,
        "precision": precision,
        "f_measure": f_measure,
        "entropy": entropy
    }
def main():
    filename = 'kddcup.data_10_percent_corrected'
    X, y = load_and_preprocess_data(filename)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    input_dim = X_train.shape[1]
    classifier = build_ann(input_dim)
    classifier.fit(X_train, y_train, batch_size=10, epochs=20)
    y_pred = classifier.predict(X_test)
    y_pred = (y_pred > 0.5)
    metrics = evaluate_model(y_test, y_pred)
    print(f"The Accuracy is: {metrics['accuracy']:.2f}")
    print(f"Recall is: {metrics['recall']:.2f}")
    print(f"False Positive Rate: {metrics['false_positive_rate']:.2f}")
    print(f"Precision is: {metrics['precision']:.2f}")
    print(f"F-measure is: {metrics['f_measure']:.2f}")
    print(f"Entropy is: {metrics['entropy']:.2f}")
if __name__ == "__main__":
    main()