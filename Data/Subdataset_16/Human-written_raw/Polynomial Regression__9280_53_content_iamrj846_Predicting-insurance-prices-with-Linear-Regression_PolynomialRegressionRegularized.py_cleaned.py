import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
b1 = pd.read_csv('insurance.csv')
b2 = b1.iloc[:, :5].values
b3 = b1.iloc[:, 6].values
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
b4 = LabelEncoder()
b2[:, 1] = b4.fit_transform(b2[:, 1])
b2[:, 4] = b4.fit_transform(b2[:, 4])
b5 = OneHotEncoder(categorical_features = [1, 4])
b2 = b5.fit_transform(b2).toarray()
b2 = b2[:, [1, 3, 4, 5, 6]]
from sklearn.preprocessing import StandardScaler
b6 = StandardScaler()
b2 = b6.fit_transform(b2)
b7 = StandardScaler()
b3 = b7.fit_transform(b3.reshape(-1, 1))
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Lasso
b8 = PolynomialFeatures(degree = 4)
b9 = b8.fit_transform(b2)
from sklearn.model_selection import train_test_split
X_train, X_test, b14, b10 = train_test_split(b9, b3, test_size = 0.2, random_state = 0)
b11 = Lasso(alpha=0.01, fit_intercept=False)
b11.fit(X_train, b14)
b12 = b11.predict(X_test)
b12 = b7.inverse_transform(b12)
b13 = b11.predict(X_train)
b13 = b7.inverse_transform(b13)
b14 = b7.inverse_transform(b14)
from sklearn.metrics import r2_score
b15 = r2_score(b14, b13) * 100
b12 = b11.predict(X_test)
b12 = b7.inverse_transform(b12)
b10 = b7.inverse_transform(b10)
from sklearn.metrics import r2_score
b16 = r2_score(b10, b12) * 100