import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
b1 = time.time()
b2 = pd.read_csv("housePriceDataset.csv")
b3 = b2["squareMeter"]
b4 = b2["price"]
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
b7 = time.time()
b8 = float(input("Please, enter square meter (m2): "))
b9 = time.time()
b10 = a*(b8**3) + b*(b8**2) + c*b8 + b5
print("House Price b11 = > $" + str(b10))
b12 = time.time()
b13 = float(input("Please, enter house price ($): "))
b14 = time.time()
a1 = 0
a2 = 1000
while a1 <= a2:
    b15 = (a1 + a2) / 2
    b16 = a*(b15**3) + b*(b15**2) + c*b15 + b5
    if b16 < b13:
        a1 = b15 + 0.001
    elif b16 > b13:
        a2 = b15 - 0.001
    else:
        print("Square Meter (m2) b11 = > " + str(b15) + " m2")
        break
print("{} Seconds".format((time.time() - b14) + (b12 - b9) + (b7 - b1)))