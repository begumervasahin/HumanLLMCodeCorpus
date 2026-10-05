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
plt.show()
b7 = time.time()
b8 = float(input("Please, enter square meter m2?"))
b9 = time.time()
b10 = a*(b8**3) + b*(b8**2) + c*b8 + b5
print("House Price b11 = > $" + str(b10))
b12 = time.time()
b13 = float(input("Please, enter house price $?"))
b14 = time.time()
for i in np.arange(0, 1000, 0.001):
    b15 = a*(i**3) + b*(i**2) + c*i + b5
    if(b15 < b13):
        continue
    else:
        print("Square Meter (m2) b11 = > " + str(i) + "m2")
        break
print("{} Seconds".format((time.time() - b14) + (b12 - b9) + (b7 - b1)))