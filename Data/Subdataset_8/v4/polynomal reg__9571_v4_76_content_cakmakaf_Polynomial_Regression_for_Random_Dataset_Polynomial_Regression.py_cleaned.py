
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
np.random.seed(2)
pageSpeeds = np.random.normal(3.0, 1.0, 100)
purchaseAmount = np.random.normal(50.0, 30.0, 100) / pageSpeeds
plt.scatter(pageSpeeds, purchaseAmount)
plt.xlabel("Page Speeds")
plt.ylabel("Purchase Amount")
plt.title("Page Speeds vs. Purchase Amount")
plt.show()
trainX = pageSpeeds[:80]
testX = pageSpeeds[80:]
trainY = purchaseAmount[:80]
testY = purchaseAmount[80:]
plt.scatter(trainX, trainY, label="Training Data")
plt.scatter(testX, testY, label="Testing Data")
plt.xlabel("Page Speeds")
plt.ylabel("Purchase Amount")
plt.legend()
plt.title("Training and Testing Data")
plt.show()
p4 = np.poly1d(np.polyfit(trainX, trainY, 7))
xp = np.linspace(0, 7, 100)
plt.scatter(trainX, trainY, label="Training Data")
plt.plot(xp, p4(xp), c='b', label="Polynomial Fit")
plt.xlabel("Page Speeds")
plt.ylabel("Purchase Amount")
plt.legend()
plt.title("Polynomial Fit on Training Data")
plt.show()
plt.scatter(testX, testY, label="Testing Data")
plt.plot(xp, p4(xp), c='b', label="Polynomial Fit")
plt.xlabel("Page Speeds")
plt.ylabel("Purchase Amount")
plt.legend()
plt.title("Polynomial Fit on Testing Data")
plt.show()
r2_test = r2_score(testY, p4(testX))
print("R-squared score for testing data:", r2_test)
r2_train = r2_score(trainY, p4(trainX))
print("R-squared score for training data:", r2_train)