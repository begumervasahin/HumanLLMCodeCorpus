import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
np.random.seed(2)
b1 = np.random.normal(3.0, 1.0, 100)
b2 = np.random.normal(50.0, 30.0, 100) / b1
plt.scatter(b1, b2)
plt.xlabel('Page Speeds')
plt.ylabel('Purchase Amount')
plt.title('Scatter plot of Page Speeds vs Purchase Amount')
plt.show()
b3 = b1[:80]
b4 = b1[80:]
b5 = b2[:80]
b6 = b2[80:]
plt.scatter(b3, b5, b7 = 'Training Data')
plt.scatter(b4, b6, b7 = 'Testing Data')
plt.xlabel('Page Speeds')
plt.ylabel('Purchase Amount')
plt.title('Scatter plot of Training and Testing Data')
plt.legend()
plt.show()
b8 = np.array(b3)
b9 = np.array(b5)
b10 = np.poly1d(np.polyfit(b8, b9, 7))
b11 = np.linspace(0, 7, 100)
plt.scatter(b3, b5, b7 = 'Training Data')
plt.plot(b11, b10(b11), b12 = 'b', b7='Fitted Model')
plt.xlabel('Page Speeds')
plt.ylabel('Purchase Amount')
plt.title('Fitted Polynomial Regression Model')
plt.legend()
plt.show()
b13 = np.array(b4)
b14 = np.array(b6)
b15 = r2_score(b14, b10(b13))
print("R-squared score for testing data:", b15)
b16 = r2_score(np.array(b5), b10(np.array(b3)))
print("R-squared score for training data:", b16)