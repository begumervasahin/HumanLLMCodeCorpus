import numpy as np
def zeroMean(datamat):
    mean = np.mean(datamat, axis=0)
    newdata = datamat - mean
    return newdata, mean
def pca(datamat):
    newdata, mean = zeroMean(datamat)
    covmat = np.cov(newdata, rowvar=0)
    eigvals, eigvects = np.linalg.eig(np.mat(covmat))
    eigvals_sort = np.argsort(eigvals)[::-1]
    eigval_final = eigvals[eigvals_sort]
    eigvect_final = eigvects[:, eigvals_sort]
    return eigval_final, eigvect_final
def percent_percentage(eigvals, percentage):
    total_variance = sum(eigvals)
    cumulative_variance = 0
    num_components = 0
    for eigval in eigvals:
        cumulative_variance += eigval
        num_components += 1
        if cumulative_variance >= total_variance * percentage:
            break
    result_percent = np.zeros(num_components)
    for i in range(num_components):
        result_percent[i] = eigvals[i] / total_variance
    return num_components, result_percent
def percent_all(eigvals):
    _, percent = percent_percentage(eigvals, 1)
    return percent
def percent_over_10(eigvals):
    _, percent = percent_percentage(eigvals, 1)
    num_components = sum(1 for p in percent if p > 0.1)
    percent = percent[:num_components]
    return num_components, percent
def product(datamat, eigvect, num):
    eigvect_final = eigvect[:, :num]
    low_data = np.dot(datamat, eigvect_final)
    return low_data
if __name__ == "__main__":
    datamat = np.array([
        [2.5, 2.4],
        [0.5, 0.7],
        [2.2, 2.9],
        [1.9, 2.2],
        [3.1, 3.0],
        [2.3, 2.7],
        [2.0, 1.6],
        [1.0, 1.1],
        [1.5, 1.6],
        [1.1, 0.9]
    ])
    eigvals, eigvects = pca(datamat)
    print("Eigenvalues:", eigvals)
    print("Eigenvectors:\n", eigvects)
    num, percent = percent_over_10(eigvals)
    print("Number of components with >10% variance:", num)
    print("Percentage of variance for these components:", percent)
    low_data = product(datamat, eigvects, num)
    print("Reduced data:\n", low_data)