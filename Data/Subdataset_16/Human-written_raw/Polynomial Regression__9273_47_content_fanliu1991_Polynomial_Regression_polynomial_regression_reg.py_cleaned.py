import assignment1 as a1
import numpy as np
import matplotlib.pyplot as plt
(countries, features, values) = a1.load_unicef_data()
print ''
b1 = values[:,1]
b2 = values[:,7:]
b2 = a1.normalize_data(b2)
b3 = 100;
b4 = b2[0:b3,:]
b5 = b1[0:b3]
b6 = [0, 0.01, 0.1, 1, 10, 100, 1000, 10000]
b7 = np.ones(shape=(100,1))
b8 = b7
for degree_index in range(2):
  b9 = degree_index + 1
  b8 = np.concatenate((b8, np.power(b4, b9)), axis=1)
b10 = np.shape(b8)[1]
b11 = np.identity(b10)
b12 = len(b5) / 10
b13 = []
for lambda_index in range(len(b6)):
  b14 = b6[lambda_index]
  b15 = []
  for validation_index in range(10):
    b16 = validation_index * b12
    b17 = b8[b16:b16+b12,:]
    b18 = b5[b16:b16+b12,:]
    b19 = np.concatenate((b8[0:b16,:], b8[b16+b12:,:]), axis=0)
    b20 = np.concatenate((b5[0:b16,:], b5[b16+b12:,:]), axis=0)
    b21 = np.dot(np.dot(np.linalg.inv(np.add(np.dot(b14, b11), np.dot(b19.transpose(), b19))), b19.transpose()), b20)
    b22 = np.sqrt(0.5 * np.sum(np.square(np.dot(b17, b21) - b18)) * 2 / len(b18))
    b15.append(b22)
  b13.append(np.mean(b15))
print(b13)
plt.semilogx(b6[1:8], b13[1:8])
plt.xlabel('b24 Value on log Scale')
plt.ylabel('Average Validation Set Error')
plt.title('Average Validation Set Error vs. b24 Value on log Scale ')
plt.axhline(b23 = b13[0], linewidth=2, color = 'g', label = '')
plt.legend(['Average validation set error', 'Unregularized result, b24 = 0'])
plt.show()