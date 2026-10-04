from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
from random import seed
from random import randrange
from csv import reader
from math import sqrt
from sklearn import linear_model
import pandas as pd
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
b1 = pd.read_csv('/home/soumen/Desktop/TML_HW3_AT/winequalityRed.csv', header = None)
print("Shape of the training b1 is {}".format(b1.shape))
[m ,n] = b1.shape
b2 = b1.iloc[:, 0:n-1].values
b3 = b1.iloc[:, n-1:n].values
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, b4 = train_test_split(b2, b3, test_size=0.3,
                                                    b5 = 1)
b6 = [0]
b7 = [0]
for i in range(1, 3):
    b8 = PolynomialFeatures(degree=i)
    b9 = b8.fit_transform(x_train)
    b10 = b8.fit_transform(x_test)
    b11 = linear_model.LinearRegression()
    b11.fit(b9, y_train)
    print("The degree of the polynomial is {}".format(i))
    b12 = b11.predict(b10)
    b13 = b11.predict(b9)
    b14 = mean_squared_error(b4, b12)
    b15 = mean_squared_error(y_train, b13)
    b6.append(b14)
    b7.append(b15)
    print("The test Accuracy is {}".format(b14))
    print("The training Accuracy is {}".format(b15))
    print('.............................................')
plt.figure(1)
plt.subplot(211)
plt.plot(b7)
plt.ylabel('Training Error(MSE)')
plt.xlabel('Degree of the polynomial')
plt.grid(True)
plt.subplot(212)
plt.plot(b6)
plt.ylabel('Testing Error(MSE)')
plt.xlabel('Degree of the polynomial')
plt.grid(True)
plt.show()