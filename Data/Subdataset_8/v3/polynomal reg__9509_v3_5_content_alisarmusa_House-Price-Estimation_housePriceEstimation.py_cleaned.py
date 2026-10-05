import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
def read_data(filename):
    return pd.read_csv(filename)
def perform_polynomial_regression(square_meter, price):
    return np.polyfit(square_meter, price, 3)
def plot_data_and_curve(square_meter, price, z, a, b, c, d):
    plt.scatter(square_meter, price)
    plt.plot(z, a*(z**3) + b*(z**2) + c*z + d)
    plt.xlabel('Square Meter')
    plt.ylabel('Price')
    plt.title('House Price Prediction')
    plt.show()
def get_user_input(message):
    print(message)
    return float(input())
def calculate_house_price_guess(m2_guess, a, b, c, d):
    return a*(m2_guess**3) + b*(m2_guess**2) + c*m2_guess + d
def binary_search_for_square_meter(house_price, a, b, c, d):
    low, high = 0, 1000
    while low <= high:
        mid = (low + high) / 2
        guess_price = a*(mid**3) + b*(mid**2) + c*mid + d
        if guess_price < house_price:
            low = mid + 0.001
        elif guess_price > house_price:
            high = mid - 0.001
        else:
            return mid
    return None
def measure_time(start_time, end_time):
    return end_time - start_time
start_time = time.time()
data = read_data("housePriceDataset.csv")
square_meter = np.array(data["squareMeter"])
price = np.array(data["price"])
a, b, c, d = perform_polynomial_regression(square_meter, price)
z = np.arange(150)
plot_data_and_curve(square_meter, price, z, a, b, c, d)
m2_guess = get_user_input("Please, enter square meter (m2): ")
pause1_time = time.time()
house_price_guess = calculate_house_price_guess(m2_guess, a, b, c, d)
print("House Price Guess => $" + str(house_price_guess))
house_price = get_user_input("Please, enter house price ($): ")
pause2_time = time.time()
square_meter_guess = binary_search_for_square_meter(house_price, a, b, c, d)
if square_meter_guess is not None:
    print("Square Meter (m2) Guess => " + str(square_meter_guess) + " m2")
else:
    print("Square meter not found for the given house price.")
total_time = measure_time(start_time, time.time())
print("{} Seconds".format(total_time))