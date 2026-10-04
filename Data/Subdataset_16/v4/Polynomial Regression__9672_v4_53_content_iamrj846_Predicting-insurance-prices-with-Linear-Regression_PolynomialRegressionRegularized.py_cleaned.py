import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler, PolynomialFeatures
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
b1 = pd.read_csv('insurance.csv')
b2 = b1.iloc[:, :5].values
b3 = b1.iloc[:, 6].values
b4 = LabelEncoder()
b2[:, 1] = b4.fit_transform(b2[:, 1])
b2[:, 4] = b4.fit_transform(b2[:, 4])
b5 = OneHotEncoder(categorical_features=[1, 4])
b2 = b5.fit_transform(b2).toarray()
b2 = b2[:, [1, 3, 4, 5, 6]]
b6 = StandardScaler()
b2 = b6.fit_transform(b2)
b7 = StandardScaler()
b3 = b7.fit_transform(b3.reshape(-1, 1))
b8 = PolynomialFeatures(degree=4)
b9 = b8.fit_transform(b2)
X_train, X_test, b14, b10 = train_test_split(b9, b3, test_size=0.2, random_state=0)
b11 = Lasso(alpha=0.01, fit_intercept=False)
b11.fit(X_train, b14)
b12 = b11.predict(X_test)
b12 = b7.inverse_transform(b12)
b13 = b11.predict(X_train)
b13 = b7.inverse_transform(b13)
b14 = b7.inverse_transform(b14)
b15 = r2_score(b14, b13) * 100
b12 = b11.predict(X_test)
b12 = b7.inverse_transform(b12)
b10 = b7.inverse_transform(b10)
b16 = r2_score(b10, b12) * 100
print(f'R2 Score on Training Set: {b15:.2f}%')
print(f'R2 Score on Test Set: {b16:.2f}%')