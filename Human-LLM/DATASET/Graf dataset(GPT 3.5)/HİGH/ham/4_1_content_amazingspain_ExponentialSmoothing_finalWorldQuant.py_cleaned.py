
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def fonk1():
    b1 = np.asarray(b9).reshape(-1,1)
    b2 = np.asarray(b5).reshape(-1,1)
    from sklearn.linear_model import LinearRegression
    b3 = LinearRegression(fit_intercept=True)
    b3.fit(b1, b2)
    plt.scatter(b1, b2)
    plt.show()
def fonk2(data,b4 = 0.25):
    global b5
    b5 = []
    b5.append(data[0])
    for i in range(len(data)):
        if i>0:
            b6 = b4*data[i] + (1-b4)*b5[i-1]
            b5.append(b6)
    return b5
def fonk3():
    b7 = pd.read_csv("/Users/vothiquynhyen/Documents/AMZNdata.csv")
    b7.describe()
    type(b7)
    b7 = b7.iloc[0:,1:]
    b7
    plt.plot(b7)
    b8 = b7.values
    b8
    type(b8)
    global b9
    b9 = b8[0].tolist()
    b9
    b9[1]
    b8
    plt.ion()
    plt.plot(b9)
    plt.show()
    b10 = "no"
    while b10 != "yes":
        b4 = input("enter your b4 for calculation:")
        fonk2(b9,b4)
        plt.ion()
        plt.clf()
        plt.plot(  b5, b11 = 'red', linewidth=4)
        plt.plot( b9, b11 = 'olive', linewidth=2)
        plt.show()
        b10 = raw_input("are you happy with the result?(yes/no)")
    b12 = b4*b9[7] + (1-b4)*b5[7]
    print "prediction for next month is ",b12
    fonk1()
    print "ggggg"
if b13 = = "__main__": fonk3()