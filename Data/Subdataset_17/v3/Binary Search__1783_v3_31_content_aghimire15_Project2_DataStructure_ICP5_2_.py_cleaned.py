import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
data = pd.read_csv('winequality-red.csv')
numeric_data = data.select_dtypes(include=[np.number]).interpolate().dropna()
y = np.log(data['quality'])
X = numeric_data.drop(columns=['quality'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
r2_score = lr_model.score(X_test, y_test)
print(f"R^2 score: {r2_score:.4f}")
y_pred = lr_model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
correlation_matrix = numeric_data.corr()
top_correlated_features = correlation_matrix['quality'].sort_values(ascending=False).head(5)
print("Top 5 features correlated with quality:\n", top_correlated_features)
null_counts = data.isnull().sum().sort_values(ascending=False)
if null_counts.sum() > 0:
    print("\nNull value counts by feature:\n", null_counts[null_counts > 0])
else:
    print("\nNo missing values found in the dataset.")