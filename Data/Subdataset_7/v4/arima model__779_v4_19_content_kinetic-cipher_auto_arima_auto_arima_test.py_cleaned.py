import numpy as np
import matplotlib.pyplot as plt
import auto_arima_model as am
import argparse
def fonk1():
    b1 = argparse.ArgumentParser()
    b1.add_argument("-f", "--forecast", b2 = "perform forecasts and plot results", action="store_true")
    b3 = b1.parse_args()
    return b3
b3 = fonk1()
a1 = 1
a2 = 0.35
a3 = 0
a4 = 60
a5 = 0.1
a6 = 0
a7 = 1
a8 = 100
print("Analyzing Noisy Sine...")
b4 = np.arange(a3, a4, a5)
b5 = a1 * np.sin(b4)
b6 = np.random.normal(a6, a7, len(b5))
b7 = np.add(b5, a2 * b6)
b8 = am.AutoArimaModel(start_p=1, max_p=3, start_q=1, max_q=3)
b8.fit(b7)
b9 = b8.get_params()
print(b9)
if b3.forecast:
    Ypred1, b10 = b8.forecast(num_steps=a8, conf_int=True)
    b11 = np.arange(len(b7) + len(Ypred1))
print("=====================")
print("Analyzing Up-Ramp...")
b12 = np.add(b4, b7)
b8.fit(b12)
b9 = b8.get_params()
print(b9)
if b3.forecast:
    Ypred2, b13 = b8.forecast(num_steps=a8, conf_int=True)
print("=====================")
print("Analyzing Down-Ramp...")
b14 = np.add(a4 - b4, b7)
b8.fit(b14)
b9 = b8.get_params()
print(b9)
if b3.forecast:
    Ypred3, b15 = b8.forecast(num_steps=a8, conf_int=True)
print("=====================")
print("Analyzing Quadratic-Ramp...")
b16 = np.add(0.01 * np.power(b4, 2), b7)
b8.fit(b16)
b9 = b8.get_params()
print(b9)
if b3.forecast:
    Ypred4, b17 = b8.forecast(num_steps=a8, conf_int=True)
print("=====================")
print("Analyzing Cubic-Ramp...")
b18 = np.add((1 / 5000) * np.power(b4, 3), b7)
b8.fit(b18)
b9 = b8.get_params()
print(b9)
if b3.forecast:
    Ypred5, b19 = b8.forecast(num_steps=a8, conf_int=True)
print("=====================")
print("Analyzing Fourth-power Ramp...")
b20 = np.add((1 / 200000) * np.power(b4, 4), b7)
b8.fit(b20)
b9 = b8.get_params()
print(b9)
if b3.forecast:
    Ypred6, b21 = b8.forecast(num_steps=a8, conf_int=True)
print("=====================")
if b3.forecast:
    fig, b22 = plt.subplots(3, 2)
    b22[0, 0].plot(b11[:len(b7)], b7, 'b')
    b22[0, 0].plot(b11[len(b7):], Ypred1, 'r')
    b22[0, 0].fill_between(b11[len(b7):], b10[:, 0], b10[:, 1], b23 = 0.3, color='b')
    b22[0, 0].grid()
    b22[0, 0].set_title('Noisy Sine')
    b22[0, 1].plot(b11[:len(b7)], b12, 'b')
    b22[0, 1].plot(b11[len(b7):], Ypred2, 'r')
    b22[0, 1].fill_between(b11[len(b7):], b13[:, 0], b13[:, 1], b23 = 0.3, color='b')
    b22[0, 1].grid()
    b22[0, 1].set_title('Up Ramp')
    b22[1, 0].plot(b11[:len(b7)], b14, 'b')
    b22[1, 0].plot(b11[len(b7):], Ypred3, 'r')
    b22[1, 0].fill_between(b11[len(b7):], b15[:, 0], b15[:, 1], b23 = 0.3, color='b')
    b22[1, 0].grid()
    b22[1, 0].set_title('Down Ramp')
    b22[1, 1].plot(b11[:len(b7)], b16, 'b')
    b22[1, 1].plot(b11[len(b7):], Ypred4, 'r')
    b22[1, 1].fill_between(b11[len(b7):], b17[:, 0], b17[:, 1], b23 = 0.3, color='b')
    b22[1, 1].grid()
    b22[1, 1].set_title('Quadratic Ramp')
    b22[2, 0].plot(b11[:len(b7)], b18, 'b')
    b22[2, 0].plot(b11[len(b7):], Ypred5, 'r')
    b22[2, 0].fill_between(b11[len(b7):], b19[:, 0], b19[:, 1], b23 = 0.3, color='b')
    b22[2, 0].grid()
    b22[2, 0].set_title('Cubic Ramp')
    b22[2, 1].plot(b11[:len(b7)], b20, 'b')
    b22[2, 1].plot(b11[len(b7):], Ypred6, 'r')
    b22[2, 1].fill_between(b11[len(b7):], b21[:, 0], b21[:, 1], b23 = 0.3, color='b')
    b22[2, 1].grid()
    b22[2, 1].set_title('Fourth-Power Ramp')
    for ax in b22.flat:
        ax.set(b24 = 'Time Sample', ylabel='Amplitude')
    for ax in b22.flat:
        ax.label_outer()
    plt.show()