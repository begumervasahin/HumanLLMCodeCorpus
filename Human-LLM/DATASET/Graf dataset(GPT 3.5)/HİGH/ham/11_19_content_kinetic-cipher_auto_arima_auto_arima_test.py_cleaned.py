
import numpy as np
import matplotlib.pyplot as plt
import auto_arima_model as am
import argparse
def fonk1():
    b1 = argparse.ArgumentParser()
    b1.add_argument("-f", "--forecast",
                        b2 = "perform forecasts and plot results",
                        b3 = "store_true")
    b4 = b1.parse_args()
    return b4
b4 = fonk1()
a1 = 1
a2 = 0.35
a3 = 0
a4 = 60
a5 = 0.1
a6 = 0
a7 = 1
a8 = 100
print("Analyzing Noisy Sine...")
b5 = np.arange(a3, a4, a5);
b6 = a1*np.sin(b5)
b7 = np.random.normal(a6,a7,len(b6))
b8 = np.add(b6,a2*b7)
b9 = am.AutoArimaModel(start_p=1,max_p=3,start_q=1,max_q=3)
b9.fit(b8)
b10 = b9.get_params()
print(b10)
if b4.forecast:
   Ypred1,b11 = b9.forecast(num_steps=a8,conf_int=True)
   b12 = np.arange(len(b8)+len(Ypred1))
print("=====================")
print("Analyzing Up-Ramp...")
b13 = np.add(b5,b8)
b9.fit(b13)
b10 = b9.get_params()
print(b10)
if b4.forecast:
   Ypred2,b14 = b9.forecast(num_steps=a8,conf_int=True)
print("=====================")
print("Analyzing Down-Ramp...")
b15 = np.add(a4-b5,b8)
b9.fit(b15)
b10 = b9.get_params()
print(b10)
if b4.forecast:
   Ypred3,b16 = b9.forecast(num_steps=a8,conf_int=True)
print("=====================")
print("Analyzing Quadratic-Ramp...")
b17 = np.add(0.01*np.power(b5,2),b8)
b9.fit(b17)
b10 = b9.get_params()
print(b10)
if b4.forecast:
   Ypred4,b18 = b9.forecast(num_steps=a8,conf_int=True)
print("=====================")
print("Analyzing Cubic-Ramp...")
b19 = np.add((1/5000)*np.power(b5,3),b8)
b9.fit(b19)
b10 = b9.get_params()
print(b10)
if b4.forecast:
   Ypred5,b20 = b9.forecast(num_steps=a8,conf_int=True)
print("=====================")
print("Analyzing Fourth-power Ramp...")
b21 = np.add( (1/200000)*np.power(b5,4),b8)
b9.fit(b21)
b10 = b9.get_params()
print(b10)
if b4.forecast:
   Ypred6,b22 = b9.forecast(num_steps=a8,conf_int=True)
print("=====================")
if b4.forecast:
    fig, b23 = plt.subplots(3, 2)
    b23[0,0].plot( b12[:len(b8)], b8,'b')
    b23[0,0].plot( b12[len(b8):], Ypred1,'r')
    b23[0,0].fill_between( b12[len(b8):],
                           b11[:, 0], b11[:, 1],
                           b24 = 0.3, color='b')
    b23[0,0].grid()
    b23[0,0].set_title('Noisy Sine')
    b23[0,1].plot( b12[:len(b8)], b13,'b')
    b23[0,1].plot( b12[len(b8):], Ypred2,'r')
    b23[0,1].fill_between( b12[len(b8):],
                           b14[:, 0], b14[:, 1],
                           b24 = 0.3, color='b')
    b23[0,1].grid()
    b23[0,1].set_title('Up Ramp')
    b23[1,0].plot( b12[:len(b8)], b15,'b')
    b23[1,0].plot( b12[len(b8):], Ypred3,'r')
    b23[1,0].fill_between( b12[len(b8):],
                           b16[:, 0], b16[:, 1],
                           b24 = 0.3, color='b')
    b23[1,0].grid()
    b23[1,0].set_title('Down Ramp')
    b23[1,1].plot( b12[:len(b8)], b17,'b')
    b23[1,1].plot( b12[len(b8):], Ypred4,'r')
    b23[1,1].fill_between( b12[len(b8):],
                           b18[:, 0], b18[:, 1],
                           b24 = 0.3, color='b')
    b23[1,1].grid()
    b23[1,1].set_title('Quadratic Ramp')
    b23[2,0].plot( b12[:len(b8)], b19,'b')
    b23[2,0].plot( b12[len(b8):], Ypred5,'r')
    b23[2,0].fill_between( b12[len(b8):],
                           b20[:, 0], b20[:, 1],
                           b24 = 0.3, color='b')
    b23[2,0].grid()
    b23[2,0].set_title('Cubic Ramp')
    b23[2,1].plot( b12[:len(b8)], b21,'b')
    b23[2,1].plot( b12[len(b8):], Ypred6,'r')
    b23[2,1].fill_between( b12[len(b8):],
                           b22[:, 0], b22[:, 1],
                           b24 = 0.3, color='b')
    b23[2,1].grid()
    b23[2,1].set_title('Fourth-Power Ramp')
    for ax in b23.flat:
        ax.set(b25 = ' b5 sample', ylabel='amplitude')
    for ax in b23.flat:
        ax.label_outer()
    plt.show()