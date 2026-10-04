import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from matplotlib import pyplot as plt
from pre_processor import Xtrain, Xtest, Ytrain, Ytest
def print_metrics(model_name, y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    print(f"Training MSE => {model_name} : {mse:.3f}")
    print(f"Training R2 score => {model_name} : {r2:.3f}")
lr = LinearRegression()
pr1 = LinearRegression()
pr2 = LinearRegression()
quadratic1 = PolynomialFeatures(degree=2)
quadratic2 = PolynomialFeatures(degree=3)
dtr = DecisionTreeRegressor(max_depth=3)
rfr = RandomForestRegressor(n_estimators=100)
Xquad1 = quadratic1.fit_transform(Xtrain)
Xquad2 = quadratic2.fit_transform(Xtrain)
lr.fit(Xtrain, Ytrain)
pr1.fit(Xquad1, Ytrain)
pr2.fit(Xquad2, Ytrain)
dtr.fit(Xtrain, Ytrain)
rfr.fit(Xtrain, Ytrain)
y_lin_pred = lr.predict(Xtest)
y_quad1_pred = pr1.predict(quadratic1.transform(Xtest))
y_quad2_pred = pr2.predict(quadratic2.transform(Xtest))
dtr_pred = dtr.predict(Xtest)
rfr_pred = rfr.predict(Xtest)
print("\n******** Importing to main.py ... **********\n\n\tRunning main.py\n")
print_metrics("Linear", Ytest, y_lin_pred)
print_metrics("Quadratic1 (d=2)", Ytest, y_quad1_pred)
print_metrics("Quadratic2 (d=3)", Ytest, y_quad2_pred)
print_metrics("DTR", Ytest, dtr_pred)
print_metrics("RFR", Ytest, rfr_pred)
print("Done")