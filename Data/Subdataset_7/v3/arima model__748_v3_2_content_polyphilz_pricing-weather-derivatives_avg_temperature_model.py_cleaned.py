import sys
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
def fonk1(b17):
    plt.figure(b1 = (12, 6))
    plt.plot(b17["mean"], b2 = "blue")
    plt.title("Mean Temperature (Â°F) from 2010 to 2018")
    plt.xlabel("Time")
    plt.ylabel("Mean Temperature (Â°F)")
    plt.savefig("plots/initial_temperature_plot.svg", b3 = 200)
    plt.savefig("plots/initial_temperature_plot.png", b3 = 200)
    plt.close()
def fonk2(b17):
    def fonk3(time_series):
        b4 = adfuller(time_series)
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Augmented Dickey-Fuller Unit Root Test:")
        b5 = ["ADF Test Statistic", "p-value", "Number of Observations Used"]
        for value, label in zip(b4, b5):
            print(f"{label} : {value}")
        if b4[1] <= 0.05:
            print("Strong evidence against the null hypothesis - reject the null hypothesis. Data has no unit root and is stationary.")
        else:
            print("Weak evidence against null hypothesis - do not reject the null hypothesis. Data has a unit root and is non-stationary.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    fonk3(b17["mean"])
    b17["Temp. First Difference"] = b17["mean"] - b17["mean"].shift(1)
    b17["Seasonal Difference"] = b17["mean"] - b17["mean"].shift(365)
    b17["Seasonal First Difference"] = b17["Temp. First Difference"] - b17["Temp. First Difference"].shift(365)
    fonk3(b17["Seasonal First Difference"].dropna())
    return b17
def fonk4(b17):
    plt.figure(b1 = (12, 6))
    b6 = plt.subplot(211)
    plot_acf(b17["mean"].dropna(), b7 = 30, b2="blue", ax=b6)
    b8 = plt.subplot(212)
    plot_pacf(b17["mean"].dropna(), b7 = 30, b2="blue", ax=b8)
    plt.savefig("plots/acf_pacf_plot.svg", b3 = 200)
    plt.savefig("plots/acf_pacf_plot.png", b3 = 200)
    plt.close()
def fonk5(b17, a1):
    b9 = sm.tsa.statespace.SARIMAX(
        b17["mean"], b10 = (1, 1, 2), seasonal_order=(0, 1, 0, a1)
    )
    b11 = b9.fit()
    print(b11.summary())
    return b11
def fonk6(b11):
    plt.figure(b1 = (12, 6))
    plt.plot(b11.resid, b2 = "blue")
    plt.title("Residuals")
    plt.xlabel("Time")
    plt.ylabel("Residual")
    plt.savefig("plots/residuals_plot1.png", b3 = 200)
    plt.savefig("plots/residuals_plot1.svg", b3 = 200)
    plt.close()
    plt.figure(b1 = (12, 6))
    b11.resid.plot(b12 = "kde", b2="blue")
    plt.title("Residuals (Kernel Density Estimation)")
    plt.xlabel("Time")
    plt.savefig("plots/residuals_plot2.png", b3 = 200)
    plt.savefig("plots/residuals_plot2.svg", b3 = 200)
    plt.close()
def fonk7(b17, b11, a1):
    b13 = pd.read_csv("forecasted_existing.csv", index_col="Dates", parse_dates=True)
    b17["forecast"] = b13["temp"]
    plt.figure(b1 = (12, 6))
    plt.plot(b17[["mean", "forecast"]], b2 = ["blue", "red"])
    plt.title("Forecast of Temperature On Existing Data")
    plt.xlabel("Time")
    plt.ylabel("Mean Temperature (Â°F)")
    plt.savefig("plots/predict_existing_values_plot.png", b3 = 200)
    plt.savefig("plots/predict_existing_values_plot.svg", b3 = 200)
    plt.close()
def fonk8(b17, b11, a1):
    b14 = pd.date_range(start=b17.index[-1] + pd.Timedelta(days=1), periods=a1)
    b15 = pd.DataFrame(index=b14, columns=b17.columns)
    b16 = pd.read_csv("forecasted_unknown_1y.csv", index_col="Dates", parse_dates=True)
    b15["forecast"] = b16["temp"]
    plt.figure(b1 = (12, 6))
    plt.plot(b17["mean"], b2 = "green", label="Original Data")
    plt.plot(b15["forecast"], b2 = "red", label="Forecasted Data")
    plt.title(f"Forecast of Temperature For Next {a1} Days")
    plt.xlabel("Time")
    plt.ylabel("Mean Temperature (Â°F)")
    plt.legend()
    plt.savefig("plots/predict_unknown_values_plot.png", b3 = 200)
    plt.savefig("plots/predict_unknown_values_plot.svg", b3 = 200)
    plt.close()
def fonk9():
    try:
        b17 = pd.read_csv("temp_data_cleaned.csv", index_col="Time", parse_dates=True)
    except FileNotFoundError:
        print("Please run `scrape_data.py` and `clean_data.py` in that b10 to generate the necessary data first.")
        sys.exit(0)
    fonk1(b17)
    b17 = fonk2(b17)
    fonk4(b17)
    a1 = 365
    b11 = fonk5(b17, a1)
    fonk6(b11)
    fonk7(b17, b11, a1)
    fonk8(b17, b11, a1)
    print("~ COMPLETION ~")
    print("All plots saved to `plots` folder")
if b18 = = "__main__":
    fonk9()