import assignment1 as a1
import numpy as np
import matplotlib.pyplot as plt
countries, features, b1 = a1.load_unicef_data()
b2 = b1[:, 1]
b3 = b1[:, 7:]
b3 = a1.normalize_data(b3)
a1 = 100
b4 = b3[:a1, :]
b5 = b2[:a1]
b6 = [0, 0.01, 0.1, 1, 10, 100, 1000, 10000]
b7 = np.ones((a1, 1))
b8 = b7
for degree_index in range(2):
    b9 = degree_index + 1
    b8 = np.concatenate((b8, np.power(b4, b9)), axis=1)
b10 = b8.shape[1]
b11 = np.identity(b10)
b12 = a1
b13 = []
for lambda_value in b6:
    b14 = []
    for validation_index in range(10):
        b15 = validation_index * b12
        b16 = b15 + b12
        b17 = b8[b15:b16, :]
        b18 = b5[b15:b16]
        b19 = np.concatenate((b8[:b15, :], b8[b16:, :]), axis=0)
        b20 = np.concatenate((b5[:b15], b5[b16:]), axis=0)
        b21 = np.linalg.inv(lambda_value * b11 + b19.T @ b19) @ b19.T @ b20
        b22 = np.sqrt(np.mean((b17 @ b21 - b18) ** 2))
        b14.append(b22)
    b13.append(np.mean(b14))
print(b13)
plt.semilogx(b6[1:], b13[1:], b23 = 'o')
plt.xlabel('Lambda Value (log scale)')
plt.ylabel('Average Validation Set Error')
plt.title('Average Validation Set Error vs. Lambda Value')
plt.axhline(b24 = b13[0], linewidth=2, color='g', label='Unregularized result, Lambda = 0')
plt.legend()
plt.show()