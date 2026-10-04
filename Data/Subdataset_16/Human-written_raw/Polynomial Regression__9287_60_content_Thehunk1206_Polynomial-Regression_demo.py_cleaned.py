import numpy as np
from numpy import polyfit
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as pt
import time
def fonk1():
    b1 = pd.read_csv('CleanData.csv')
    b1.drop(['Unnamed: 0'],b2 = 1, b3=True)
    b1.drop(b1.index[[0,1,5,9,73,74,75,710,711,712,713,714,715,716,717,718,719]], b3 = True)
    print(b1.info())
    print(b1.describe())
    b4 = pt.figure()
    b5 = b4.add_subplot(1,1,1)
    b6 = b1['Decimal Date'].tolist()
    b7 = b1['Carbon Dioxide (ppm)'].tolist()
    b8 = b1['Carbon Dioxide Fit (ppm)'].tolist()
    b9 = b1['Seasonally Adjusted CO2 (ppm)'].tolist()
    b10 = b1['Seasonally Adjusted CO2 Fit (ppm)'].tolist()
    b11 = b6[0:600]
    b12 = b9[0:600]
    b13 = b6[601:703]
    b14 = b9[601:703]
    a1 = 2
    b15 = time.time()
    b16 = polyfit(b11,b12,a1)
    b17 = b16.tolist()
    print(b17)
    b18 = list()
    for i in range(len(b11)):
        b19 = b16[-1]
        for d in range(a1):
            b19 += b11[i]**(a1-d) * b16[d]
        b18.append(b19)
    b5.scatter(b11,b12,b20 = 'red',label='Carbon Dioxide (ppm)')
    b5.plot(b11,b18,b20 = 'blue',label='Regression Line')
    b5.legend(b21 = 'upper left')
    a2 = 0
    for i in range(len(b18)):
        a2+= ((b12[i]- (b18[i]))**2)/len(b18)
    print("==================b28 During b22 = ======================")
    print("b23 = ", a2)
    b24 = list()
    for i in range(len(b13)):
        b25 = b16[-1]
        for deg in range(a1):
            b25 += b13[i]**(a1-deg) * b16[deg]
        b24.append(b25)
    print("========================================================")
    b26 = time.time()
    print("Approx execution time: ", b26-b15,"Seconds")
    print("==================b27 = ==========================")
    for i in range(len(b13)):
        print("Predicted value of CO2(in ppm) for Year:",b13[i],b24[i])
    a3 = 0
    for i in range(len(b24)):
        a3+= ((b14[i]- (b24[i]))**2)/len(b24)
    print("==================PRediction b28 = ======================")
    print("b23 FOR b29 = ", a3)
    pt.show()
fonk1()