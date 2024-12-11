
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
np.random.seed(2)
b1 = np.random.normal(3.0, 1.0, 100)
b2 = np.random.normal(50.0, 30.0, 100) / b1
plt.scatter(b1, b2)
plt.xlabel("Page Speeds")
plt.ylabel("Purchase Amount")
plt.title("Page Speeds vs. Purchase Amount")
plt.show()
b3 = b1[:80]
b4 = b1[80:]
b5 = b2[:80]
b6 = b2[80:]
plt.scatter(b3, b5, b7 = "Training Data")
plt.scatter(b4, b6, b7 = "Testing Data")
plt.xlabel("Page Speeds")
plt.ylabel("Purchase Amount")
plt.legend()
plt.title("Training and Testing Data")
plt.show()
b8 = np.poly1d(np.polyfit(b3, b5, 7))
b9 = np.linspace(0, 7, 100)
plt.scatter(b3, b5, b7 = "Training Data")
plt.plot(b9, b8(b9), b10 = 'b', b7="Polynomial Fit")
plt.xlabel("Page Speeds")
plt.ylabel("Purchase Amount")
plt.legend()
plt.title("Polynomial Fit on Training Data")
plt.show()
plt.scatter(b4, b6, b7 = "Testing Data")
plt.plot(b9, b8(b9), b10 = 'b', b7="Polynomial Fit")
plt.xlabel("Page Speeds")
plt.ylabel("Purchase Amount")
plt.legend()
plt.title("Polynomial Fit on Testing Data")
plt.show()
b11 = r2_score(b6, b8(b4))
print("R-squared score for testing data:", b11)
b12 = r2_score(b5, b8(b3))
print("R-squared score for training data:", b12)