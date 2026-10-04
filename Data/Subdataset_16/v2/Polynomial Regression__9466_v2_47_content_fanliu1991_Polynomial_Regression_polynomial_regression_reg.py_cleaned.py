import numpy as np
import matplotlib.pyplot as plt
import assignment1 as a1
(countries, features, values) = a1.load_unicef_data()
b1 = values[:, 1]
b2 = values[:, 7:]
b2 = a1.normalize_data(b2)
a1 = 100
b3 = b2[:a1, :]
b4 = b1[:a1]
b5 = [0, 0.01, 0.1, 1, 10, 100, 1000, 10000]
b6 = np.ones((a1, 1))
for degree in range(2):
    b6 = np.concatenate((b6, np.power(b3, degree + 1)), axis=1)
b7 = b6.shape[1]
b8 = np.identity(b7)
b9 = a1
b10 = []
for lambda_value in b5:
    b11 = []
    for i in range(10):
        b12 = i * b9
        b13 = b12 + b9
        b14 = b6[b12:b13, :]
        b15 = b4[b12:b13]
        b16 = np.concatenate((b6[:b12, :], b6[b13:, :]), axis=0)
        b17 = np.concatenate((b4[:b12], b4[b13:]), axis=0)
        b18 = np.linalg.inv(lambda_value * b8 + b16.T @ b16) @ b16.T @ b17
        b19 = np.sqrt(np.mean((b14 @ b18 - b15) ** 2))
        b11.append(b19)
    b10.append(np.mean(b11))
print(b10)
plt.semilogx(b5[1:], b10[1:], b20 = 'Average validation set error')
plt.xlabel('Lambda Value (log scale)')
plt.ylabel('Average Validation Set Error')
plt.title('Average Validation Set Error vs. Lambda Value on log Scale')
plt.axhline(b21 = b10[0], linewidth=2, color='g', b20='Unregularized result, Lambda = 0')
plt.legend()
plt.show()