import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
np.random.seed(2)
pageSpeeds = np.random.normal(3.0, 1.0, 100)
purchaseAmount = np.random.normal(50.0, 30.0, 100) / pageSpeeds
plt.scatter(pageSpeeds, purchaseAmount)
plt.xlabel('Page Speeds')
plt.ylabel('Purchase Amount')
plt.title('Relationship between Page Speeds and Purchase Amount')
plt.show()
trainX = pageSpeeds[:80]
testX = pageSpeeds[80:]
trainY = purchaseAmount[:80]
testY = purchaseAmount[80:]
plt.scatter(trainX, trainY, label='Training Data')
plt.scatter(testX, testY, label='Testing Data')
plt.xlabel('Page Speeds')
plt.ylabel('Purchase Amount')
plt.title('Training and Testing Data Split')
plt.legend()
plt.show()
x_train = np.array(trainX)
y_train = np.array(trainY)
poly_fit = np.poly1d(np.polyfit(x_train, y_train, 7))
x_values = np.linspace(0, 7, 100)
plt.scatter(trainX, trainY, label='Training Data')
plt.plot(x_values, poly_fit(x_values), c='b', label='Fitted Model')
plt.xlabel('Page Speeds')
plt.ylabel('Purchase Amount')
plt.title('Fitted Polynomial Regression Model')
plt.legend()
plt.show()
x_test = np.array(testX)
y_test = np.array(testY)
r2_test = r2_score(y_test, poly_fit(x_test))
print("R-squared score for testing data:", r2_test)
r2_train = r2_score(y_train, poly_fit(x_train))
print("R-squared score for training data:", r2_train)