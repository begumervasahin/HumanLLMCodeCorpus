import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
np.random.seed(2)
b1 = np.random.normal(3.0, 1.0, 100)
b2 = np.random.normal(50.0, 30.0, 100) / b1
plt.scatter(b1, b2)
plt.xlabel('Page Speeds')
plt.ylabel('Purchase Amount')
plt.title('Relationship between Page Speeds and Purchase Amount')
plt.show()
train_x, b3 = b1[:80], b1[80:]
train_y, b4 = b2[:80], b2[80:]
plt.scatter(train_x, train_y, b5 = 'Training Data')
plt.scatter(b3, b4, b5 = 'Testing Data')
plt.xlabel('Page Speeds')
plt.ylabel('Purchase Amount')
plt.title('Training and Testing Data Split')
plt.legend()
plt.show()
b6 = np.poly1d(np.polyfit(train_x, train_y, 7))
b7 = np.linspace(0, 7, 100)
plt.scatter(train_x, train_y, b5 = 'Training Data')
plt.plot(b7, b6(b7), b8 = 'b', b5='Fitted Model')
plt.xlabel('Page Speeds')
plt.ylabel('Purchase Amount')
plt.title('Fitted Polynomial Regression Model')
plt.legend()
plt.show()
b9 = r2_score(b4, b6(b3))
print("R-squared score for testing data:", b9)
b10 = r2_score(train_y, b6(train_x))
print("R-squared score for training data:", b10)