print("\n********Importing to main.py ...**********")
from pre_processor import Xtrain,Xtest,Ytrain,Ytest,np
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from matplotlib import pyplot as plt
print("\n\n\tRunning main.py\n")
b1 = LinearRegression()
b2 = LinearRegression()
b3 = LinearRegression()
b4 = PolynomialFeatures(degree=2)
b5 = PolynomialFeatures(degree=3)
b6 = DecisionTreeRegressor(max_depth=3)
b7 = RandomForestRegressor(n_estimators=100)
b8 = b4.fit_transform(Xtrain)
b9 = b5.fit_transform(Xtrain)
b1.fit(Xtrain,Ytrain)
b2.fit(b8,Ytrain)
b3.fit(b9,Ytrain)
b10 = b1.predict(Xtest)
b11 = b2.predict(b4.fit_transform(Xtest))
b12 = b3.predict(b5.fit_transform(Xtest))
print("Training b13 = > Linear : %.3f, \n\tQuadratic1(d=2) : %.3f, \n\tQuadratic2(d=3) : %.3f"%(mean_squared_error(Ytest,b10),
                                                                                        mean_squared_error(Ytest,b11),
                                                                                        mean_squared_error(Ytest,b12)))
print("Training R2 b14 = > Linear : %.3f, \n\tQuadratic(d=2) : %.3f, \n\tQuadratic2(d=3) : %.3f"%(r2_score(Ytest,b10),
                                                                                      r2_score(Ytest,b11),
                                                                                      r2_score(Ytest,b12)))
b6.fit(Xtrain,Ytrain)
b15 = b6.predict(Xtest)
print("Training b13 = > DTR : %.3f"%(mean_squared_error(Ytest,b15)))
print("Training R2 b14 = > DTR : %.3f"%(r2_score(Ytest,b15)))
b7.fit(Xtrain,Ytrain)
b16 = b7.predict(Xtest)
print("Training b13 = > RFR : %.3f"%(mean_squared_error(Ytest,b16)))
print("Training R2 b14 = > RFR : %.3f"%(r2_score(Ytest,b16)))
'''
b17 = b1.predict(x_test)
b18 = b2.predict(b4.fit_transform(x_test))
b19 = b3.predict(b5.fit_transform(x_test))
plt.scatter(x_test,y_test,b20 = 'Training Points')
plt.plot(x_test,b17,b20 = 'Linear Fit',linestyle='-')
plt.plot(x_test,b18,b20 = 'Quadratic Fit1(d=2)')
plt.plot(x_test,b19,b20 = 'Quadratic Fit2(d=3)')
plt.legend(b21 = 'upper left')
plt.show()
print("Done")