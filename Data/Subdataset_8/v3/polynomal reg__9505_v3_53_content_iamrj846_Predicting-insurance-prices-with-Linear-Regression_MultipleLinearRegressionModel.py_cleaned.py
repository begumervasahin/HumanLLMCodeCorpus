import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
insurance_data = pd.read_csv('insurance.csv')
X = insurance_data.iloc[:, :-1]
y = insurance_data.iloc[:, -1]
label_encoder = LabelEncoder()
X['sex'] = label_encoder.fit_transform(X['sex'])
X['region'] = label_encoder.fit_transform(X['region'])
onehot_encoder = OneHotEncoder(categories='auto', sparse=False)
X_encoded = onehot_encoder.fit_transform(X)
X_encoded = X_encoded[:, [1, 3, 4, 5, 6]]
X_encoded = np.append(arr=np.ones((X_encoded.shape[0], 1)).astype(int), values=X_encoded, axis=1)
ols_model = sm.OLS(endog=y, exog=X_encoded).fit()
print(ols_model.summary())
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=0)
linear_regressor = LinearRegression()
linear_regressor.fit(X_train, y_train)
y_pred_train = linear_regressor.predict(X_train)
y_pred_test = linear_regressor.predict(X_test)
r2_score_train = r2_score(y_train, y_pred_train) * 100
r2_score_test = r2_score(y_test, y_pred_test) * 100
print("R-squared score on training set: {:.2f}%".format(r2_score_train))
print("R-squared score on test set: {:.2f}%".format(r2_score_test))