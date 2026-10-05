import numpy as np
import cv2
import os
import random
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
b1 = r"C:\Users\Computer\Desktop\KV\Viola and Jones"
b2 = r"C:\Users\Computer\Desktop\KV\treniranje i testiranje"
b3 = r"C:\Users\Computer\Desktop\KV\jedinicna lica"
b4 = r"C:\Users\Computer\Desktop\KV\part1"
b5 = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
def fonk1(image_path, b8):
    b6 = cv2.imread(image_path)
    b7 = cv2.cvtColor(b6, cv2.COLOR_BGR2GRAY)
    b8 = cv2.CascadeClassifier(b8)
    b9 = b8.detectMultiScale(b7)
    return b7, b9
def fonk2(image, b9):
    b10 = []
    for (x, y, w, h) in b9:
        b11 = cv2.resize(image[y:y+h, x:x+w], (360, 480))
        b10.append(b11)
    return b10
def fonk3(filename):
    age, b12 = filename.split("_")[:2]
    return int(age), b12
def fonk4(Sigma):
    plt.plot(np.arange(1, len(Sigma) + 1), Sigma, b13 = 'o', linewidth=2, markersize=12)
    plt.xlabel('i')
    plt.ylabel('sigma_i')
    plt.title('Eigenvalues')
    plt.show()
b14 = []
b15 = []
b16 = []
for _ in range(111):
    b17 = random.choice(os.listdir(b4))
    b18 = os.path.join(b4, b17)
    b7, b9 = fonk1(b18, b5)
    b10 = fonk2(b7, b9)
    for face_image in b10:
        age, b12 = fonk3(b17)
        b14.append(face_image)
        b15.append(b12)
        b16.append(0 if age < 45 else 1)
b14 = np.array(b14)
b15 = np.array(b15)
b16 = np.array(b16)
X_train, X_test, y_train, b19 = train_test_split(b14, b15, test_size=0.2, random_state=42)
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