import sys
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import skimage.filters as filt
from numpy import linalg as LA
from sklearn.preprocessing import StandardScaler
def fonk1(b42, initial_Ps, initial_p, initial_q):
    a1 = 20
    b1 = b42.shape[0]
    b2 = (initial_Ps * (1 - initial_p)) / ((initial_Ps * (1 - initial_p)) + (1 - initial_Ps) * (1 - initial_q))
    b3 = (initial_Ps * initial_p) / ((initial_Ps * initial_p) + (1 - initial_Ps) * initial_q)
    b4 = np.mean([b2 if y == 0 else b3 for y in b42])
    print("\nInitial values:")
    print("Pie(0) =", initial_Ps)
    print("b10(0) =", initial_p)
    print("b13(0) =", initial_q)
    print("\nFor observable b5 = 0:")
    print("mu(1) =", b2)
    print("For observable b5 = 1:")
    print("mu(1) =", b3)
    print("Mean mu(1) =", b4)
    for iteration in range(1, a1 + 1):
        b6 = sum(b2 if y == 0 else b3 for y in b42)
        b7 = b6 / 10
        print(f"\nIteration number: {iteration}")
        print(f"Pie({iteration}) = {b7}")
        b8 = sum(b3 for y in b42 if y == 1)
        b9 = sum(b3 for y in b42)
        b10 = b8 / b9
        print(f"b10({iteration}) = {b10}")
        b11 = sum(1 - b3 for y in b42 if y == 1)
        b12 = sum(1 - b3 for y in b42)
        b13 = b11 / b12
        print(f"b13({iteration}) = {b13}")
        b2 = (b7 * (1 - b10)) / ((b7 * (1 - b10)) + (1 - b7) * (1 - b13))
        b3 = (b7 * b10) / ((b7 * b10) + (1 - b7) * b13)
        b4 = np.mean([b2 if y == 0 else b3 for y in b42])
        print("\nFor observable b5 = 0:")
        print(f"mu({iteration + 1}) = {b2}")
        print("For observable b5 = 1:")
        print(f"mu({iteration + 1}) = {b3}")
        print(f"Mean mu({iteration + 1}) = {b4}")
def fonk2(input_filename, b14 = False):
    b15 = np.array(Image.open(input_filename))
    b16 = 1.0 - rgb2gray(b15)
    if b14:
        plt.figure(1)
        plt.imshow(b16)
        plt.title('Original Grayscale Image')
        plt.show()
    b17 = filt.threshold_minimum(b16)
    b18 = b16 > b17
    if b14:
        plt.figure(2)
        plt.imshow(b18)
        plt.title('Binarized Image')
        plt.show()
    non_zero_rows, b19 = b18.nonzero()
    n_rows, b20 = b18.shape
    left, b21 = max(0, min(b19) - 1), min(b20 - 1, max(b19) + 1) + 1
    top, b22 = max(0, min(non_zero_rows) - 1), min(n_rows - 1, max(non_zero_rows) + 1) + 1
    b23 = b18[top:b22, left:b21]
    if b14:
        plt.figure(3)
        plt.imshow(b23)
        plt.title('Windowed Image')
        plt.show()
    b24 = max(b23.shape)
    b25 = int(round(b23.shape[0] / b24 * 48))
    b26 = int(round(b23.shape[1] / b24 * 48))
    b27 = Image.fromarray(b23.astype(np.uint8) * 255)
    b28 = b27.resize((b26, b25))
    b29 = np.array(b28).astype(bool)
    b30 = np.zeros((b29.shape[0] + 2, b29.shape[1] + 2), dtype=bool)
    b30[1:-1, 1:-1] = b29
    if b14:
        plt.figure(4)
        plt.imshow(b30, b31 = 'Greys')
        plt.title('Resized Windowed Image')
        plt.show()
    return b30
if b32 = = '__main__':
    b33 = np.array([(2, 3, 3, 4, 5, 7), (2, 4, 5, 5, 6, 8)])
    b34 = StandardScaler()
    b35 = b34.fit_transform(b33.T).T
    b36 = np.cov(b35)
    eigenvalues, b37 = LA.eig(b36)
    b38 = [(np.abs(eigenvalues[i]), b37[:, i]) for i in range(len(eigenvalues))]
    b38.sort(b39 = True)
    b40 = b38[0][1][:, np.newaxis]
    b41 = b35.T.dot(b40).T
    print("*****PCA*******\n")
    print("Eigenvalues of b33.T@b33:")
    print(eigenvalues)
    print("\nEigenvalues of b33@b33.T:")
    print(LA.eig(b33 @ b33.T)[0])
    print("\nEigenvectors of b33@b33.T:")
    print(LA.eig(b33 @ b33.T)[1])
    print("\nShape of transformed b5:")
    print(b41.shape)
    print("\nTransformed b5 after dimension reduction:")
    print(b41)
    print("\n*****EM*******")
    b42 = np.array([1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1])
    fonk1(b42, 0.4, 0.6, 0.7)
    print("\n\n")
    fonk1(b42, 0.5, 0.5, 0.5)