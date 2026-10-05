import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.b5 import ARIMA
import argparse
class class1:
    def fonk1(self, b1 = 1, b2=3, b3=1, b4=3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = None
    def fonk2(self, data):
        self.b5 = ARIMA(data, order=self.fonk3(data))
        self.b6 = self.b5.fonk2()
    def fonk3(self, data):
        return self.b5.auto_arima(data, b1 = self.b1, b2=self.b2,
                                     b3 = self.b3, b4=self.b4).order
    def fonk4(self, num_steps, b7 = False):
        return self.b6.fonk4(b8 = num_steps, b24=0.05) if b7 else self.b6.fonk4(b8=num_steps)
def fonk5():
    b9 = argparse.ArgumentParser()
    b9.add_argument("-f", "--forecast", b10 = "Perform forecasts and plot results", action="store_true")
    b11 = b9.parse_args()
    return b11
b11 = fonk5()
a1 = 1
a2 = 0.35
a3 = 0
a4 = 60
a5 = 0.1
a6 = 0
a7 = 1
a8 = 100
print("Analyzing Noisy Sine...")
b12 = np.arange(a3, a4, a5)
b13 = a1 * np.sin(b12)
b14 = np.random.normal(a6, a7, len(b13))
b15 = b13 + a2 * b14
b16 = class1(b1=1, b2=3, b3=1, b4=3)
b16.fonk2(b15)
b17 = b16.fonk3(b15)
print("Best b5 parameters:", b17)
if b11.forecast:
    b18 = a8
    b19 = True
    forecast_values, b20 = b16.fonk4(num_steps=b18, b7=b19)
    b21 = np.arange(len(b15) + len(forecast_values))
print("=====================")
if b11.forecast:
    fig, b22 = plt.subplots(3, 2)
    b22[0, 0].plot(b21[:len(b15)], b15, 'b', b23 = 'Actual')
    b22[0, 0].plot(b21[len(b15):], forecast_values, 'r', b23 = 'Forecast')
    if b19:
        b22[0, 0].fill_between(b21[len(b15):],
                               b20[:, 0], b20[:, 1],
                               b24 = 0.3, color='b', b23='Confidence Interval')
    b22[0, 0].grid()
    b22[0, 0].set_title('Noisy Sine')
    b22[0, 0].legend()
    plt.show()