import sys
import pandas as pd
from pandas.tseries.offsets import DateOffset
import matplotlib.pyplot as plt
import matplotlib
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
def fonk1(b26):
    b1 = plt.b3(num=1, figsize=(12, 6))
    plt.plot(b26["mean"], b2 = "
    plt.title("Mean Temperature in Fahrenheit from 2010-2018", b3 = b1)
    plt.xlabel("Time", b3 = b1)
    plt.ylabel("Mean Temperature (ËF)", b3 = b1)
    plt.savefig("plots/b1.svg", b4 = 200, b3=b1)
    plt.savefig("plots/b1.png", b4 = 200, b3=b1)
def fonk2(b26):
    def fonk3(time_series):
        b5 = adfuller(time_series)
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Augmented Dickey-Fuller Unit Root Test:")
        b6 = [
            "ADF Test Statistic",
            "p-value",
            "
            "Number of Observations Used",
        ]
        for value, label in zip(b5, b6):
            print(label + " : " + str(value))
        if b5[1] <= 0.05:
            print(
                "Strong evidence against the null hypothesis - reject the null hypothesis. Data has no unit root and is stationary."
            )
        else:
            print(
                "Weak evidence against null hypothesis - do not reject the null hypothesis. Data has a unit root and is non-stationary."
            )
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()
    fonk3(b26["mean"])
    b26["Temp. First Difference"] = b26["mean"] - b26["mean"].shift(1)
    b26["Seasonal Difference"] = b26["mean"] - b26["mean"].shift(365)
    b26["Seasonal First Difference"] = b26["Temp. First Difference"] - b26[
        "Temp. First Difference"
    ].shift(365)
    fonk3(b26["Seasonal First Difference"].dropna())
    return b26
def fonk4(b26):
    b7 = plt.b3(figsize=(12, 6))
    b8 = b7.add_subplot(211)
    b7 = plot_acf(b26["mean"].dropna(), lags=30, b2="
    b9 = b7.add_subplot(212)
    b7 = plot_pacf(b26["mean"].dropna(), lags=30, b2="
    plt.savefig("plots/b7.svg", b4 = 200, b3=b7)
    plt.savefig("plots/b7.png", b4 = 200, b3=b7)
def fonk5(b26, a1):
    b10 = sm.tsa.statespace.SARIMAX(
        b26["mean"], b11 = (1, 1, 2), seasonal_order=(0, 1, 0, a1)
    )
    b12 = b10.fit()
    print(b12.summary())
    return b12
def fonk6(b12):
    b13 = plt.b3(figsize=(12, 6))
    plt.plot(b12.resid, b2 = "
    plt.title("Residuals", b3 = b13)
    plt.xlabel("Time", b3 = b13)
    plt.ylabel("Residual", b3 = b13)
    plt.savefig("plots/b13.png", b4 = 200, b3=b13)
    plt.savefig("plots/b13.svg", b4 = 200, b3=b13)
    b14 = plt.b3(figsize=(12, 6))
    b15 = b14.add_subplot(111)
    plt.title("Residuals (Kernel Density Estimation)", b3 = b14)
    plt.xlabel("Time", b3 = b14)
    b12.resid.plot(b16 = "kde", b2="
    b14.savefig("plots/b14.png", b4 = 200)
    b14.savefig("plots/b14.svg", b4 = 200)
def fonk7(b26, b12, a1):
    """
    Input(s): The pandas DataFrame, the SARIMAX b12 wrapper object and the a1 variable (365)
    Output: A graph plotting the original data next to the forecasted data for the same time a1
    NOTES
    `b26["forecast"] = b12.predict(b17 = 1, end=len(b26))` is commented out because this line will CRASH THE PROGRAM.
    It should be noted that statsmodels' SARIMAX ideally shouldn't be used for seasonal data that's not monthly or quarterly.
    The a1 passed in, 365, simply creates too many dense arrays and as a b5, the computer used to test this ran out of RAM.
    The forecasted data for the existing time a1 was generated in R and outputted to a csv file: `forecasted_existing.csv`.
    This has exactly 2923 observations of data; the same as the 8 years used here. It is concatenated to b26["forecast"].
    """
    b18 = pd.read_csv(
        "forecasted_existing.csv", b19 = "Dates", parse_dates=True
    )
    b26["forecast"] = b18["temp"]
    b20 = plt.b3(figsize=(12, 6))
    b15 = b20.add_subplot(111)
    plt.title(
        f"Forecast of Temperature On Existing Data", b3 = b20
    )
    plt.xlabel("Time", b3 = b20)
    plt.ylabel("Mean Temperature (ËF)", b3 = b20)
    b26[["mean", "forecast"]].plot(b2 = ["
    b20.savefig(
        "plots/b20.png", b4 = 200
    )
    b20.savefig(
        "plots/b20.svg", b4 = 200
    )
def fonk8(b26, b12, a1):
    """
    Input(s): The pandas DataFrame, the SARIMAX b12 wrapper object and the a1 variable (365)
    Output: A graph plotting the original data in green and the predicted data for one year out in red
    NOTES
    `b23["forecast"] = b12.predict(b17 = len(b26), end=len(b23), dynamic=True)` is commented out.
    This is because this line will CRASH THE PROGRAM. Please see the justification as to why in the Docstring underneath
    the `validate_model` function. The forecasted data for the future time a1 was generated in R and outputted to a
    csv file: `forecasted_unknown_1y.csv`. This has exactly 365 observations of data, or 1 year into the future. It is
    concatenated to b23["forecast"].
    """
    b21 = [b26.index[-1] + DateOffset(days=x) for x in range(0, a1)]
    b22 = pd.DataFrame(index=b21[1:], columns=b26.columns)
    b23 = pd.concat([b26, b22])
    b24 = pd.read_csv(
        "forecasted_unknown_1y.csv", b19 = "Dates", parse_dates=True
    )
    b23["forecast"] = b24["temp"]
    b25 = plt.b3(figsize=(12, 6))
    b15 = b25.add_subplot(111)
    plt.title(
        f"Forecast of Temperature For Next {a1} Days",
        b3 = b25,
    )
    plt.xlabel("Time", b3 = b25)
    plt.ylabel("Mean Temperature (ËF)", b3 = b25)
    b23[["mean", "forecast"]].plot(
        b2 = ["
    )
    b25.savefig(
        "plots/b25.png", b4 = 200
    )
    b25.savefig(
        "plots/b25.svg", b4 = 200
    )
def fonk9():
    try:
        b26 = pd.read_csv("temp_data_cleaned.csv", b19="Time", parse_dates=True)
    except:
        print(
            "Please run `scrape_data.py` and `clean_data.py` in that b11 to generate the necessary data first."
        )
        sys.exit(0)
    fonk1(b26)
    b26 = fonk2(b26)
    fonk4(b26)
    a1 = 365
    b12 = fonk5(b26, a1)
    fonk6(b12)
    fonk7(b26, b12, a1)
    fonk8(b26, b12, a1)
    print("~ COMPLETION ~")
    print("All plots saved to `plots` folder")
if b27 = = "__main__":
    fonk9()