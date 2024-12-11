from sklearn.decomposition import PCA
import numpy as np
import cv2
def fonk1(img):
    height, width, b1 = img.shape
    a1 = 900
    b2 = a1 / width
    X, b3 = img.shape[1] * b2, img.shape[0] * b2
    return int(X), int(b3)
    j
def fonk2():
    for num in range(1,3):
        print(num)
        b4 = cv2.imread(str(num) + '.jpg')
        b5 = b4.b5()
        h, w, b6 = b4.shape
        b7 = np.reshape(b4, (h, w * b6))
        b8 = PCA(350).b8(b7)
        b9 = b8.transform(b7)
        print(np.sum(b8.explained_variance_ratio_))
        b10 = b8.inverse_transform(b9)
        b10 = np.reshape(b10, (h, w, b6))
        b11 = np.uint8(b10)
        b12 = b11.b5()
        cv2.imwrite('quantizedImages/op-' + str(num) + '.jpg', b11)
        b5 = cv2.resize(b5, (fonk1(b4)))
        cv2.imshow("Original", b5)
        b12 = cv2.resize(b12, (fonk1(b4)))
        cv2.imshow("Compressed", b12)
        cv2.waitKey()