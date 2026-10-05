import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
print("Data Preprocessing")
data = pd.read_csv("coEmission.csv")
features = data.iloc[:, :3].values
target = data.iloc[:, 3].values
x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=0)
print("Creating Model...")
poly_features = PolynomialFeatures(degree=4)
x_poly = poly_features.fit_transform(features)
polynomial_reg = LinearRegression()
print("Training Started...")
polynomial_reg.fit(x_poly, target)
print("Training Completed")
while True:
    print("\nEnter data for CO emission prediction:")
    year = int(input("Year (after 2005): ")) - 2005
    temperature = int(input("Temperature: "))
    fuel_type = int(input("Fuel type: "))
    input_params = [temperature, fuel_type, year]
    predicted_emission = polynomial_reg.predict(poly_features.transform([input_params]))[0]
    print("Predicted CO emission:", predicted_emission, "grams")