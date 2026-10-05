import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
b1 = pd.read_table("plantinhas.txt", sep=',', header=0, names=["sepal-length", "sepal-width", "petal-length", "petal-width", "class"])
b2 = b1.iloc[:, :-1]
b3 = b1.iloc[:, -1]
X_train, X_test, y_train, b4 = train_test_split(b2, b3, test_size=0.2, random_state=42)
print("Training set shapes:")
print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)
print("\nTesting set shapes:")
print("X_test shape:", X_test.shape)
print("b4 shape:", b4.shape)