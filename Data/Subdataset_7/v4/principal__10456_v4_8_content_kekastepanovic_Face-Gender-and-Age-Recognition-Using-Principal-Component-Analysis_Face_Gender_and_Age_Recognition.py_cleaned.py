import numpy as np
import cv2
import os
import random
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
b1 = []
b2 = []
b3 = []
b4 = []
b5 = []
b6 = []
a1 = 0
a2 = 0
a3 = 0
b7 = r"C:\Users\Computer\Desktop\KV\Viola and Jones"
b8 = r"C:\Users\Computer\Desktop\KV\treniranje a6 testiranje"
b9 = r"C:\Users\Computer\Desktop\KV\jedinicna lica"
a4 = 50
a5 = 0
while a5 <= 110:
    b10 = random.choice([x for x in os.listdir(r"C:\Users\Computer\Desktop\KV\part1") if os.path.isfile(os.path.join(r"C:\Users\Computer\Desktop\KV\part1", x))])
    a5 += 1
    b11 = cv2.imread(os.path.join(r"C:\Users\Computer\Desktop\KV\part1", b10))
    b12 = cv2.cvtColor(b11, cv2.COLOR_BGR2GRAY)
    b13 = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    b14 = b13.detectMultiScale(b12)
    a6 = 0
    for (column, row, width, height) in b14:
        b15 = b12[row:row + height, column:column + width]
        b15 = cv2.resize(b15, (360, 480))
        b16 = b10
        b6.append(b16)
        b1.append(b15)
        b17 = b16.find("_")
        b2.append(b16[b17 + 1])
        b18 = int(b16[0:b17])
        if b18 < 45:
            b3.append(0)
        else:
            b3.append(1)
        cv2.imwrite(os.path.join(b7, b16), b15)
        a6 += 1
b2 = np.array(b2)
b3 = np.array(b3)
b6 = np.array(b6)
b19 = np.random.rand(len(b1)) < 0.8
b20 = np.array(b1)[b19, :]
b21 = np.array(b1)[~b19, :]
b22 = b6[b19]
b23 = b6[~b19]
b24 = b2[b19]
b25 = b2[~b19]
b26 = b3[b19]
b27 = b3[~b19]
b28 = np.sum(b20, b37=0) / len(b20)
b29 = np.sum(b21, b37=0) / len(b21)
b20 = b20 - b28
b21 = b21 - b29
U, Sigma, b30 = np.linalg.svd(b20, full_matrices=False)
b31 = np.matmul(b20, b30[:a4, :].T)
b32 = np.matmul(b21, b30[:a4, :].T)
b33 = len(b32)
for r_idx in range(len(b32)):
    if a3 <= 3:
        b34 = np.reshape(b21[r_idx, :], (360, 480), 'C')
        b35 = str(a3) + "test" + b23[r_idx]
        cv2.imwrite(os.path.join(b8, b35), b34)
    b36 = []
    for training in range(len(b31)):
        b36.append(np.sum((b31[training, :] - b32[r_idx, :]) ** 2, b37 = 0))
    b38 = b36.index(min(b36))
    if a3 <= 3:
        b39 = np.reshape(b20[b38, :], (360, 480), 'C')
        b35 = str(a3) + "train" + b22[b38]
        cv2.imwrite(os.path.join(b8, b35), b39)
    b40 = b24[b38]
    b4.append(b40)
    b18 = b26[b38]
    b5.append(b18)
    if b25[r_idx] == b40:
        a1 += 1
    if b27[r_idx] == b18:
        a2 += 1
    del b36[:]
    a3 += 1
b41 = (a1 / b33) * 100
b42 = (a2 / b33) * 100
print("PCA Accuracy:", b41)
print("Confusion Matrix for Gender:")
print(confusion_matrix(b25, b4))
print("PCA Accuracy for Age:")
print(b42)
print("Confusion Matrix for Age:")
print(confusion_matrix(b27, b5))
b43 = MLPClassifier(hidden_layer_sizes=(15, 10), max_iter=1000, solver='adam', batch_size='auto', early_stopping=True)
b43.fit(b31, b24)
b44 = b43.predict(b32)
print("Confusion Matrix for Gender (MLP):")
print(confusion_matrix(b25, b44))
b45 = MLPClassifier(hidden_layer_sizes=(15, 10), max_iter=1000, solver='adam', batch_size='auto', early_stopping=True)
b45.fit(b31, b26)
b46 = b45.predict(b32)
print("Confusion Matrix for Age (MLP):")
print(confusion_matrix(b27, b46))
b47 = np.sum(b20, b37=0) / len(b20)
b48 = np.reshape(b47, (360, 480), 'C')
cv2.imwrite(os.path.join(b7, "average_photo.jpg"), b48)
for a6 in range(4):
    b49 = np.reshape(b30[a6, :].T, (360, 480))
    ret, b50 = cv2.threshold(b49, 0, 175, cv2.THRESH_BINARY)
    cv2.imwrite(os.path.join(b9, f"face{a6+1}.jpg"), b50)
b51 = Sigma.tolist()
b52 = list(range(len(Sigma)))
plt.plot(b52, b51, b53 = 'o', linewidth=2, markersize=12)
plt.xlabel('a6')
plt.ylabel('sigma_i')
plt.title('Eigenvalues')
plt.show()