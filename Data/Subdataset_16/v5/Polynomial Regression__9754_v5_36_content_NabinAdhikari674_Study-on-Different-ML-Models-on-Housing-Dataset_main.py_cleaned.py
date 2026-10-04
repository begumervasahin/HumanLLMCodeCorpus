import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from matplotlib import pyplot as plt
from pre_processor import Xtrain, Xtest, Ytrain, Ytest
def fonk1(model_name, y_true, y_pred):
    b1 = mean_squared_error(y_true, y_pred)
    b2 = r2_score(y_true, y_pred)
    print(f"Training b3 = > {model_name} : {b1:.3f}")
    print(f"Training R2 b4 = > {model_name} : {b2:.3f}")
b5 = LinearRegression()
b6 = LinearRegression()
b7 = LinearRegression()
b8 = PolynomialFeatures(degree=2)
b9 = PolynomialFeatures(degree=3)
b10 = DecisionTreeRegressor(max_depth=3)
b11 = RandomForestRegressor(n_estimators=100)
b12 = b8.fit_transform(Xtrain)
b13 = b9.fit_transform(Xtrain)
b5.fit(Xtrain, Ytrain)
b6.fit(b12, Ytrain)
b7.fit(b13, Ytrain)
b10.fit(Xtrain, Ytrain)
b11.fit(Xtrain, Ytrain)
b14 = b5.predict(Xtest)
b15 = b6.predict(b8.transform(Xtest))
b16 = b7.predict(b9.transform(Xtest))
b17 = b10.predict(Xtest)
b18 = b11.predict(Xtest)
print("\n******** Importing to main.py ... **********\n\n\tRunning main.py\n")
fonk1("Linear", Ytest, b14)
fonk1("Quadratic1 (b19 = 2)", Ytest, b15)
fonk1("Quadratic2 (b19 = 3)", Ytest, b16)
fonk1("DTR", Ytest, b17)
fonk1("RFR", Ytest, b18)
print("Done")