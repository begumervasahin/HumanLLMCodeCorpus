import cv2
import numpy as np
from sklearn.decomposition import PCA
def fonk1(img):
    height, width, b1 = img.shape
    a1 = 900
    b2 = a1 / width
    new_width, b3 = int(width * b2), int(height * b2)
    return new_width, b3
def fonk2(b11):
    height, width, b4 = b11.shape
    b5 = np.reshape(b11, (height, width * b4))
    b6 = PCA(n_components=350)
    b7 = b6.fit(b5)
    b8 = b7.transform(b5)
    b9 = b7.inverse_transform(b8)
    b10 = np.uint8(np.reshape(b9, (height, width, b4)))
    return b10
def fonk3():
    for num in range(1, 3):
        print(f"Processing b11 {num}")
        b11 = cv2.imread(f"{num}.jpg")
        b12 = b11.copy()
        b10 = fonk2(b11)
        cv2.imwrite(f'quantizedImages/op-{num}.jpg', b10)
        b13 = cv2.resize(b12, fonk1(b11))
        cv2.imshow("Original", b13)
        b14 = cv2.resize(b10, fonk1(b11))
        cv2.imshow("Compressed", b14)
        cv2.waitKey()
if b15 = = "__main__":
    fonk3()