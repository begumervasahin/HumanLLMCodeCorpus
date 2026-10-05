import cv2
import numpy as np
from sklearn.decomposition import PCA
def fonk1(img):
    height, width, b1 = img.shape
    a1 = 900
    b2 = a1 / width
    new_width, b3 = int(width * b2), int(height * b2)
    return new_width, b3
def fonk2():
    for num in range(1, 3):
        print(f"Processing b4 {num}")
        b4 = cv2.imread(str(num) + '.jpg')
        b5 = b4.copy()
        height, width, b6 = b4.shape
        b7 = np.reshape(b4, (height, width * b6))
        b8 = PCA(n_components=350)
        b9 = b8.fit(b7)
        b10 = b9.transform(b7)
        b11 = b9.inverse_transform(b10)
        b11 = np.reshape(b11, (height, width, b6))
        b12 = np.uint8(b11)
        cv2.imwrite(f'quantizedImages/op-{num}.jpg', b12)
        b13 = cv2.resize(b5, fonk1(b4))
        cv2.imshow("Original", b13)
        b14 = cv2.resize(b12, fonk1(b4))
        cv2.imshow("Compressed", b14)
        cv2.waitKey()
if b15 = = "__main__":
    fonk2()