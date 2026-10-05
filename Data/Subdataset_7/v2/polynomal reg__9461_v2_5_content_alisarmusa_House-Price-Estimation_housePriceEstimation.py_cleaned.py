import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
b1 = time.time()
b2 = pd.read_csv("housePriceDataset.csv")
b3 = b2["squareMeter"]
b4 = b2["b4"]
b3 = np.array(b3)
b4 = np.array(b4)
a, b, c, b5 = np.polyfit(b3, b4, 3)
b6 = np.arange(150)
plt.scatter(b3, b4)
plt.plot(b6, a*(b6**3) + b*(b6**2) + c*b6 + b5)
plt.xlabel('Square Meter')
plt.ylabel('Price')
plt.title('House Price Prediction')
plt.show()
print("Please, enter square meter (m2): ")
b7 = float(input())
b8 = time.time()
b9 = a*(b7**3) + b*(b7**2) + c*b7 + b5
print("House Price b10 = > $" + str(b9))
print("Please, enter house b4 ($): ")
b11 = float(input())
b12 = time.time()
a1 = 0
a2 = 1000
while a1 <= a2:
    b13 = (a1 + a2) / 2
    b14 = a*(b13**3) + b*(b13**2) + c*b13 + b5
    if b14 < b11:
        a1 = b13 + 0.001
    elif b14 > b11:
        a2 = b13 - 0.001
    else:
        print("Square Meter (m2) b10 = > " + str(b13) + " m2")
        break
b15 = (time.time() - b12) + (b12 - b8) + (b8 - b1)
print("{} Seconds".format(b15))