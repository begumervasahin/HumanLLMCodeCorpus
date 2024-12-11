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
a1 = 50
a2 = 3
b2 = []
b3 = []
b4 = []
b5 = []
b6 = []
b7 = []
a3 = 0
a4 = 0
b8 = os.path.join(b1, "Viola and Jones")
b9 = os.path.join(b1, "treniranje i testiranje")
b10 = os.path.join(b1, "jedinicna lica")
for _ in range(111):
    b11 = random.choice(os.listdir(os.path.join(b1, "part1")))
    b12 = cv2.imread(os.path.join(b1, "part1", b11))
    b13 = cv2.cvtColor(b12, cv2.COLOR_BGR2GRAY)
    b14 = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    b15 = b14.detectMultiScale(b13)
    for (column, row, width, height) in b15:
        b16 = cv2.resize(b13[row:row + height, column:column + width], (360, 480))
        b2.append(b16)
        b17 = b11.find("_")
        b3.append(b11[b17 + 1])
        b18 = int(b11[:b17])
        b4.append(0 if b18 < 45 else 1)
        cv2.imwrite(os.path.join(b8, b11), b16)
b3 = np.array(b3)
b4 = np.array(b4)
b19 = np.random.rand(len(b2)) < 0.8
b20 = np.array(b2)[b19, :]
b21 = np.array(b2)[~b19, :]
b22 = b3[b19]
b23 = b3[~b19]
b24 = b4[b19]
b25 = b4[~b19]
b26 = np.mean(b20, axis=0)
b27 = np.mean(b21, axis=0)
b20 -= b26
b21 -= b27
U, Sigma, b28 = np.linalg.svd(b20, full_matrices=False)
b29 = np.dot(b20, b28[:a1, :].T)
b30 = np.dot(b21, b28[:a1, :].T)
b31 = len(b30)
for r_idx in range(b31):
    if slicne_poredjenje <= a2:
        b32 = np.reshape(b21[r_idx], (360, 480), 'C')
        b33 = f"{slicne_poredjenje}test{face_file_name_lista_test[r_idx]}"
        cv2.imwrite(os.path.join(b9, b33), b32)
    b34 = np.sum((b29 - b30[r_idx])**2, axis=1)
    b35 = np.argmin(b34)
    if slicne_poredjenje <= a2:
        b36 = np.reshape(b20[b35], (360, 480), 'C')
        b33 = f"{slicne_poredjenje}train{face_file_name_lista_train[b35]}"
        cv2.imwrite(os.path.join(b9, b33), b36)
    b37 = b22[b35]
    b5.append(b37)
    b18 = b24[b35]
    b6.append(b18)
    if b23[r_idx] == b37:
        a3 += 1
    if b25[r_idx] == b18:
        a4 += 1
    slicne_poredjenje += 1
b38 = (a3 / b31) * 100
b39 = (a4 / b31) * 100
print("PCA Accuracy:", b38)
print("Confusion Matrix for Gender:")
print(confusion_matrix(b23, b5))
print("PCA Accuracy for Age:")
print(b39)
print("Confusion Matrix for Age:")
print(confusion_matrix(b25, b6))
b40 = MLPClassifier(hidden_layer_sizes=(15, 10), max_iter=1000, solver='adam', batch_size='auto', early_stopping=True)
b40.fit(b29, b22)
b41 = b40.predict(b30)
print("Confusion Matrix for Gender (MLP):")
print(confusion_matrix(b23, b41))
b42 = MLPClassifier(hidden_layer_sizes=(15, 10), max_iter=1000, solver='adam', batch_size='auto', early_stopping=True)
b42.fit(b29, b24)
b43 = b42.predict(b30)
print("Confusion Matrix for Age (MLP):")
print(confusion_matrix(b25, b43))
b44 = np.reshape(b26, (360, 480), 'C')
cv2.imwrite(os.path.join(b8, "average_photo.jpg"), b44)
for i in range(min(4, a1)):
    b45 = np.reshape(b28[i].T, (360, 480))
    ret, b46 = cv2.threshold(b45, 0, 175, cv2.THRESH_BINARY)
    cv2.imwrite(os.path.join(b10, f"face{i+1}.jpg"), b46)
plt.plot(range(len(Sigma)), Sigma, b47 = 'o', linewidth=2, markersize=12)
plt.xlabel('i')
plt.ylabel('sigma_i')
plt.title('Eigenvalues')
plt.show()