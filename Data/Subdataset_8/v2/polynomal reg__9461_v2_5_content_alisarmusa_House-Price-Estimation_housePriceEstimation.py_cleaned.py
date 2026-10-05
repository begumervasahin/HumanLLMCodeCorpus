import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
start_time = time.time()
data = pd.read_csv("housePriceDataset.csv")
square_meter = data["squareMeter"]
price = data["price"]
square_meter = np.array(square_meter)
price = np.array(price)
a, b, c, d = np.polyfit(square_meter, price, 3)
z = np.arange(150)
plt.scatter(square_meter, price)
plt.plot(z, a*(z**3) + b*(z**2) + c*z + d)
plt.xlabel('Square Meter')
plt.ylabel('Price')
plt.title('House Price Prediction')
plt.show()
print("Please, enter square meter (m2): ")
m2_guess = float(input())
pause1_time = time.time()
house_price_guess = a*(m2_guess**3) + b*(m2_guess**2) + c*m2_guess + d
print("House Price Guess => $" + str(house_price_guess))
print("Please, enter house price ($): ")
house_price = float(input())
pause2_time = time.time()
low = 0
high = 1000
while low <= high:
    mid = (low + high) / 2
    guess_price = a*(mid**3) + b*(mid**2) + c*mid + d
    if guess_price < house_price:
        low = mid + 0.001
    elif guess_price > house_price:
        high = mid - 0.001
    else:
        print("Square Meter (m2) Guess => " + str(mid) + " m2")
        break
total_time = (time.time() - pause2_time) + (pause2_time - pause1_time) + (pause1_time - start_time)
print("{} Seconds".format(total_time))