import numpy as np
import cv2
from sklearn.decomposition import PCA
def fonk1(img):
    height, width, b1 = img.shape
    a1 = 900
    b2 = a1 / width
    b3 = int(width * b2)
    b4 = int(height * b2)
    return b3, b4
def fonk2(image_path):
    b5 = cv2.imread(image_path)
    b6 = b5.copy()
    height, width, b7 = b5.shape
    b8 = np.reshape(b5, (height, width * b7))
    b9 = PCA(n_components=350).fit(b8)
    b10 = b9.transform(b8)
    b11 = np.sum(b9.explained_variance_ratio_)
    b12 = b9.inverse_transform(b10)
    b12 = np.reshape(b12, (height, width, b7))
    b13 = np.uint8(b12)
    return b6, b13
def fonk3():
    for num in range(1, 3):
        print("Processing b5", num)
        b6, b13 = fonk2(str(num) + '.jpg')
        cv2.imwrite('quantizedImages/op-' + str(num) + '.jpg', b13)
        b14 = cv2.resize(b6, fonk1(b6))
        b15 = cv2.resize(b13, fonk1(b6))
        cv2.imshow("Original", b14)
        cv2.imshow("Compressed", b15)
        cv2.waitKey()
if b16 = = "__main__":
    fonk3()