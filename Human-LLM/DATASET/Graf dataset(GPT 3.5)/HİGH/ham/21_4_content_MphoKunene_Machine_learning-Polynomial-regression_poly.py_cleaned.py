import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = [[12], [18], [20], [25], [27]]
b2 = [[14], [15], [16], [20], [27]]
b3 = [[12], [20], [45], [47]]
b4 = [[14], [16], [50], [52]]
b5 = LinearRegression()
b5.fit(b1, b2)
b6 = np.linspace(0, 28, 110)
b7 = b5.predict(b6.reshape(b6.shape[0], 1))
plt.plot(b6, b7)
b8 = PolynomialFeatures(degree=2)
b9 = b8.fit_transform(b1)
b10 = b8.transform(b3)
b11 = LinearRegression()
b11.fit(b9, b2)
b12 = b8.transform(b6.reshape(b6.shape[0], 1))
plt.plot(b6, b11.predict(b12), b13 = 'r', linestyle='--')
plt.title('Fish Tank price regressed on diameter')
plt.xlabel('Diameter in inches')
plt.ylabel('Price in dollars')
plt.axis([0, 30, 0, 30])
plt.grid(True)
plt.scatter(b1, b2)
plt.show()
print b1
print b9
print b3
print b10