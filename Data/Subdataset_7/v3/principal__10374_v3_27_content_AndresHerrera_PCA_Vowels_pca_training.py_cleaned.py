import os
import cv2
import numpy as np
def fonk1(vector, rows, cols):
    b1 = []
    a1 = 0
    while a1 + cols <= rows * cols:
        try:
            b1.append(vector[a1:a1 + cols])
        except:
            b1 = vector[a1:a1 + cols]
        a1 += cols
    b1 = np.array(b1)
    return b1
a2 = 20
a3 = 20
b2 = ['A', 'E', 'I', 'O', 'U']
def fonk2():
    for vowel in b2:
        b3 = None
        a4 = 0
        print('Processing vowel:', vowel)
        for file_name in os.listdir(os.path.join('training/', vowel)):
            a4 += 1
            print('Reading b4:', file_name)
            b4 = cv2.imread(os.path.join('training/', vowel, file_name), cv2.IMREAD_GRAYSCALE)
            b5 = cv2.resize(b4, (a2, a3))
            b6 = b5.reshape(a2 * a3)
            try:
                b3 = np.vstack((b3, b6))
            except:
                b3 = b6
        if b3 is not None:
            mean, b7 = cv2.PCACompute(b3, np.mean(b3, axis=0).reshape(1, -1))
        b8 = fonk1(mean.transpose(), a2, a3)
        cv2.imwrite('trained/pca_vowels_' + vowel + '.png', b8)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if b9 = = "__main__":
    fonk2()