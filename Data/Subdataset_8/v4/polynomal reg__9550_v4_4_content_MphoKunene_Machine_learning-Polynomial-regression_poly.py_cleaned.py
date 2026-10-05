import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
x_train = [[12], [18], [20], [25], [27]]
y_train = [[14], [15], [16], [20], [27]]
x_test = [[12], [20], [45], [47]]
y_test = [[14], [16], [50], [52]]
regressor = LinearRegression()
regressor.fit(x_train, y_train)
xx = np.linspace(0, 28, 110)
yy = regressor.predict(xx.reshape(xx.shape[0], 1))
plt.plot(xx, yy)
quadratic_featurizer = PolynomialFeatures(degree=2)
x_train_quadratic = quadratic_featurizer.fit_transform(x_train)
x_test_quadratic = quadratic_featurizer.transform(x_test)
regressor_quadratic = LinearRegression()
regressor_quadratic.fit(x_train_quadratic, y_train)
xx_quadratic = quadratic_featurizer.transform(xx.reshape(xx.shape[0], 1))
plt.plot(xx, regressor_quadratic.predict(xx_quadratic), c='r', linestyle='--')
plt.scatter(x_train, y_train)
plt.title('Fish Tank price regressed on diameter')
plt.xlabel('Diameter in inches')
plt.ylabel('Price in dollars')
plt.axis([0, 30, 0, 30])
plt.grid(True)
plt.show()
print("Training data (linear):", x_train)
print("Training data (quadratic):", x_train_quadratic)
print("Test data (linear):", x_test)
print("Test data (quadratic):", x_test_quadratic)