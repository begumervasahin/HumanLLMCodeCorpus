import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
train = pd.read_csv('winequality-red.csv')
numeric_data = train.select_dtypes(include=[np.number]).interpolate().dropna()
y = np.log(train['quality'])
X = numeric_data.drop(['quality'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
r2_score = lr_model.score(X_test, y_test)
print("R^2 score is:\n", r2_score)
predictions = lr_model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
print("RMSE is:\n", rmse)
corr_matrix = numeric_data.corr()
top_correlations = corr_matrix['quality'].sort_values(ascending=False).head(5)
print("Top 5 features correlated with quality:\n", top_correlations, '\n')
missing_values = train.isnull().sum().sort_values(ascending=False).head(25)
nulls_df = pd.DataFrame({'Null Count': missing_values})
nulls_df.index.name = 'Feature'
print("Missing values in the dataset:\n", nulls_df)