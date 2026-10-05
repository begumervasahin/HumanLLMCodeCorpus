import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import argparse
class AutoArimaModel:
    def __init__(self, start_p=1, max_p=3, start_q=1, max_q=3):
        self.start_p = start_p
        self.max_p = max_p
        self.start_q = start_q
        self.max_q = max_q
        self.model = None
    def fit(self, data):
        self.model = ARIMA(data, order=self.get_params())
        self.model_fit = self.model.fit()
    def get_params(self):
        return self.model.auto_arima(self.model.endog, start_p=self.start_p, max_p=self.max_p,
                                     start_q=self.start_q, max_q=self.max_q).order
    def forecast(self, num_steps, conf_int=False):
        return self.model_fit.forecast(steps=num_steps, alpha=0.05) if conf_int else self.model_fit.forecast(steps=num_steps)
def get_cmd_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--forecast", help="perform forecasts and plot results", action="store_true")
    args = parser.parse_args()
    return args
args = get_cmd_line_args()
A = 1
a = 0.35
t_start = 0
t_end = 60
t_delta = 0.1
noise_mean = 0
noise_std = 1
num_forecast_steps = 100
print("Analyzing Noisy Sine...")
time = np.arange(t_start, t_end, t_delta)
y = A * np.sin(time)
noise = np.random.normal(noise_mean, noise_std, len(y))
yn = np.add(y, a * noise)
arima_model = AutoArimaModel(start_p=1, max_p=3, start_q=1, max_q=3)
arima_model.fit(yn)
model_args = arima_model.get_params()
print(model_args)
if args.forecast:
    Ypred1, conf_int1 = arima_model.forecast(num_steps=num_forecast_steps, conf_int=True)
    time_axis = np.arange(len(yn) + len(Ypred1))
print("=====================")
if args.forecast:
    fig, axs = plt.subplots(3, 2)
    axs[0, 0].plot(time_axis[:len(yn)], yn, 'b')
    axs[0, 0].plot(time_axis[len(yn):], Ypred1, 'r')
    axs[0, 0].fill_between(time_axis[len(yn):],
                           conf_int1[:, 0], conf_int1[:, 1],
                           alpha=0.3, color='b')
    axs[0, 0].grid()
    axs[0, 0].set_title('Noisy Sine')
    plt.show()