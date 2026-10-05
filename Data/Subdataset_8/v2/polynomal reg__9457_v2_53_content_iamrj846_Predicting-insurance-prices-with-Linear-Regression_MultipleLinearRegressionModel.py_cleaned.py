
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
insurance_data = pd.read_csv('insurance.csv')
features = insurance_data.iloc[:, :-1].values
target = insurance_data.iloc[:, -1].values
label_encoder = LabelEncoder()
features[:, 1] = label_encoder.fit_transform(features[:, 1])
features[:, 4] = label_encoder.fit_transform(features[:, 4])
onehot_encoder = OneHotEncoder(categories='auto', sparse=False)
features = onehot_encoder.fit_transform(features)
features = features[:, [1, 3, 4, 5, 6]]
features = np.append(arr=np.ones((features.shape[0], 1)).astype(int), values=features, axis=1)
ols_regressor = sm.OLS(endog=target, exog=features).fit()
print(ols_regressor.summary())
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=0)
linear_regressor = LinearRegression()
linear_regressor.fit(X_train, y_train)
y_pred_train = linear_regressor.predict(X_train)
y_pred_test = linear_regressor.predict(X_test)
r2_score_train = r2_score(y_train, y_pred_train) * 100
r2_score_test = r2_score(y_test, y_pred_test) * 100
print("R-squared score on training set: {:.2f}%".format(r2_score_train))
print("R-squared score on test set: {:.2f}%".format(r2_score_test))