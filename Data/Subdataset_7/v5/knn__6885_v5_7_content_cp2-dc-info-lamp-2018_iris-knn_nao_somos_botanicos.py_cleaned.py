
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
b1 = pd.read_table("plantinhas.txt", sep=',', header=0, names=["sepal-length", "sepal-width", "petal-length", "petal-width", "class"])
b2 = b1.drop(columns=['class'])
b3 = b1['class']
X_train, X_test, y_train, b4 = train_test_split(b2, b3, test_size=0.2, random_state=42)