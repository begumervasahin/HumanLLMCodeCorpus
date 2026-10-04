import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
b1 = pd.read_csv('winequality-red.csv')
b2 = b1.select_dtypes(include=[np.number]).interpolate().dropna()
b3 = np.log(b1['quality'])
b4 = b2.drop(['quality'], axis=1)
X_train, X_test, y_train, b5 = train_test_split(b4, b3, test_size=0.33, random_state=42)
b6 = LinearRegression()
b6.fit(X_train, y_train)
b7 = b6.score(X_test, b5)
print("R^2 score is:\n", b7)
b8 = b6.predict(X_test)
b9 = np.sqrt(mean_squared_error(b5, b8))
print("RMSE is:\n", b9)
b10 = b2.corr()
b11 = b10['quality'].sort_values(ascending=False).head(5)
print("Top 5 features correlated with quality:\n", b11, '\n')
b12 = b1.isnull().sum().sort_values(ascending=False).head(25)
b13 = pd.DataFrame({'Null Count': b12})
b13.index.b14 = 'Feature'
print("Missing values in the dataset:\n", b13)