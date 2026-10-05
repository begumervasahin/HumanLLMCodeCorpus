import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
np.random.seed(2)
pageSpeeds = np.random.normal(3.0, 1.0, 100)
purchaseAmount = np.random.normal(50.0, 30.0, 100) / pageSpeeds
plt.scatter(pageSpeeds, purchaseAmount)
plt.xlabel('Page Speeds')
plt.ylabel('Purchase Amount')
plt.title('Scatter plot of Page Speeds vs Purchase Amount')
plt.show()
trainX = pageSpeeds[:80]
testX = pageSpeeds[80:]
trainY = purchaseAmount[:80]
testY = purchaseAmount[80:]
plt.scatter(trainX, trainY, label='Training Data')
plt.scatter(testX, testY, label='Testing Data')
plt.xlabel('Page Speeds')
plt.ylabel('Purchase Amount')
plt.title('Scatter plot of Training and Testing Data')
plt.legend()
plt.show()
x = np.array(trainX)
y = np.array(trainY)
p4 = np.poly1d(np.polyfit(x, y, 7))
xp = np.linspace(0, 7, 100)
plt.scatter(trainX, trainY, label='Training Data')
plt.plot(xp, p4(xp), c='b', label='Fitted Model')
plt.xlabel('Page Speeds')
plt.ylabel('Purchase Amount')
plt.title('Fitted Polynomial Regression Model')
plt.legend()
plt.show()
testx = np.array(testX)
testy = np.array(testY)
r2_test = r2_score(testy, p4(testx))
print("R-squared score for testing data:", r2_test)
r2_train = r2_score(np.array(trainY), p4(np.array(trainX)))
print("R-squared score for training data:", r2_train)