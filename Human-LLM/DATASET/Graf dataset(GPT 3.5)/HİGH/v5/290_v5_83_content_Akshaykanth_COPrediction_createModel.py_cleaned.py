import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
print("Data Preprocessing")
b1 = pd.read_csv("coEmission.csv")
b2 = b1.iloc[:, :3].values
b3 = b1.iloc[:, 3].values
x_train, x_test, y_train, b4 = train_test_split(b2, b3, test_size=0.2, random_state=0)
print("Creating Model...")
b5 = PolynomialFeatures(degree=4)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
print("Training Started...")
b7.fit(b6, b3)
print("Training Completed")
while True:
    print("\nEnter b1 for CO emission prediction:")
    b8 = int(input("Year (after 2005): ")) - 2005
    b9 = int(input("Temperature: "))
    b10 = int(input("Fuel type: "))
    b11 = [b9, b10, b8]
    b12 = b7.predict(b5.transform([b11]))[0]
    print("Predicted CO emission:", b12, "grams")