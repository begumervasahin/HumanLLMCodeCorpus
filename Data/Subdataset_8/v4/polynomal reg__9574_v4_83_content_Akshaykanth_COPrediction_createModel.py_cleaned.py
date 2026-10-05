
import pandas as pd
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
print("Data Pre Processing")
data = pd.read_csv("coEmission.csv")
x = data.iloc[:, 0:3].values
y = data.iloc[:, 3].values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
print("Model Creating...!")
poly_reg = PolynomialFeatures(degree=4)
x_poly = poly_reg.fit_transform(x)
pol_reg = LinearRegression()
print("Training Started..!")
pol_reg.fit(x_poly, y)
print("Training Ended")
while True:
    print("\nEnter data for CO emission prediction:")
    year = int(input("Year (after 2005): ")) - 2005
    temp = int(input("Temperature: "))
    fuel = int(input("Fuel type: "))
    params = [temp, fuel, year]
    predicted_emission = pol_reg.predict(poly_reg.fit_transform([params]))[0]
    print("Predicted CO emission:", predicted_emission, "grams")