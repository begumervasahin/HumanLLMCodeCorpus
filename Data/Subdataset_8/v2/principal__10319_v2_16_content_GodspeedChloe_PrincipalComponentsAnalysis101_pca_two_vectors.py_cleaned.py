import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans2
def read_csv(file_name):
    records = []
    with open(file_name) as data:
        header = data.readline().strip().split(',')
        for line in data.readlines():
            values = [int(val.strip()) for val in line.strip().split(',')]
            records.append(values)
    return records, header
def compute_covariance(records):
    data_matrix = np.asarray([rec[1:] for rec in records]).T
    return np.cov(data_matrix)
def compute_eigenv(C):
    eigenvalues, eigenvectors = np.linalg.eig(C)
    return eigenvalues, eigenvectors
def normalize_eigenvalues(eigenvalues):
    total_sum = np.sum(eigenvalues)
    return eigenvalues / total_sum
def plot_eigenvalues(eigenvalues):
    cumulative_sum = np.cumsum(eigenvalues)
    plt.plot(range(len(eigenvalues) + 1), np.hstack([0, cumulative_sum]), 'bo-', label='Eigenvalues')
    plt.xlabel('Eigenvalue ID (decreasing magnitude)')
    plt.ylabel('Variance captured')
    plt.title('Eigenvalues And Their Captured Variance')
    plt.legend()
    plt.show()
def two_best_vectors(eigenvalues, eigenvectors):
    sorted_indices = np.argsort(eigenvalues)[::-1]
    return eigenvectors[:, sorted_indices[0]], eigenvectors[:, sorted_indices[1]]
def subtract_means(data):
    means = np.mean(data, axis=0)
    centered_data = data - means
    return means, centered_data
def project_with_two_vectors(data, vec1, vec2):
    projected_data = np.dot(data, np.vstack((vec1, vec2)).T)
    plt.plot(projected_data[:, 0], projected_data[:, 1], 'bo')
    plt.xlabel('AMOUNT OF PRINCIPAL COMPONENT 1')
    plt.ylabel('AMOUNT OF PRINCIPAL COMPONENT 2')
    plt.title('Data Projected Onto 2D PCA Space')
    plt.show()
    return projected_data
def round_vectors(vectors):
    return np.round(vectors, 2)
def reproject_centroids(centroids, vec1, vec2, means):
    reprojected_centroids = centroids.dot(np.vstack((vec1, vec2))) + means
    for centroid in reprojected_centroids:
        print('Centroid:')
        print(centroid)
def usage():
    print('USAGE: python3 pca_two_vectors.py <filename>.csv')
    sys.exit()
def main():
    if len(sys.argv) != 2:
        usage()
    file_name = sys.argv[1]
    records, _ = read_csv(file_name)
    print('Part one: Reading in CSV...')
    print('Part two: Computing covariance matrix C...')
    C = compute_covariance(records)
    print(C)
    print('Part three: Computing eigenvalues and eigenvectors...')
    eigenvalues, eigenvectors = compute_eigenv(C)
    print('Eigenvalues:\n', eigenvalues)
    print('Eigenvectors:\n', eigenvectors)
    print('Part four: Sorting and normalizing eigenvalues...')
    normalized_eigenvalues = normalize_eigenvalues(eigenvalues)
    print(normalized_eigenvalues)
    print('Part five: Plotting eigenvalues...')
    plot_eigenvalues(normalized_eigenvalues)
    print('Part six: Selecting the two best eigenvectors...')
    vec1, vec2 = two_best_vectors(eigenvalues, eigenvectors)
    print('Best eigenvector:\n', vec1)
    print('Second best eigenvector:\n', vec2)
    print('Part seven: Subtracting means from the data...')
    means, centered_data = subtract_means(records)
    print('Part eight: Projecting data onto two eigenvectors...')
    projected_data = project_with_two_vectors(centered_data, vec1, vec2)
    print('Part nine: Performing k-Means clustering...')
    centroids, _ = kmeans2(projected_data, 3, iter=20, minit='random')
    print('Part ten: Reprojecting centroids...')
    reproject_centroids(centroids, vec1, vec2, means)
if __name__ == "__main__":
    main()