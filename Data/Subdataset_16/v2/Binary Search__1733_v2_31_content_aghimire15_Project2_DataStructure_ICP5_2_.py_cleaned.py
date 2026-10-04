import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
b1 = pd.read_csv('winequality-red.csv')
b2 = b1.select_dtypes(include=[np.number]).interpolate().dropna()
b3 = np.log(b1['quality'])
b4 = b2.drop(columns=['quality'])
X_train, X_test, y_train, b5 = train_test_split(b4, b3, test_size=0.33, random_state=42)
b6 = LinearRegression()
b6.fit(X_train, y_train)
b7 = b6.score(X_test, b5)
print(f"R^2 score: {b7:.4f}")
b8 = b6.predict(X_test)
b9 = np.sqrt(mean_squared_error(b5, b8))
print(f"Root Mean Squared Error (RMSE): {b9:.4f}")
b10 = b2.corr()
print("Top 5 features correlated with quality:\n", b10['quality'].sort_values(b11 = False).head(5))
b12 = b1.isnull().sum().sort_values(b11=False)
print("\nNull value counts by feature:\n", b12[b12 > 0])