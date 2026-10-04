
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
filename = "plantinhas.txt"
data = pd.read_csv(filename, sep=',', header=0, names=["sepal-length", "sepal-width", "petal-length", "petal-width", "class"])
features = data.drop(columns=["class"])
labels = data["class"]
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
print(f"Training data shape: {X_train.shape}")
print(f"Testing data shape: {X_test.shape}")
print(f"Training labels shape: {y_train.shape}")
print(f"Testing labels shape: {y_test.shape}")