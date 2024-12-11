import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
b1 = time.time()
b2 = pd.read_csv("housePriceDataset.csv")
b3 = b2["b3"]
b4 = b2["b4"]
b5 = np.array(b3)
b6 = np.array(b4)
a, b, c, b7 = np.polyfit(b5, b6, 3)
b8 = np.arange(150)
plt.scatter(b5, b6)
plt.plot(b8, a*(b8**3) + b*(b8**2) + c*b8 + b7)
plt.show()
b9 = time.time()
b10 = float(input("Please, enter square meter (m2): "))
b11 = time.time()
b12 = a*(b10**3) + b*(b10**2) + c*b10 + b7
print("House Price b13 = > $" + str(b12))
b14 = time.time()
b15 = float(input("Please, enter house b4 ($): "))
b16 = time.time()
for i in np.arange(0, 1000, 0.001):
    b17 = a*(i**3) + b*(i**2) + c*i + b7
    if(b17 < b15):
        continue
    else:
        print("Square Meter (m2) b13 = > " + str(i) + "m2")
        break
print("{} Seconds".format((time.time() - b16) + (b14 - b11) + (b9 - b1)))