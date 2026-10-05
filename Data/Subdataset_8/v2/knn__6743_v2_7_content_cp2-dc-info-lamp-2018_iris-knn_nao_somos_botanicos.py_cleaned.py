import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
data = pd.read_table("plantinhas.txt", sep=',', header=0, names=["sepal-length", "sepal-width", "petal-length", "petal-width", "class"])
features = data.iloc[:, :-1]
target = data.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
print("Training set shapes:")
print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)
print("\nTesting set shapes:")
print("X_test shape:", X_test.shape)
print("y_test shape:", y_test.shape)