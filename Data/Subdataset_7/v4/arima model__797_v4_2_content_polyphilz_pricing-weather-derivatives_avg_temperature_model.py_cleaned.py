import sys
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from pandas.tseries.offsets import DateOffset
def fonk1(b15):
    plt.figure(b1 = (12, 6))
    plt.plot(b15["mean"], b2 = "blue")
    plt.title("Mean Temperature in Fahrenheit from 2010-2018")
    plt.xlabel("Time")
    plt.ylabel("Mean Temperature (ËF)")
    plt.savefig("plots/initial_plot.svg", b3 = 200)
    plt.savefig("plots/initial_plot.png", b3 = 200)
def fonk2(b15):
    def fonk3(time_series):
        b4 = adfuller(time_series)
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Augmented Dickey-Fuller Unit Root Test:")
        b5 = ["ADF Test Statistic", "p-value", "Number of Observations Used"]
        for value, label in zip(b4, b5):
            print(label + " : " + str(value))
        if b4[1] <= 0.05:
            print("Strong evidence against the null hypothesis - reject the null hypothesis. Data has no unit root and is stationary.")
        else:
            print("Weak evidence against null hypothesis - do not reject the null hypothesis. Data has a unit root and is non-stationary.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    fonk3(b15["mean"])
    b15["Temp. First Difference"] = b15["mean"] - b15["mean"].shift(1)
    b15["Seasonal Difference"] = b15["mean"] - b15["mean"].shift(365)
    b15["Seasonal First Difference"] = b15["Temp. First Difference"] - b15["Temp. First Difference"].shift(365)
    fonk3(b15["Seasonal First Difference"].dropna())
    return b15
def fonk4(b15):
    plt.figure(b1 = (12, 6))
    plt.subplot(211)
    plot_acf(b15["mean"].dropna(), b6 = 30, b2="blue")
    plt.subplot(212)
    plot_pacf(b15["mean"].dropna(), b6 = 30, b2="blue")
    plt.savefig("plots/acf_pacf_plot.svg", b3 = 200)
    plt.savefig("plots/acf_pacf_plot.png", b3 = 200)
def fonk5(b15, a1):
    b7 = sm.tsa.statespace.SARIMAX(b15["mean"], order=(1, 1, 2), seasonal_order=(0, 1, 0, a1))
    b8 = b7.fit()
    print(b8.summary())
    return b8
def fonk6(b8):
    plt.figure(b1 = (12, 6))
    plt.plot(b8.resid, b2 = "blue")
    plt.title("Residuals")
    plt.xlabel("Time")
    plt.ylabel("Residual")
    plt.savefig("plots/resids_plot1.png", b3 = 200)
    plt.savefig("plots/resids_plot1.svg", b3 = 200)
    plt.figure(b1 = (12, 6))
    b8.resid.plot(b9 = "kde", b2="blue")
    plt.title("Residuals (Kernel Density Estimation)")
    plt.xlabel("Time")
    plt.savefig("plots/resids_plot2.png", b3 = 200)
    plt.savefig("plots/resids_plot2.svg", b3 = 200)
def fonk7(b15, b8, a1):
    b10 = pd.read_csv("forecasted_existing.csv", index_col="Dates", parse_dates=True)
    b15["forecast"] = b10["temp"]
    plt.figure(b1 = (12, 6))
    plt.title("Forecast of Temperature On Existing Data")
    plt.xlabel("Time")
    plt.ylabel("Mean Temperature (ËF)")
    b15[["mean", "forecast"]].plot(b2 = ["green", "red"])
    plt.savefig("plots/predict_existing_values_plot.png", b3 = 200)
    plt.savefig("plots/predict_existing_values_plot.svg", b3 = 200)
def fonk8(b15, b8, a1):
    b11 = [b15.index[-1] + DateOffset(days=x) for x in range(0, a1)]
    b12 = pd.DataFrame(index=b11[1:], columns=b15.columns)
    b13 = pd.concat([b15, b12])
    b14 = pd.read_csv("forecasted_unknown_1y.csv", index_col="Dates", parse_dates=True)
    b13["forecast"] = b14["temp"]
    plt.figure(b1 = (12, 6))
    plt.title(f"Forecast of Temperature For Next {a1} Days")
    plt.xlabel("Time")
    plt.ylabel("Mean Temperature (ËF)")
    b13[["mean", "forecast"]].plot(b2 = ["green", "red"])
    plt.savefig("plots/predict_unknown_values_plot.png", b3 = 200)
    plt.savefig("plots/predict_unknown_values_plot.svg", b3 = 200)
def fonk9():
    try:
        b15 = pd.read_csv("temp_data_cleaned.csv", index_col="Time", parse_dates=True)
    except FileNotFoundError:
        print("Please run `scrape_data.py` and `clean_data.py` in that order to generate the necessary data first.")
        sys.exit(0)
    fonk1(b15)
    b15 = fonk2(b15)
    fonk4(b15)
    a1 = 365
    b8 = fonk5(b15, a1)
    fonk6(b8)
    fonk7(b15, b8, a1)
    fonk8(b15, b8, a1)
    print("~ COMPLETION ~")
    print("All plots saved to `plots` folder")
if b16 = = "__main__":
    fonk9()