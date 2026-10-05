import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
def fonk1(b17):
    print("Step 1: Data Preprocessing")
    b1 = pd.read_csv(b17)
    return b1
def fonk2(b1, b2 = 0.2, random_state=0):
    b3 = b1.iloc[:, 0:3].values
    b4 = b1.iloc[:, 3].values
    x_train, x_test, y_train, b5 = train_test_split(b3, b4, b2=b2, random_state=random_state)
    return x_train, x_test, y_train, b5
def fonk3(x_train, y_train, b6 = 4):
    print("Step 2: Model Creation")
    b7 = PolynomialFeatures(b6=b6)
    b8 = b7.fit_transform(x_train)
    b9 = LinearRegression()
    b9.fit(b8, y_train)
    print("Training Ended")
    return b7, b9
def fonk4(b7, b9):
    print("\nPredict CO Emission (Enter Year, Temp, Fuel) or type 'quit' to exit")
    while True:
        b10 = input("Year: ")
        if b10.lower() == 'quit':
            print("Exiting...")
            break
        b11 = int(b10) - 2005
        b12 = int(input("Temp: "))
        b13 = int(input("Fuel: "))
        b14 = [b12, b13, b11]
        b15 = b9.predict(b7.fit_transform([b14]))[0]
        print("Predicted CO emission:", b15, "grams")
if b16 = = "__main__":
    b17 = "coEmission.csv"
    b1 = fonk1(b17)
    x_train, x_test, y_train, b5 = fonk2(b1)
    b7, b9 = fonk3(x_train, y_train)
    fonk4(b7, b9)