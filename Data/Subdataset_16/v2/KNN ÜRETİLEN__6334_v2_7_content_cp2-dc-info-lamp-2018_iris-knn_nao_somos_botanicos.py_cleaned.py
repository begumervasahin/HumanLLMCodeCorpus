
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
b1 = "plantinhas.txt"
b2 = pd.read_csv(b1, sep=',', header=0, names=["sepal-length", "sepal-width", "petal-length", "petal-width", "class"])
b3 = b2.drop(columns=["class"])
b4 = b2["class"]
X_train, X_test, y_train, b5 = train_test_split(b3, b4, test_size=0.2, random_state=42)
print(f"Training b2 shape: {X_train.shape}")
print(f"Testing b2 shape: {X_test.shape}")
print(f"Training b4 shape: {y_train.shape}")
print(f"Testing b4 shape: {b5.shape}")