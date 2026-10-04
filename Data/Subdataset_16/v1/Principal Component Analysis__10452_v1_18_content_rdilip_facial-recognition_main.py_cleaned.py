import numpy as np
import cv2
import glob, os
from sklearn.preprocessing import normalize
os.makedirs("grayimg", b1 = True)
os.makedirs("adjusted", b1 = True)
b2 = []
b3 = glob.glob("b23/*.jpg")
b4 = iter(range(len(b3) * 2))
b5 = np.zeros((150, 150))
a1 = 0
for img_path in b3:
    try:
        b6 = cv2.imread(img_path, 0)[:150, :150]
        if b6 is None:
            raise ValueError(f"Image {img_path} not loaded properly.")
        b7 = next(b4)
        cv2.imwrite(f"grayimg/{b7}.png", b6)
        b5 += b6
        a1 += 1
    except Exception as e:
        b2.append((img_path, str(e)))
b5 = b5 / float(a1)
for img_index in range(a1):
    b6 = cv2.imread(f"grayimg/{img_index}.png", 0)
    if b6 is None:
        b2.append((f"grayimg/{img_index}.png", "Image not loaded properly."))
        continue
    b8 = b6.astype(np.float64) - b5
    cv2.imwrite(f'adjusted/{img_index}.png', b8)
b9 = []
for img_path in glob.glob("adjusted/*.png"):
    b6 = cv2.imread(img_path, 0)
    if b6 is not None:
        b9.append(b6.reshape((150 * 150,)))
b10 = np.array(b9)
b11 = np.transpose(b10)
b12 = np.dot(np.transpose(b11), b11)
b15, b13 = np.linalg.eig(b12)
b14 = b15.argsort()[::-1]
b15 = b15[b14]
b13 = b13[:, b14]
b16 = np.dot(b11, b13)
b17 = normalize(b16, norm='l1', axis=0)
b18 = cv2.imread("george.jpg", 0)[:150, :150]
if b18 is None:
    raise ValueError("Target b6 'george.jpg' not loaded properly.")
b19 = b17[:, :50]
b20 = np.dot(np.transpose(b19), b18.reshape((150 * 150, 1)) - b5.reshape((150 * 150, 1)))
b21 = float("inf")
b22 = ""
for img_path in b3:
    b23 = cv2.imread(img_path, 0)[:150, :150]
    if b23 is None:
        b2.append((img_path, "Image not loaded properly."))
        continue
    b24 = np.dot(np.transpose(b19), b23.reshape((150 * 150, 1)) - b5.reshape((150 * 150, 1)))
    b25 = np.linalg.norm(b20 - b24)
    if b25 < b21:
        b21 = b25
        b22 = img_path
print(f"The closest b6 is: {b22}")
print(f"Problems encountered: {b2}")