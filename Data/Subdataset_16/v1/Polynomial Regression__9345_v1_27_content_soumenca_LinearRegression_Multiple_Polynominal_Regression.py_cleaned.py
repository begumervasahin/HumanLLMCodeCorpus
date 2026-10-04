import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
b1 = pd.read_csv('/home/soumen/Desktop/TML_HW3_AT/winequalityRed.csv', header=None)
print("Shape of the training b1 is {}".format(b1.shape))
[m, n] = b1.shape
b2 = b1.iloc[:, 0:n-1].values
b3 = b1.iloc[:, n-1].values
x_train, x_test, y_train, b4 = train_test_split(b2, b3, test_size=0.3, random_state=1)
b5 = [0]
b6 = [0]
for i in range(1, 3):
    b7 = PolynomialFeatures(degree=i)
    b8 = b7.fit_transform(x_train)
    b9 = b7.fit_transform(x_test)
    b10 = LinearRegression()
    b10.fit(b8, y_train)
    b11 = b10.predict(b8)
    b12 = b10.predict(b9)
    b13 = mean_squared_error(y_train, b11)
    b14 = mean_squared_error(b4, b12)
    b6.append(b13)
    b5.append(b14)
    print("The degree of the polynomial is {}".format(i))
    print("The test Accuracy (MSE) is {}".format(b14))
    print("The training Accuracy (MSE) is {}".format(b13))
    print('.............................................')
plt.figure(1)
plt.subplot(211)
plt.plot(b6)
plt.ylabel('Training Error (MSE)')
plt.xlabel('Degree of the polynomial')
plt.grid(True)
plt.subplot(212)
plt.plot(b5)
plt.ylabel('Testing Error (MSE)')
plt.xlabel('Degree of the polynomial')
plt.grid(True)
plt.show()