import os
import glob
import cv2
import numpy as np
from sklearn.preprocessing import normalize
os.makedirs("grayimg", b1 = True)
os.makedirs("adjusted", b1 = True)
b2 = []
b3 = glob.glob("b23/*.jpg")
b4 = len(b3)
b5 = np.zeros((150, 150))
a1 = 0
for img_path in b3:
    try:
        b6 = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)[:150, :150]
        cv2.imwrite(f"grayimg/{a1}.png", b6)
        b5 += b6
        a1 += 1
    except Exception as e:
        b2.append(img_path)
        print(f"Error processing {img_path}: {e}")
b5 /= float(a1)
for img_index in range(a1):
    b6 = cv2.imread(f"grayimg/{img_index}.png", cv2.IMREAD_GRAYSCALE)
    b7 = b6.astype(np.float64) - b5
    cv2.imwrite(f"adjusted/{img_index}.png", b7)
b8 = []
for img_path in glob.glob("adjusted/*.png"):
    b6 = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    b8.append(b6.reshape(150 * 150))
b9 = np.array(b8)
b10 = b9.T
b11 = np.dot(b10.T, b10)
b14, b12 = np.linalg.eig(b11)
b13 = np.argsort(b14)[::-1]
b14 = b14[b13]
b12 = b12[:, b13]
b15 = np.dot(b10, b12)
b16 = normalize(b15, norm='l1', axis=0)
b17 = cv2.imread("george.jpg", cv2.IMREAD_GRAYSCALE)[:150, :150]
b18 = b17.reshape(150 * 150, 1) - b5.reshape(150 * 150, 1)
b19 = b16[:, :50]
b20 = np.dot(b19.T, b18)
b21 = float("inf")
b22 = ""
for img_path in b3:
    b23 = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)[:150, :150]
    b24 = b23.reshape(150 * 150, 1) - b5.reshape(150 * 150, 1)
    b25 = np.dot(b19.T, b24)
    b26 = np.linalg.norm(b20 - b25)
    if b26 < b21:
        b21 = b26
        b22 = img_path
print(f"The b6 most similar to the target is: {b22}")