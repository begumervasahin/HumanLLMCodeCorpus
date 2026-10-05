import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans2
def fonk1(b14):
    b1 = []
    with open(b14) as data:
        b2 = data.readline().strip().split(',')
        for line in data.readlines():
            b3 = [int(val.strip()) for val in line.strip().split(',')]
            b1.append(b3)
    return b1, b2
def fonk2(b1):
    b4 = np.asarray([rec[1:] for rec in b1]).T
    return np.cov(b4)
def fonk3(b16):
    eigenvalues, b5 = np.linalg.eig(b16)
    return eigenvalues, b5
def fonk4(eigenvalues):
    b6 = np.sum(eigenvalues)
    return eigenvalues / b6
def fonk5(eigenvalues):
    b7 = np.cumsum(eigenvalues)
    plt.plot(range(len(eigenvalues) + 1), np.hstack([0, b7]), 'bo-', b8 = 'Eigenvalues')
    plt.xlabel('Eigenvalue ID (decreasing magnitude)')
    plt.ylabel('Variance captured')
    plt.title('Eigenvalues And Their Captured Variance')
    plt.legend()
    plt.show()
def fonk6(eigenvalues, b5):
    b9 = np.argsort(eigenvalues)[::-1]
    return b5[:, b9[0]], b5[:, b9[1]]
def fonk7(data):
    b10 = np.mean(data, axis=0)
    b11 = data - b10
    return b10, b11
def fonk8(data, vec1, b18):
    b12 = np.dot(data, np.vstack((vec1, b18)).T)
    plt.plot(b12[:, 0], b12[:, 1], 'bo')
    plt.xlabel('AMOUNT OF PRINCIPAL COMPONENT 1')
    plt.ylabel('AMOUNT OF PRINCIPAL COMPONENT 2')
    plt.title('Data Projected Onto 2D PCA Space')
    plt.show()
    return b12
def fonk9(vectors):
    return np.round(vectors, 2)
def fonk10(centroids, vec1, b18, b10):
    b13 = centroids.dot(np.vstack((vec1, b18))) + b10
    for centroid in b13:
        print('Centroid:')
        print(centroid)
def fonk11():
    print('USAGE: python3 pca_two_vectors.py <filename>.csv')
    sys.exit()
def fonk12():
    if len(sys.argv) != 2:
        fonk11()
    b14 = sys.argv[1]
    b1, b15 = fonk1(b14)
    print('Part one: Reading in CSV...')
    print('Part two: Computing covariance matrix b16...')
    b16 = fonk2(b1)
    print(b16)
    print('Part three: Computing eigenvalues and b5...')
    eigenvalues, b5 = fonk3(b16)
    print('Eigenvalues:\n', eigenvalues)
    print('Eigenvectors:\n', b5)
    print('Part four: Sorting and normalizing eigenvalues...')
    b17 = fonk4(eigenvalues)
    print(b17)
    print('Part five: Plotting eigenvalues...')
    fonk5(b17)
    print('Part six: Selecting the two best b5...')
    vec1, b18 = fonk6(eigenvalues, b5)
    print('Best eigenvector:\n', vec1)
    print('Second best eigenvector:\n', b18)
    print('Part seven: Subtracting b10 from the data...')
    b10, b11 = fonk7(b1)
    print('Part eight: Projecting data onto two b5...')
    b12 = fonk8(b11, vec1, b18)
    print('Part nine: Performing k-Means clustering...')
    centroids, b15 = kmeans2(b12, 3, iter=20, minit='random')
    print('Part ten: Reprojecting centroids...')
    fonk10(centroids, vec1, b18, b10)
if b19 = = "__main__":
    fonk12()