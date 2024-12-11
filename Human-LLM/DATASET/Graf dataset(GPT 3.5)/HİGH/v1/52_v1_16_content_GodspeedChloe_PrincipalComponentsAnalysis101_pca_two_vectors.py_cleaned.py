import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans2
def fonk1(file_name, b24, b1):
    with open(file_name) as data:
        b1 = data.readline().strip().split(',')
        for i in range(len(b1)):
            b1[i] = b1[i].strip()
        b2 = data.readlines()
        for line in b2:
            b3 = line.strip().split(',')
            for v in range(len(b3)):
                b3[v] = int(b3[v].strip())
            b24.append(b3)
    return b24, b1
def fonk2(b24):
    b4 = np.asarray([rec[1:] for rec in b24]).T
    return np.cov(b4)
def fonk3(b26):
    eigenvalues, b5 = np.linalg.eig(b26)
    return eigenvalues, b5
def fonk4(eigenvalues):
    b6 = np.sum(eigenvalues)
    return eigenvalues / b6
def fonk5(eigenvalues):
    b7 = np.append(np.asarray([0]), eigenvalues)
    b8 = np.asarray([])
    b9 = range(0, 13)
    a1 = 0
    for v in np.nditer(b7):
        a1 += v
        b8 = np.append(b8, np.asarray([a1]))
    plt.figure(1)
    plt.plot(b9, b8, 'bo', b9, b8, 'b30')
    plt.xlabel('Eigenvalue ID (decreasing magnitude)')
    plt.ylabel('Variance captured')
    plt.title('Eigenvalues And Their Captured Variance')
    plt.show()
def fonk6(eigenvalues, b5):
    b10 = eigenvalues.tolist()
    b11 = b5.tolist()
    a2 = 0
    a3 = 0
    a4 = 0
    a5 = 0
    for i in range(len(b10)):
        if abs(b10[i]) > a3:
            a5 = a3
            a3 = abs(b10[i])
            a4 = a2
            a2 = i
        elif abs(b10[i]) > a5:
            a5 = abs(b10[i])
            a4 = i
    return b11[a2], b11[a4]
def fonk7(data):
    b12 = []
    b13 = []
    b6 = len(data)
    for b18 in range(1, len(data[0])):
        a6 = 0
        for d in data:
            a6 += d[b18]
        a6 = a6 / b6
        b13.append(a6)
    for d in data:
        b12.append(d[1:])
    for a6 in range(len(b13)):
        for md in range(b6):
            b12[md][a6] = b12[md][a6] - b13[a6]
    return b13, b12
def fonk8(data, vec1, vec2):
    b14 = []
    b9 = []
    b8 = []
    b15 = vec1.T
    b16 = vec2.T
    for d in data:
        b9.append(np.dot(d, b15))
        b8.append(np.dot(d, b16))
        b14.append([np.dot(d, b15), np.dot(d, b16)])
    plt.figure(1)
    plt.plot(b9, b8, 'bo')
    plt.xlabel('AMOUNT OF PRINCIPAL COMPONENT')
    plt.ylabel('AMOUNT OF PRINCIPAL COMPONENT')
    plt.title('HW AG DATA PROJECTED ONTO 2D PCA SPACE USING THE KLT TRANSFORMATION')
    plt.show()
    return b14
def fonk9(vectors):
    for v in range(len(vectors)):
        b17 = vectors[v]
        for a in range(len(b17)):
            b18 = b17[a]
            b18 = (round(100 * b18)) / 100
            b17[a] = b18
        vectors[v] = b17
    return vectors
def fonk10(centroids, vec1, vec2, b13):
    b19 = centroids.tolist()
    b20 = []
    for i in range(len(b19)):
        b21 = np.asarray([b19[i]])
        b15 = np.asarray([vec1.tolist()])
        b16 = np.asarray([vec2.tolist()])
        b22 = np.dot(b21.T, b15)
        b23 = np.dot(b21.T, b16)
        b21 = np.add(b22, b23)
        b21 = np.add(b21, b13)
        b21 = b21.tolist()
        b20.append(b21[0])
    b20 = fonk9(b20)
    for b21 in b20:
        print('Centroid:')
        print(b21)
def fonk11():
    print('USAGE: python3 pca_two_vectors.py <filename>.csv')
    quit()
def fonk12():
    b24 = []
    b25 = []
    if len(sys.argv) != 2:
        fonk11()
    try:
        open(sys.argv[1], 'b4')
    except IOError:
        print('invalid filename')
        fonk11()
    print('\nPart one: reading in csv ...')
    b24, b25 = fonk1(sys.argv[1], b24, b25)
    print('\nPart two: Covariance Matrix  b26 = \n')
    b26 = fonk2(b24)
    print(b26)
    print('\nPart three: Proper vectors for b26\n')
    eigenvalues, b5 = fonk3(b26)
    b5 = b5.T
    print('Values: \n', eigenvalues)
    print('Vectors:\n', b5)
    print('\nPart four: sorting eigenvalues:\n')
    b27 = -np.sort(-eigenvalues)
    print(b27)
    print('\nPart five: normalize eigenvalues:\n')
    b27 = fonk4(b27)
    print(b27)
    fonk5(b27)
    print('\nPart six: show b5 associated with the 2 largest eigenvalues\n')
    b15, b16 = fonk6(eigenvalues, b5)
    b28 = fonk9([b15, b16])
    b15 = b28[0]
    b16 = b28[1]
    print('Best:\n', b15)
    print('Second:\n', b16)
    b15 = -np.asarray(b15)
    b16 = -np.asarray(b16)
    print('\nPart seven: project data with the 2 largest eigenvalues\n')
    b13, b29 = fonk7(b24)
    b14 = fonk8(b29, b15, b16)
    print('\nPart eight: perform b30-Means clustering with Euclidean distance and b30 = 3 ...\n')
    centroids, b31 = kmeans2(b14, 3, iter=20, minit='random')
    print('\nPart nine: print centroids found from clustering in PCA space\n')
    print('Centroids:\n')
    print(centroids)
    print('\nPart ten: multiply centroids by the \'best\' b5\n')
    fonk10(centroids, b15, b16, b13)
if b32 = = "__main__":
    fonk12()