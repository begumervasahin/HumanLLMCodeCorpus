import numpy as np
import matplotlib.pyplot as plt
from load_data import load_mnist
import pandas as pd
import timeit
b1 = load_mnist()
images, b2 = b1['data'], b1['target']
def fonk1(b21):
    b3 = np.mean(b21, b13=0)
    b4 = np.b4(b21, b13=0)
    b5 = np.where(b4 == 0, 1., b4)
    b6 = (b21 - b3) / b5
    return b6, b3, b4
def fonk2(b21, num_components):
    b6, b7, b7 = fonk1(b21)
    b8 = np.cov(b6, rowvar=False, bias=True)
    eigenvalues, b9 = np.linalg.eig(b8)
    b10 = np.argsort(eigenvalues)[::-1]
    b11 = b9[:, b10][:, :num_components]
    b12 = np.dot(b11.T, b6.T).T
    return b12
def fonk3(predict, actual):
    return np.square(predict - actual).sum(b13 = 1).mean()
def fonk4(func, b14 = 10):
    b15 = []
    for b7 in range(b14):
        b16 = timeit.default_timer()
        func()
        b17 = timeit.default_timer()
        b15.append(b17 - b16)
    b18 = np.mean(b15)
    b19 = np.b4(b15)
    return b18, b19
def fonk5(b21, n_components):
    N, b7 = b21.shape
    b8 = (b21 @ b21.T) / N
    eigenvalues, b9 = np.linalg.eig(b8)
    b10 = np.argsort(eigenvalues)[::-1]
    b20 = b9[:, b10][:, :n_components]
    b11 = b20 @ np.linalg.inv(b20.T @ b20) @ b20.T
    b12 = b11 @ b21.T
    return b12.T
a1 = 1000
b21 = (images.reshape(-1, 28 * 28)[:a1]) / 255.
b6, b7, b7 = fonk1(b21)
np.testing.assert_almost_equal(fonk2(b6, 2), fonk5(b6, 2))
b22 = []
for num_component in range(1, 100):
    b23 = fonk2(b6, num_component)
    b24 = fonk3(b23, b6)
    b22.append((num_component, b24))
b22 = np.asarray(b22)
plt.plot(b22[:, 0], b22[:, 1])
plt.axhline(100, b25 = '--', color='r', b30=2)
plt.xlabel('Number of Components')
plt.ylabel('Mean Squared Error (MSE)')
plt.title('MSE vs Number of Principal Components')
plt.show()
b26 = {'Size of Dataset': [], 'Mean Time': [], 'Std Time': []}
for datasetsize in np.arange(4, 784, b27 = 50):
    b28 = b6[:datasetsize]
    b18, b19 = fonk4(lambda: b28.T @ b28)
    b26['Size of Dataset'].append(datasetsize)
    b26['Mean Time'].append(b18)
    b26['Std Time'].append(b19)
b29 = pd.DataFrame(b26)
plt.errorbar(b29['Size of Dataset'], b29['Mean Time'], b29['Std Time'], b30 = 2)
plt.xlabel('Size of Dataset')
plt.ylabel('Running Time')
plt.title('Running Time vs Size of Dataset')
plt.show()
b31 = {'Number of Datapoints': [], 'Mean Time (PCA)': [], 'Std Time (PCA)': [],
                 'Mean Time (PCA_high_dim)': [], 'Std Time (PCA_high_dim)': []}
for datasetsize in np.arange(4, 784, b27 = 100):
    b28 = b6[:datasetsize]
    mean_time_pca, b32 = fonk4(lambda: fonk2(b28, 2), b14=10)
    mean_time_high_dim, b33 = fonk4(lambda: fonk5(b28, 2), b14=10)
    b31['Number of Datapoints'].append(datasetsize)
    b31['Mean Time (PCA)'].append(mean_time_pca)
    b31['Std Time (PCA)'].append(b32)
    b31['Mean Time (PCA_high_dim)'].append(mean_time_high_dim)
    b31['Std Time (PCA_high_dim)'].append(b33)
b34 = pd.DataFrame(b31)
plt.errorbar(b34['Number of Datapoints'], b34['Mean Time (PCA)'], b34['Std Time (PCA)'], b35 = 'PCA', b30=2)
plt.errorbar(b34['Number of Datapoints'], b34['Mean Time (PCA_high_dim)'], b34['Std Time (PCA_high_dim)'], b35 = 'PCA_high_dim', b30=2)
plt.xlabel('Number of Datapoints')
plt.ylabel('Run Time')
plt.title('Run Time vs Number of Datapoints')
plt.legend()
plt.show()
mean_time_pca, b32 = fonk4(lambda: fonk2(b6, 2))
mean_time_high_dim, b33 = fonk4(lambda: fonk5(b6, 2))
print("Time taken for PCA:", mean_time_pca, "+/-", b32)
print("Time taken for PCA_high_dim:", mean_time_high_dim, "+/-", b33)