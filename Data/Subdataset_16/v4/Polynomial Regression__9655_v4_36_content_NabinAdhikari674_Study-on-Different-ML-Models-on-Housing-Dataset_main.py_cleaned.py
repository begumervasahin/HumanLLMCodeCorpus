import numpy as np
from sklearn.metrics import accuracy_score, r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from matplotlib import pyplot as plt
from pre_processor import Xtrain, Xtest, Ytrain, Ytest
b1 = LinearRegression()
b2 = LinearRegression()
b3 = LinearRegression()
b4 = PolynomialFeatures(degree=2)
b5 = PolynomialFeatures(degree=3)
b6 = DecisionTreeRegressor(max_depth=3)
b7 = RandomForestRegressor(n_estimators=100)
b8 = b4.fit_transform(Xtrain)
b9 = b5.fit_transform(Xtrain)
b1.fit(Xtrain, Ytrain)
b2.fit(b8, Ytrain)
b3.fit(b9, Ytrain)
b6.fit(Xtrain, Ytrain)
b7.fit(Xtrain, Ytrain)
b10 = b1.predict(Xtest)
b11 = b2.predict(b4.fit_transform(Xtest))
b12 = b3.predict(b5.fit_transform(Xtest))
b13 = b6.predict(Xtest)
b14 = b7.predict(Xtest)
print("\n********Importing to main.py ...**********\n\n\tRunning main.py\n")
print("Training b15 = > Linear : %.3f, Quadratic1 (d=2) : %.3f, Quadratic2 (d=3) : %.3f" %
      (mean_squared_error(Ytest, b10),
       mean_squared_error(Ytest, b11),
       mean_squared_error(Ytest, b12)))
print("Training R2 b16 = > Linear : %.3f, Quadratic1 (d=2) : %.3f, Quadratic2 (d=3) : %.3f" %
      (r2_score(Ytest, b10),
       r2_score(Ytest, b11),
       r2_score(Ytest, b12)))
print("Training b15 = > DTR : %.3f" % mean_squared_error(Ytest, b13))
print("Training R2 b16 = > DTR : %.3f" % r2_score(Ytest, b13))
print("Training b15 = > RFR : %.3f" % mean_squared_error(Ytest, b14))
print("Training R2 b16 = > RFR : %.3f" % r2_score(Ytest, b14))
print("Done")