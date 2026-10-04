import numpy as np
import matplotlib.pyplot as plt
import assignment1 as a1
countries, features, b1 = a1.load_unicef_data()
b2 = b1[:, 1]
b3 = b1[:, 7:]
b3 = a1.normalize_data(b3)
a1 = 100
b4 = b3[:a1, :]
b5 = b2[:a1]
b6 = [0, 0.01, 0.1, 1, 10, 100, 1000, 10000]
b7 = np.ones((a1, 1))
for degree in range(1, 3):
    b7 = np.concatenate((b7, np.power(b4, degree)), axis=1)
b8 = b7.shape[1]
b9 = np.identity(b8)
b10 = a1
b11 = []
for lambda_value in b6:
    b12 = []
    for i in range(10):
        b13 = i * b10
        b14 = b13 + b10
        b15 = b7[b13:b14, :]
        b16 = b5[b13:b14]
        b17 = np.concatenate((b7[:b13, :], b7[b14:, :]), axis=0)
        b18 = np.concatenate((b5[:b13], b5[b14:]), axis=0)
        b19 = np.linalg.inv(lambda_value * b9 + b17.T @ b17) @ b17.T @ b18
        b20 = np.sqrt(np.mean((b15 @ b19 - b16) ** 2))
        b12.append(b20)
    b11.append(np.mean(b12))
print(b11)
plt.semilogx(b6[1:], b11[1:], b21 = 'Average validation set error')
plt.xlabel('Lambda Value (log scale)')
plt.ylabel('Average Validation Set Error')
plt.title('Average Validation Set Error vs. Lambda Value on log Scale')
plt.axhline(b22 = b11[0], linewidth=2, color='g', b21='Unregularized result, Lambda = 0')
plt.legend()
plt.show()