import numpy as np
import timeit
import matplotlib.pyplot as plt
from load_data import load_mnist
b1 = load_mnist()
images, b2 = b1['data'], b1['target']
def fonk1(b23):
    b3 = np.mean(b23, b14=0)
    b4 = np.b4(b23, b14=0)
    b5 = b4.copy()
    b5[b4 = = 0] = 1.
    b6 = (b23 - b3) / b5
    return b6, b3, b4
def fonk2(b23, num_components):
    b6, mean, b4 = fonk1(b23)
    b7 = np.cov(b6, rowvar=False, bias=True)
    eigenvalues, b8 = np.linalg.eig(b7)
    b9 = np.argsort(eigenvalues)[::-1]
    b10 = eigenvalues[b9]
    b11 = b8[:, b9]
    b12 = b11[:, :num_components]
    b13 = np.dot(b12.T, b6.T).T
    return b13
def fonk3(predict, actual):
    return np.square(predict - actual).sum(b14 = 1).mean()
def fonk4(f, b15 = 10):
    b16 = []
    for _ in range(b15):
        b17 = timeit.default_timer()
        f()
        b18 = timeit.default_timer()
        b16.append(b18 - b17)
    b19 = np.mean(b16)
    b20 = np.b4(b16)
    return b19, b20
def fonk5(b23, n_components):
    N, b21 = b23.shape
    b7 = (b23 @ b23.T) / N
    eigenvalues, b8 = np.linalg.eig(b7)
    b9 = np.argsort(eigenvalues)[::-1]
    b10 = eigenvalues[b9]
    b11 = b8[:, b9]
    b22 = b11[:, :n_components]
    b12 = b22 @ np.linalg.inv(b22.T @ b22) @ b22.T
    b13 = b12 @ b23.T
    return b13.T
a1 = 1000
b23 = (images.reshape(-1, 28 * 28)[:a1]) / 255.
b6, mean, b4 = fonk1(b23)
np.testing.assert_almost_equal(fonk2(b6, 2), fonk5(b6, 2))
b24 = []
for num_component in range(1, 100):
    b25 = fonk2(b6, num_component)
    b26 = fonk3(b25, b6)
    b24.append((num_component, b26))
b24 = np.asarray(b24)
plt.plot(b24[:, 0], b24[:, 1])
plt.axhline(100, b27 = '--', color='r', b32=2)
plt.xlabel('Number of Components')
plt.ylabel('Mean Squared Error (MSE)')
plt.title('MSE vs Number of Principal Components')
plt.show()
b28 = {'Size of Dataset': [], 'Mean Time': [], 'Std Time': []}
for datasetsize in np.arange(4, 784, b29 = 50):
    b30 = b6[:datasetsize]
    b19, b20 = fonk4(lambda: b30.T @ b30)
    b28['Size of Dataset'].append(datasetsize)
    b28['Mean Time'].append(b19)
    b28['Std Time'].append(b20)
b31 = pd.DataFrame(b28)
plt.errorbar(b31['Size of Dataset'], b31['Mean Time'], b31['Std Time'], b32 = 2)
plt.xlabel('Size of Dataset')
plt.ylabel('Running Time')
plt.title('Running Time vs Size of Dataset')
plt.show()
b33 = {'Number of Datapoints': [], 'Mean Time (PCA)': [], 'Std Time (PCA)': [],
                 'Mean Time (PCA_high_dim)': [], 'Std Time (PCA_high_dim)': []}
for datasetsize in np.arange(4, 784, b29 = 100):
    b30 = b6[:datasetsize]
    mean_time_pca, b34 = fonk4(lambda: fonk2(b30, 2), b15=10)
    mean_time_high_dim, b35 = fonk4(lambda: fonk5(b30, 2), b15=10)
    b33['Number of Datapoints'].append(datasetsize)
    b33['Mean Time (PCA)'].append(mean_time_pca)
    b33['Std Time (PCA)'].append(b34)
    b33['Mean Time (PCA_high_dim)'].append(mean_time_high_dim)
    b33['Std Time (PCA_high_dim)'].append(b35)
b36 = pd.DataFrame(b33)
plt.errorbar(b36['Number of Datapoints'], b36['Mean Time (PCA)'], b36['Std Time (PCA)'], b37 = 'PCA', b32=2)
plt.errorbar(b36['Number of Datapoints'], b36['Mean Time (PCA_high_dim)'], b36['Std Time (PCA_high_dim)'], b37 = 'PCA_high_dim', b32=2)
plt.xlabel('Number of Datapoints')
plt.ylabel('Run Time')
plt.title('Run Time vs Number of Datapoints')
plt.legend()
plt.show()
mean_time_pca, b34 = fonk4(lambda: fonk2(b6, 2))
mean_time_high_dim, b35 = fonk4(lambda: fonk5(b6, 2))
print("Time taken for PCA:", mean_time_pca, "+/-", b34)
print("Time taken for PCA_high_dim:", mean_time_high_dim, "+/-", b35)