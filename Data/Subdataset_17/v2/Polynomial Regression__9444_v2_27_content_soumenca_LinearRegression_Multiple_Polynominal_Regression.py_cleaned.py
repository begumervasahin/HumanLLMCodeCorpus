import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
data = pd.read_csv('/home/soumen/Desktop/TML_HW3_AT/winequalityRed.csv', header=None)
print(f"Shape of the training data is {data.shape}")
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
train_mse_list = []
test_mse_list = []
for degree in range(1, 3):
    poly = PolynomialFeatures(degree=degree)
    x_train_poly = poly.fit_transform(x_train)
    x_test_poly = poly.fit_transform(x_test)
    model = LinearRegression()
    model.fit(x_train_poly, y_train)
    y_train_pred = model.predict(x_train_poly)
    y_test_pred = model.predict(x_test_poly)
    train_mse = mean_squared_error(y_train, y_train_pred)
    test_mse = mean_squared_error(y_test, y_test_pred)
    train_mse_list.append(train_mse)
    test_mse_list.append(test_mse)
    print(f"The degree of the polynomial is {degree}")
    print(f"Training MSE: {train_mse}")
    print(f"Testing MSE: {test_mse}")
    print('.............................................')
plt.figure(figsize=(10, 6))
plt.subplot(211)
plt.plot(range(1, 3), train_mse_list, marker='o', linestyle='--', color='b')
plt.ylabel('Training Error (MSE)')
plt.xlabel('Degree of the Polynomial')
plt.grid(True)
plt.subplot(212)
plt.plot(range(1, 3), test_mse_list, marker='o', linestyle='--', color='r')
plt.ylabel('Testing Error (MSE)')
plt.xlabel('Degree of the Polynomial')
plt.grid(True)
plt.tight_layout()
plt.show()