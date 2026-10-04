import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data_file = pd.ExcelFile('mice_protein.xlsx')
df = data_file.parse('Data_Cortex_Nuclear')
protein_data = df.iloc[:, 1:78]
protein_data_filled = protein_data.apply(lambda col: col.fillna(col.mean()), axis=0)
covariance_matrix = np.cov(protein_data_filled.transpose())
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
principal_components = eigenvectors[:, :2]
projected_data = np.dot(principal_components.T, protein_data_filled.transpose()).transpose()
pc1 = projected_data[:, 0]
pc2 = projected_data[:, 1]
groups = {
    'c-CS-m': (0, 149, 'blue'),
    'c-SC-m': (150, 299, 'red'),
    'c-CS-s': (300, 434, 'green'),
    'c-SC-s': (435, 569, 'yellow'),
    't-CS-m': (570, 704, 'orange'),
    't-SC-m': (705, 839, 'pink'),
    't-CS-s': (840, 944, 'black'),
    't-SC-s': (945, 1079, 'brown')
}
plt.figure(figsize=(10, 8))
for label, (start, end, color) in groups.items():
    plt.plot(pc1[start:end], pc2[start:end], '*', markersize=3, color=color, alpha=0.5, label=label)
plt.title("Scatter Plot of Principal Components")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.legend()
plt.show()