"""
Designed By: Akshaykanth D L
Date: 02-05-2019
Title : "Carbon Monoxide Prediction"
"""
import pandas as pd
from sklearn.svm import SVR
import numpy as numpy
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
print("Data Pre Processing")
b1 = pd.read_csv("coEmission.csv", )
b2 = b1.iloc[:,0:3].values
b3 = b1.iloc[:, 3].values
x_tarin, y_train, x_test, b4 = train_test_split(b2,b3, test_size=0.2, random_state=0)
print("Model Creating...!")
b5 = PolynomialFeatures(degree=4)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
print("Training Started..!")
b7.fit(b6, b3)
print("Training Ended")
while(True):
    print("
    print(" Year: ", b8 = "")
    b9 = int(input()) - 2005
    print(" Temp: ", b8 = "")
    b10 = int(input())
    print(" Fuel: ", b8 = "")
    b11 = int(input())
    b12 = [b10, b11, b9]
    print(" CO emission: ", b7.predict(b5.fit_transform([b12]))[0], "grams")