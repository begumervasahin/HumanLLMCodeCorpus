import numpy as np
import cv2
import os
import random
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
b1 = r"C:\Users\Computer\Desktop\KV"
b2 = os.path.join(b1, "Viola and Jones")
b3 = os.path.join(b1, "treniranje i testiranje")
b4 = os.path.join(b1, "jedinicna lica")
b5 = os.path.join(b1, "part1")
b6 = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
def fonk1(image_path, cascade_path):
    b7 = cv2.imread(image_path)
    b8 = cv2.cvtColor(b7, cv2.COLOR_BGR2GRAY)
    b9 = cv2.CascadeClassifier(cascade_path)
    b10 = b9.detectMultiScale(b8)
    return b8, b10
def fonk2(image, b10):
    b11 = []
    for (x, y, w, h) in b10:
        b12 = cv2.resize(image[y:y+h, x:x+w], (360, 480))
        b11.append(b12)
    return b11
def fonk3(filename):
    age, b13 = filename.split("_")[:2]
    return int(age), b13
def fonk4(singular_values):
    plt.plot(np.arange(1, len(singular_values) + 1), singular_values, b14 = 'o', linewidth=2, markersize=12)
    plt.xlabel('Component')
    plt.ylabel('Eigenvalue')
    plt.title('Eigenvalues of PCA')
    plt.show()
b15 = []
b16 = []
for _ in range(111):
    b17 = random.choice(os.listdir(b5))
    b18 = os.path.join(b5, b17)
    b8, b10 = fonk1(b18, b6)
    b11 = fonk2(b8, b10)
    for face_image in b11:
        age, b13 = fonk3(b17)
        b15.append(face_image)
        b16.append(b13)
b15 = np.array(b15)
b16 = np.array(b16)
X_train, X_test, y_train, b19 = train_test_split(b15, b16, test_size=0.2, random_state=42)
b20 = X_train.reshape(X_train.shape[0], -1)
b21 = X_test.reshape(X_test.shape[0], -1)
b22 = PCA(n_components=50)
b23 = b22.fit_transform(b20)
b24 = b22.transform(b21)
b25 = MLPClassifier(hidden_layer_sizes=(15, 10), max_iter=1000, solver='adam', batch_size='auto', early_stopping=True)
b25.fit(b23, y_train)
b26 = b25.predict(b24)
b27 = np.mean(b26 == b19) * 100
b28 = confusion_matrix(b19, b26)
print("Gender Prediction Accuracy: {:.2f}%".format(b27))
print("Confusion Matrix for Gender Prediction:")
print(b28)
fonk4(b22.singular_values_)