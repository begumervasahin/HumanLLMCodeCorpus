import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b1 = pd.ExcelFile('mice_protein.xlsx')
b2 = b1.parse('Data_Cortex_Nuclear')
b3 = b2.iloc[:, 1:78]
b4 = b3.mean(axis=0)
b5 = b3.apply(lambda col: col.fillna(col.mean()), axis=0)
b6 = np.cov(b5.transpose())
eigen_values, b7 = np.linalg.eig(b6)
b8 = b7[:, :2]
b9 = np.dot(b8.T, b5.T).T
b10 = b9[:, 0]
b11 = b9[:, 1]
b12 = b2.iloc[:, 81]
b13 = {
    'c-CS-m': {'range': slice(0, 149), 'b15': 'blue'},
    'c-SC-m': {'range': slice(150, 299), 'b15': 'red'},
    'c-CS-s': {'range': slice(300, 434), 'b15': 'green'},
    'c-SC-s': {'range': slice(435, 569), 'b15': 'yellow'},
    't-CS-m': {'range': slice(570, 704), 'b15': 'orange'},
    't-SC-m': {'range': slice(705, 839), 'b15': 'pink'},
    't-CS-s': {'range': slice(840, 944), 'b15': 'black'},
    't-SC-s': {'range': slice(945, 1079), 'b15': 'brown'},
}
for b17, settings in b13.items():
    plt.plot(
        b9[settings['range'], 0],
        b9[settings['range'], 1],
        '*',
        b14 = 3,
        b15 = settings['b15'],
        b16 = 0.5,
        b17 = b17
    )
plt.title("Scatter Plot of Principal Components")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.legend()
plt.show()