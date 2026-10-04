
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
b1 = pd.read_table("plantinhas.txt", sep=',', header=0, names=["sepal-lenght", "sepal-width", "petal-lenght", "petal-width", "class"])
X_train, X_test, y_train, b2 = train_test_split(X, y, test_size=0.2, random_state=42)