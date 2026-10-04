import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
b1 = pd.read_csv('/home/soumen/Desktop/TML_HW3_AT/winequalityRed.csv', header=None)
print(f"Shape of the training b1 is {b1.shape}")
b2 = b1.iloc[:, :-1].values
b3 = b1.iloc[:, -1].values
x_train, x_test, y_train, b4 = train_test_split(b2, b3, test_size=0.3, random_state=1)
b5 = []
b6 = []
for degree in range(1, 3):
    b7 = PolynomialFeatures(degree=degree)
    b8 = b7.fit_transform(x_train)
    b9 = b7.fit_transform(x_test)
    b10 = LinearRegression()
    b10.fit(b8, y_train)
    b11 = b10.predict(b8)
    b12 = b10.predict(b9)
    b13 = mean_squared_error(y_train, b11)
    b14 = mean_squared_error(b4, b12)
    b5.append(b13)
    b6.append(b14)
    print(f"The degree of the polynomial is {degree}")
    print(f"Training MSE: {b13}")
    print(f"Testing MSE: {b14}")
    print('.............................................')
plt.figure(b15 = (10, 6))
plt.subplot(211)
plt.plot(range(1, 3), b5, b16 = 'o', linestyle='--', color='b')
plt.ylabel('Training Error (MSE)')
plt.xlabel('Degree of the Polynomial')
plt.grid(True)
plt.subplot(212)
plt.plot(range(1, 3), b6, b16 = 'o', linestyle='--', color='r')
plt.ylabel('Testing Error (MSE)')
plt.xlabel('Degree of the Polynomial')
plt.grid(True)
plt.tight_layout()
plt.show()