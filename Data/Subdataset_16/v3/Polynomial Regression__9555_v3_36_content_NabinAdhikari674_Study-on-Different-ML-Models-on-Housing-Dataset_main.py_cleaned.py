print("\n******** Importing to main.py ... **********")
from pre_processor import Xtrain, Xtest, Ytrain, Ytest, np
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from matplotlib import pyplot as plt
print("\n\n\tRunning main.py\n")
b1 = LinearRegression()
b2 = LinearRegression()
b3 = LinearRegression()
b4 = PolynomialFeatures(b15=2)
b5 = PolynomialFeatures(b15=3)
b6 = DecisionTreeRegressor(max_depth=3)
b7 = RandomForestRegressor(n_estimators=100)
b8 = b4.fit_transform(Xtrain)
b9 = b5.fit_transform(Xtrain)
b1.fit(Xtrain, Ytrain)
b2.fit(b8, Ytrain)
b3.fit(b9, Ytrain)
b10 = b1.predict(Xtest)
b11 = b2.predict(b4.fit_transform(Xtest))
b12 = b3.predict(b5.fit_transform(Xtest))
def fonk1(model_name, y_true, y_pred):
    b13 = mean_squared_error(y_true, y_pred)
    b14 = r2_score(y_true, y_pred)
    print(f"{model_name} - MSE: {b13:.3f}, RÂ² Score: {b14:.3f}")
fonk1("Linear Regression", Ytest, b10)
fonk1("Quadratic Regression (b15 = 2)", Ytest, b11)
fonk1("Quadratic Regression (b15 = 3)", Ytest, b12)
b6.fit(Xtrain, Ytrain)
b16 = b6.predict(Xtest)
fonk1("Decision Tree Regressor", Ytest, b16)
b7.fit(Xtrain, Ytrain)
b17 = b7.predict(Xtest)
fonk1("Random Forest Regressor", Ytest, b17)
'''
def fonk2(X, Y, b10, b11, b12):
    plt.scatter(X, Y, b18 = 'Training Points')
    plt.plot(X, b10, b18 = 'Linear Fit', linestyle='-')
    plt.plot(X, b11, b18 = 'Quadratic Fit (b15=2)')
    plt.plot(X, b12, b18 = 'Quadratic Fit (b15=3)')
    plt.legend(b19 = 'upper left')
    plt.show()
fonk2(Xtest, Ytest, b10, b11, b12)
print("Done")
'''
print("Done")