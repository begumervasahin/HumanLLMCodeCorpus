import numpy as np
import matplotlib.pyplot as plt
import auto_arima_model as am
import argparse
def fonk1():
    b1 = argparse.ArgumentParser()
    b1.add_argument("-f", "--forecast", b2 = "perform forecasts and plot results", action="store_true")
    return b1.parse_args()
def fonk2():
    a1 = 1
    a2 = 0.35
    a3 = 0
    a4 = 60
    a5 = 0.1
    a6 = 0
    a7 = 1
    b3 = np.arange(a3, a4, a5)
    b4 = a1 * np.sin(b3)
    b5 = np.random.normal(a6, a7, len(b4))
    return b3, np.add(b4, a2 * b5)
def fonk3(b11, data, a8):
    b11.fit(data)
    return b11.forecast(b6 = a8, b15=True)
def fonk4(b16, b3, data, forecast, b15, color):
    b16.plot(b3[:len(data)], data, 'b')
    b16.plot(b3[len(data):], forecast, 'r')
    b16.fill_between(b3[len(data):], b15[:, 0], b15[:, 1], b7 = 0.3, color='b')
    b16.grid()
    b16.set(b8 = 'Time Sample', ylabel='Amplitude')
def fonk5():
    b9 = fonk1()
    a8 = 100
    print("Analyzing Noisy Sine...")
    b3, b10 = fonk2()
    b11 = am.AutoArimaModel(start_p=1, max_p=3, start_q=1, max_q=3)
    b12 = b11.get_params()
    print(b12)
    if b9.forecast:
        Ypred1, b13 = fonk3(b11, b10, a8)
        b14 = np.arange(len(b10) + len(Ypred1))
    print("=====================")
    for title, data_func in [("Up-Ramp", lambda t: np.add(t, b10)),
                              ("Down-Ramp", lambda t: np.add(a4 - t, b10)),
                              ("Quadratic-Ramp", lambda t: np.add(0.01 * np.power(t, 2), b10)),
                              ("Cubic-Ramp", lambda t: np.add((1 / 5000) * np.power(t, 3), b10)),
                              ("Fourth-power Ramp", lambda t: np.add((1 / 200000) * np.power(t, 4), b10))]:
        print(f"Analyzing {title}...")
        b4 = data_func(b3)
        b11.fit(b4)
        b12 = b11.get_params()
        print(b12)
        if b9.forecast:
            forecast_data, b15 = fonk3(b11, b4, a8)
            fig, b16 = plt.subplots()
            fonk4(b16, b14, b4, forecast_data, b15, 'b')
            b16.set_title(title)
            plt.show()
if b17 = = "__main__":
    fonk5()