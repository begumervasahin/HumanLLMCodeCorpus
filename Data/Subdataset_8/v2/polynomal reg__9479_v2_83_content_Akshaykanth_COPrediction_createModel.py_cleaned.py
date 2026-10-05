import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
print("Step 1: Data Preprocessing")
data = pd.read_csv("coEmission.csv")
x = data.iloc[:, 0:3].values
y = data.iloc[:, 3].values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
print("Step 2: Model Creation")
poly_reg = PolynomialFeatures(degree=4)
x_poly = poly_reg.fit_transform(x_train)
pol_reg = LinearRegression()
print("Step 3: Training Started")
pol_reg.fit(x_poly, y_train)
print("Training Ended")
print("\nPredict CO Emission (Enter Year, Temp, Fuel) or type 'quit' to exit")
while True:
    user_input = input("Year: ")
    if user_input.lower() == 'quit':
        print("Exiting...")
        break
    year = int(user_input) - 2005
    temp = int(input("Temp: "))
    fuel = int(input("Fuel: "))
    params = [temp, fuel, year]
    co_emission = pol_reg.predict(poly_reg.fit_transform([params]))[0]
    print("Predicted CO emission:", co_emission, "grams")