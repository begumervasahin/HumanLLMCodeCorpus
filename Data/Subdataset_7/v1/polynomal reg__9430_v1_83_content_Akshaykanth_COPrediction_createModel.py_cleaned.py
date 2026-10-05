import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
print("Data Pre Processing")
b1 = pd.read_csv("coEmission.csv")
b2 = b1.iloc[:, 0:3].values
b3 = b1.iloc[:, 3].values
x_train, x_test, y_train, b4 = train_test_split(b2, b3, test_size=0.2, random_state=0)
print("Model Creating...!")
b5 = PolynomialFeatures(degree=4)
b6 = b5.fit_transform(x_train)
b7 = LinearRegression()
print("Training Started..!")
b7.fit(b6, y_train)
print("Training Ended")
while True:
    print("\nEnter Data (Year, Temp, Fuel) or 'quit' to exit:")
    b8 = input("Year: ")
    if b8.lower() == 'quit':
        print("Exiting...")
        break
    b9 = int(b8) - 2005
    b10 = int(input("Temp: "))
    b11 = int(input("Fuel: "))
    b12 = [b10, b11, b9]
    b13 = b7.predict(b5.fit_transform([b12]))[0]
    print("CO emission:", b13, "grams")