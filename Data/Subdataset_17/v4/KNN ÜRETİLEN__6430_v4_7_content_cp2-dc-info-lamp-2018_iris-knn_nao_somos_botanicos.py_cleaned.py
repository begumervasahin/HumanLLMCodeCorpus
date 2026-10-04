
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
data = pd.read_table("plantinhas.txt", sep=',', header=0,
                     names=["sepal-length", "sepal-width", "petal-length", "petal-width", "class"])
X = data.drop("class", axis=1)
y = data["class"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Training features shape: {X_train.shape}")
print(f"Testing features shape: {X_test.shape}")
print(f"Training labels shape: {y_train.shape}")
print(f"Testing labels shape: {y_test.shape}")