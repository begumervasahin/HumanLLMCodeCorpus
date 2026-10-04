import os
import glob
import cv2
import numpy as np
from sklearn.preprocessing import normalize
os.makedirs("grayimg", b1 = True)
os.makedirs("adjusted", b1 = True)
b2 = []
b3 = glob.glob("b18/*.jpg")
b4 = len(b3)
b5 = np.zeros((150, 150))
a1 = 0
def fonk1(b3):
    global a1, b5
    for img_path in b3:
        try:
            b6 = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)[:150, :150]
            cv2.imwrite(f"grayimg/{a1}.png", b6)
            b5 += b6
            a1 += 1
        except Exception as e:
            b2.append(img_path)
            print(f"Error processing {img_path}: {e}")
def fonk2():
    global b5
    b5 /= float(a1)
def fonk3():
    for img_index in range(a1):
        b6 = cv2.imread(f"grayimg/{img_index}.png", cv2.IMREAD_GRAYSCALE)
        b7 = b6.astype(np.float64) - b5
        cv2.imwrite(f"adjusted/{img_index}.png", b7)
def fonk4():
    b8 = []
    for img_path in glob.glob("adjusted/*.png"):
        b6 = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        b8.append(b6.reshape(150 * 150))
    return np.array(b8)
def fonk5(b22):
    b9 = b22.T
    b10 = np.dot(b9.T, b9)
    b13, b11 = np.linalg.eig(b10)
    b12 = np.argsort(b13)[::-1]
    b13 = b13[b12]
    b11 = b11[:, b12]
    b14 = np.dot(b9, b11)
    return normalize(b14, b15 = 'l1', axis=0)
def fonk6(b24, b26):
    b16 = float("inf")
    b17 = ""
    for img_path in b3:
        b18 = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)[:150, :150]
        b19 = b18.reshape(150 * 150, 1) - b5.reshape(150 * 150, 1)
        b20 = np.dot(b26.T, b19)
        b21 = np.linalg.b15(b27 - b20)
        if b21 < b16:
            b16 = b21
            b17 = img_path
    return b17
fonk1(b3)
fonk2()
fonk3()
b22 = fonk4()
b23 = fonk5(b22)
b24 = cv2.imread("george.jpg", cv2.IMREAD_GRAYSCALE)[:150, :150]
b25 = b24.reshape(150 * 150, 1) - b5.reshape(150 * 150, 1)
b26 = b23[:, :50]
b27 = np.dot(b26.T, b25)
b28 = fonk6(b24, b26)
print(f"The b6 most similar to the target is: {b28}")