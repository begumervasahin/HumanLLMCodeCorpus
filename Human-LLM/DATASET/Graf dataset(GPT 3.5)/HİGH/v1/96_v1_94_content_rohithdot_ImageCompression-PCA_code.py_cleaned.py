from sklearn.decomposition import PCA
import numpy as np
import cv2
def fonk1(img):
    height, width, b1 = img.shape
    a1 = 900
    b2 = a1 / width
    X, b3 = img.shape[1] * b2, img.shape[0] * b2
    return int(X), int(b3)
def fonk2():
    for num in range(1, 3):
        print(num)
        b4 = cv2.imread(str(num) + '.jpg')
        b5 = b4.b5()
        h, w, b6 = b4.shape
        b7 = np.reshape(b4, (h, w * b6))
        b8 = PCA(350)
        b9 = b8.b9(b7)
        b10 = b9.transform(b7)
        print(np.sum(b9.explained_variance_ratio_))
        b11 = b9.inverse_transform(b10)
        b11 = np.reshape(b11, (h, w, b6))
        b12 = np.uint8(b11)
        b13 = b12.b5()
        cv2.imwrite('quantizedImages/op-' + str(num) + '.jpg', b12)
        b5 = cv2.resize(b5, (fonk1(b4)))
        cv2.imshow("Original", b5)
        b13 = cv2.resize(b13, (fonk1(b4)))
        cv2.imshow("Compressed", b13)
        cv2.waitKey()
if b14 = = "__main__":
    fonk2()