import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data_file = pd.ExcelFile('mice_protein.xlsx')
df1 = data_file.parse('Data_Cortex_Nuclear')
v1_null = df1.iloc[:, 1:78]
mean_values = v1_null.mean(axis=0)
modified_v1 = v1_null.apply(lambda col: col.fillna(col.mean()), axis=0)
covariance_matrix = np.cov(modified_v1.transpose())
eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)
eig_vectors_selected = eigen_vectors[:, :2]
projected_data = np.dot(eig_vectors_selected.T, modified_v1.T).T
pc1 = projected_data[:, 0]
pc2 = projected_data[:, 1]
labels = df1.iloc[:, 81]
plot_settings = {
    'c-CS-m': {'range': slice(0, 149), 'color': 'blue'},
    'c-SC-m': {'range': slice(150, 299), 'color': 'red'},
    'c-CS-s': {'range': slice(300, 434), 'color': 'green'},
    'c-SC-s': {'range': slice(435, 569), 'color': 'yellow'},
    't-CS-m': {'range': slice(570, 704), 'color': 'orange'},
    't-SC-m': {'range': slice(705, 839), 'color': 'pink'},
    't-CS-s': {'range': slice(840, 944), 'color': 'black'},
    't-SC-s': {'range': slice(945, 1079), 'color': 'brown'},
}
for label, settings in plot_settings.items():
    plt.plot(
        projected_data[settings['range'], 0],
        projected_data[settings['range'], 1],
        '*',
        markersize=3,
        color=settings['color'],
        alpha=0.5,
        label=label
    )
plt.title("Scatter Plot of Principal Components")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.legend()
plt.show()