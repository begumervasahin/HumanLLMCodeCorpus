print("\n******** Importing to main.py ... **********")
from pre_processor import Xtrain, Xtest, Ytrain, Ytest, np
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from matplotlib import pyplot as plt
print("\n\n\tRunning main.py\n")
linear_regressor = LinearRegression()
poly_regressor_deg2 = LinearRegression()
poly_regressor_deg3 = LinearRegression()
quadratic_features_deg2 = PolynomialFeatures(degree=2)
quadratic_features_deg3 = PolynomialFeatures(degree=3)
decision_tree_regressor = DecisionTreeRegressor(max_depth=3)
random_forest_regressor = RandomForestRegressor(n_estimators=100)
X_quad_deg2 = quadratic_features_deg2.fit_transform(Xtrain)
X_quad_deg3 = quadratic_features_deg3.fit_transform(Xtrain)
linear_regressor.fit(Xtrain, Ytrain)
poly_regressor_deg2.fit(X_quad_deg2, Ytrain)
poly_regressor_deg3.fit(X_quad_deg3, Ytrain)
y_pred_linear = linear_regressor.predict(Xtest)
y_pred_quad_deg2 = poly_regressor_deg2.predict(quadratic_features_deg2.fit_transform(Xtest))
y_pred_quad_deg3 = poly_regressor_deg3.predict(quadratic_features_deg3.fit_transform(Xtest))
print("Training MSE => Linear: %.3f, \n\tQuadratic (degree=2): %.3f, \n\tQuadratic (degree=3): %.3f" %
      (mean_squared_error(Ytest, y_pred_linear),
       mean_squared_error(Ytest, y_pred_quad_deg2),
       mean_squared_error(Ytest, y_pred_quad_deg3)))
print("Training R2 Score => Linear: %.3f, \n\tQuadratic (degree=2): %.3f, \n\tQuadratic (degree=3): %.3f" %
      (r2_score(Ytest, y_pred_linear),
       r2_score(Ytest, y_pred_quad_deg2),
       r2_score(Ytest, y_pred_quad_deg3)))
decision_tree_regressor.fit(Xtrain, Ytrain)
y_pred_dtr = decision_tree_regressor.predict(Xtest)
print("Training MSE => Decision Tree Regressor: %.3f" % mean_squared_error(Ytest, y_pred_dtr))
print("Training R2 Score => Decision Tree Regressor: %.3f" % r2_score(Ytest, y_pred_dtr))
random_forest_regressor.fit(Xtrain, Ytrain)
y_pred_rfr = random_forest_regressor.predict(Xtest)
print("Training MSE => Random Forest Regressor: %.3f" % mean_squared_error(Ytest, y_pred_rfr))
print("Training R2 Score => Random Forest Regressor: %.3f" % r2_score(Ytest, y_pred_rfr))
'''
y_fit_linear = linear_regressor.predict(Xtest)
y_fit_quad_deg2 = poly_regressor_deg2.predict(quadratic_features_deg2.fit_transform(Xtest))
y_fit_quad_deg3 = poly_regressor_deg3.predict(quadratic_features_deg3.fit_transform(Xtest))
plt.scatter(Xtest, Ytest, label='Training Points')
plt.plot(Xtest, y_fit_linear, label='Linear Fit', linestyle='-')
plt.plot(Xtest, y_fit_quad_deg2, label='Quadratic Fit (degree=2)')
plt.plot(Xtest, y_fit_quad_deg3, label='Quadratic Fit (degree=3)')
plt.legend(loc='upper left')
plt.show()
print("Done")
'''
print("Done")