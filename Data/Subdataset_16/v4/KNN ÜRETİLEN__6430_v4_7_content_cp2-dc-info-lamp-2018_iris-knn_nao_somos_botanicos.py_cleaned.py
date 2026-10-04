
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
b1 = pd.read_table("plantinhas.txt", sep=',', header=0,
                     b2 = ["sepal-length", "sepal-width", "petal-length", "petal-width", "class"])
b3 = b1.drop("class", axis=1)
b4 = b1["class"]
X_train, X_test, y_train, b5 = train_test_split(b3, b4, test_size=0.2, random_state=42)
print(f"Training features shape: {X_train.shape}")
print(f"Testing features shape: {X_test.shape}")
print(f"Training labels shape: {y_train.shape}")
print(f"Testing labels shape: {b5.shape}")