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
        print(f'Reading from: {vowel} Directory')
        b3 = None
        a4 = 0
        for file_name in os.listdir(os.path.join('training/', vowel)):
            a4 += 1
            print(file_name)
            b1 = cv2.imread(os.path.join('training/', vowel, file_name), cv2.IMREAD_GRAYSCALE)
            b4 = cv2.resize(b1, (a2, a3))
            b5 = b4.reshape(a2 * a3)
            try:
                b3 = np.vstack((b3, b5))
            except:
                b3 = b5
        if b3 is not None:
            mean, b6 = cv2.PCACompute(b3, np.mean(b3, axis=0).reshape(1, -1))
            b7 = fonk1(mean.transpose(), a2, a3)
            cv2.imwrite(f'trained/pca_vowels_{vowel}.png', b7)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if b8 = = "__main__":
    fonk2()