import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans2
def fonk1(file_name):
    b1 = []
    with open(file_name) as data:
        b2 = data.readline().strip().split(',')
        for line in data.readlines():
            b3 = [int(val.strip()) for val in line.split(',')]
            b1.append(b3)
    return b1, b2
def fonk2(b1):
    b4 = np.array([rec[1:] for rec in b1]).T
    return np.cov(b4)
def fonk3(b14):
    eigenvalues, b5 = np.linalg.eig(b14)
    return eigenvalues, b5
def fonk4(eigenvalues):
    return eigenvalues / np.sum(eigenvalues)
def fonk5(eigenvalues):
    b6 = np.cumsum(np.insert(eigenvalues, 0, 0))
    plt.plot(range(len(eigenvalues) + 1), b6, 'bo', range(len(eigenvalues) + 1), b6, 'b22')
    plt.xlabel('Eigenvalue ID (decreasing magnitude)')
    plt.ylabel('Variance captured')
    plt.title('Eigenvalues And Their Captured Variance')
    plt.show()
def fonk6(eigenvalues, b5):
    b7 = np.argsort(eigenvalues)[::-1][:2]
    return b5[:, b7[0]], b5[:, b7[1]]
def fonk7(data):
    b8 = np.mean(data, axis=0)[1:]
    return b8, data[:, 1:] - b8
def fonk8(data, vec1, vec2):
    b9 = np.dot(data, vec1)
    b10 = np.dot(data, vec2)
    plt.plot(b9, b10, 'bo')
    plt.xlabel('AMOUNT OF PRINCIPAL COMPONENT')
    plt.ylabel('AMOUNT OF PRINCIPAL COMPONENT')
    plt.title('HW AG DATA PROJECTED ONTO 2D PCA SPACE USING THE KLT TRANSFORMATION')
    plt.show()
    return np.column_stack((b9, b10))
def fonk9(vectors):
    return np.round(vectors, 2)
def fonk10(centroids, vec1, vec2, b8):
    b11 = centroids.dot(np.array([vec1, vec2]).T) + b8
    b12 = fonk9(b11)
    for centroid in b12:
        print('Centroid:')
        print(centroid)
def fonk11():
    print('USAGE: python3 pca_two_vectors.py <filename>.csv')
    quit()
def fonk12():
    if len(sys.argv) != 2:
        fonk11()
    try:
        open(sys.argv[1], 'r')
    except IOError:
        print('Invalid filename')
        fonk11()
    print('\nReading data from CSV...')
    b1, b13 = fonk1(sys.argv[1])
    print('\nCalculating covariance matrix...')
    b14 = fonk2(b1)
    print(b14)
    print('\nComputing b5 and eigenvalues...')
    eigenvalues, b5 = fonk3(b14)
    b5 = b5.T
    print('Eigenvalues: \n', eigenvalues)
    print('Eigenvectors:\n', b5)
    print('\nSorting eigenvalues...')
    b15 = -np.sort(-eigenvalues)
    print(b15)
    print('\nNormalizing eigenvalues...')
    b16 = fonk4(b15)
    print(b16)
    fonk5(b16)
    print('\nChoosing the two best b5...')
    b19, b17 = fonk6(b15, b5)
    b18 = fonk9(np.array([b19, b17]))
    b19 = b18[0]
    b17 = b18[1]
    print('Best:\n', b19)
    print('Second:\n', b17)
    b19 = -b19
    b17 = -b17
    print('\nProjecting data with the two best b5...')
    b8, b20 = fonk7(np.array(b1))
    b21 = fonk8(b20, b19, b17)
    print('\nPerforming b22-Means clustering with Euclidean distance and b22 = 3...')
    centroids, b23 = kmeans2(b21, 3, iter=20, minit='random')
    print('\nCentroids found from clustering in PCA space:\n')
    print(centroids)
    print('\nReprojecting centroids by the best b5...')
    fonk10(centroids, b19, b17, b8)
if b24 = = "__main__":
    fonk12()