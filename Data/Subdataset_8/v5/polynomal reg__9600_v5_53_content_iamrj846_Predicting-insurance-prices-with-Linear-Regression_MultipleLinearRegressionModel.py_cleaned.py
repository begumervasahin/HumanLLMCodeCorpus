
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm
insurance_data = pd.read_csv('insurance.csv')
features = insurance_data.iloc[:, :5].values
target = insurance_data.iloc[:, 6].values
label_encoder = LabelEncoder()
features[:, 1] = label_encoder.fit_transform(features[:, 1])
features[:, 4] = label_encoder.fit_transform(features[:, 4])
onehot_encoder = OneHotEncoder(categories='auto', drop='first')
encoded_features = onehot_encoder.fit_transform(features).toarray()
selected_features = encoded_features[:, [1, 3, 4, 5, 6]]
selected_features_with_intercept = np.append(arr=np.ones((len(insurance_data), 1)).astype(int), values=selected_features, axis=1)
X_opt = selected_features_with_intercept[:, [0, 2, 3, 4]]
regressor_OLS = sm.OLS(endog=target, exog=X_opt).fit()
print(regressor_OLS.summary())
X_train, X_test, y_train, y_test = train_test_split(X_opt, target, test_size=0.2, random_state=0)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred_train = regressor.predict(X_train)
r2_score_train = r2_score(y_train, y_pred_train) * 100
y_pred_test = regressor.predict(X_test)
r2_score_test = r2_score(y_test, y_pred_test) * 100