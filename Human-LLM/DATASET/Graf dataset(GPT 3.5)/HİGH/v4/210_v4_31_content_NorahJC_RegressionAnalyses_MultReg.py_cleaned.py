import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score
b1 = pd.read_csv('3-Products-Multiple.csv')
b2 = b1.drop(columns=['Location', 'Product_1', 'Product_2', 'Product_3'])
b3 = b1['Product_1']
b4 = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
b5 = b4.fit_transform(b2)
X_train, X_test, y_train, b6 = train_test_split(b5, b3, test_size=0.2, random_state=0)
b7 = LinearRegression()
b7.fit(X_train, y_train)
print('Coefficients:')
print(b7.coef_)
print('Variance score:', r2_score(b6, b7.predict(X_test)))
b8 = b7.predict(X_test)
print('Predictions:')
print(b8)
plt.scatter(b7.predict(X_train), b7.predict(X_train) - y_train, b9 = "green", s=10, label='Train data')
plt.scatter(b7.predict(X_test), b7.predict(X_test) - b6, b9 = "blue", s=10, label='Test data')
plt.hlines(b3 = 0, xmin=-1000, xmax=200000, linewidth=2)
plt.legend(b10 = 'upper right')
plt.title("Residual errors")
plt.xlabel('Predicted values')
plt.ylabel('Residuals')
plt.show()