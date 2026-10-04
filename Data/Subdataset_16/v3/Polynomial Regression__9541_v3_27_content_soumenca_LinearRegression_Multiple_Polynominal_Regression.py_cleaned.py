import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
b1 = '/home/soumen/Desktop/TML_HW3_AT/winequalityRed.csv'
b2 = pd.read_csv(b1, header=None)
print(f"Shape of the dataset: {b2.shape}")
b3 = b2.iloc[:, :-1].values
b4 = b2.iloc[:, -1].values
x_train, x_test, y_train, b5 = train_test_split(b3, b4, test_size=0.3, random_state=1)
b6 = []
b7 = []
for degree in range(1, 3):
    b8 = PolynomialFeatures(degree=degree)
    b9 = b8.fit_transform(x_train)
    b10 = b8.transform(x_test)
    b11 = LinearRegression()
    b11.fit(b9, y_train)
    b12 = b11.predict(b9)
    b13 = b11.predict(b10)
    b14 = mean_squared_error(y_train, b12)
    b15 = mean_squared_error(b5, b13)
    b6.append(b14)
    b7.append(b15)
    print(f"Polynomial degree: {degree}")
    print(f"Training MSE: {b14:.4f}")
    print(f"Testing MSE: {b15:.4f}")
    print('------------------------------------')
plt.figure(b16 = (10, 6))
plt.subplot(2, 1, 1)
plt.plot(range(1, 3), b6, b17 = 'o', linestyle='--', color='b', label='Training MSE')
plt.ylabel('Error (MSE)')
plt.xlabel('Degree of Polynomial')
plt.title('Training Error vs. Polynomial Degree')
plt.legend()
plt.grid(True)
plt.subplot(2, 1, 2)
plt.plot(range(1, 3), b7, b17 = 'o', linestyle='--', color='r', label='Testing MSE')
plt.ylabel('Error (MSE)')
plt.xlabel('Degree of Polynomial')
plt.title('Testing Error vs. Polynomial Degree')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()