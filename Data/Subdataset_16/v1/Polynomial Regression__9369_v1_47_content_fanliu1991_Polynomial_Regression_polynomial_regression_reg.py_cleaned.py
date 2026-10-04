import numpy as np
import matplotlib.pyplot as plt
import assignment1 as a1
(countries, features, values) = a1.load_unicef_data()
b1 = values[:, 1]
b2 = values[:, 7:]
b2 = a1.normalize_data(b2)
a1 = 100
b3 = b2[0:a1, :]
b4 = b1[0:a1]
b5 = [0, 0.01, 0.1, 1, 10, 100, 1000, 10000]
b6 = np.ones(shape=(a1, 1))
b7 = b6
for degree_index in range(2):
    b8 = degree_index + 1
    b7 = np.concatenate((b7, np.power(b3, b8)), axis=1)
b9 = np.shape(b7)[1]
b10 = np.identity(b9)
b11 = a1
b12 = []
for lambda_value in b5:
    b13 = []
    for validation_index in range(10):
        b14 = validation_index * b11
        b15 = b14 + b11
        b16 = b7[b14:b15, :]
        b17 = b4[b14:b15]
        b18 = np.concatenate((b7[:b14, :], b7[b15:, :]), axis=0)
        b19 = np.concatenate((b4[:b14], b4[b15:]), axis=0)
        b20 = np.linalg.inv(lambda_value * b10 + b18.T @ b18) @ b18.T @ b19
        b21 = np.sqrt(0.5 * np.sum((b16 @ b20 - b17) ** 2) * 2 / len(b17))
        b13.append(b21)
    b12.append(np.mean(b13))
print(b12)
plt.semilogx(b5[1:], b12[1:])
plt.xlabel('b23 Value on log Scale')
plt.ylabel('Average Validation Set Error')
plt.title('Average Validation Set Error vs. b23 Value on log Scale')
plt.axhline(b22 = b12[0], linewidth=2, color='g')
plt.legend(['Average validation set error', 'Unregularized result, b23 = 0'])
plt.show()