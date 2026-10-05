import sys
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
def initial_temperature_plot(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df["mean"], color="blue")
    plt.title("Mean Temperature (Â°F) from 2010 to 2018")
    plt.xlabel("Time")
    plt.ylabel("Mean Temperature (Â°F)")
    plt.savefig("plots/initial_temperature_plot.svg", dpi=200)
    plt.savefig("plots/initial_temperature_plot.png", dpi=200)
    plt.close()
def check_stationarity(df):
    def perform_adf_test(time_series):
        result = adfuller(time_series)
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Augmented Dickey-Fuller Unit Root Test:")
        labels = ["ADF Test Statistic", "p-value", "Number of Observations Used"]
        for value, label in zip(result, labels):
            print(label + " : " + str(value))
        if result[1] <= 0.05:
            print("Strong evidence against the null hypothesis - reject the null hypothesis. Data has no unit root and is stationary.")
        else:
            print("Weak evidence against null hypothesis - do not reject the null hypothesis. Data has a unit root and is non-stationary.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()
    perform_adf_test(df["mean"])
    df["Temp. First Difference"] = df["mean"] - df["mean"].shift(1)
    df["Seasonal Difference"] = df["mean"] - df["mean"].shift(365)
    df["Seasonal First Difference"] = df["Temp. First Difference"] - df["Temp. First Difference"].shift(365)
    perform_adf_test(df["Seasonal First Difference"].dropna())
    return df
def plot_acf_pacf(df):
    plt.figure(figsize=(12, 6))
    ax1 = plt.subplot(211)
    plot_acf(df["mean"].dropna(), lags=30, color="blue", ax=ax1)
    ax2 = plt.subplot(212)
    plot_pacf(df["mean"].dropna(), lags=30, color="blue", ax=ax2)
    plt.savefig("plots/acf_pacf_plot.svg", dpi=200)
    plt.savefig("plots/acf_pacf_plot.png", dpi=200)
    plt.close()
def build_sarimax_model(df, period):
    model = sm.tsa.statespace.SARIMAX(
        df["mean"], order=(1, 1, 2), seasonal_order=(0, 1, 0, period)
    )
    results = model.fit()
    print(results.summary())
    return results
def plot_residuals(results):
    plt.figure(figsize=(12, 6))
    plt.plot(results.resid, color="blue")
    plt.title("Residuals")
    plt.xlabel("Time")
    plt.ylabel("Residual")
    plt.savefig("plots/residuals_plot1.png", dpi=200)
    plt.savefig("plots/residuals_plot1.svg", dpi=200)
    plt.close()
    plt.figure(figsize=(12, 6))
    results.resid.plot(kind="kde", color="blue")
    plt.title("Residuals (Kernel Density Estimation)")
    plt.xlabel("Time")
    plt.savefig("plots/residuals_plot2.png", dpi=200)
    plt.savefig("plots/residuals_plot2.svg", dpi=200)
    plt.close()
def validate_existing_data(df, results, period):
    existing_data = pd.read_csv("forecasted_existing.csv", index_col="Dates", parse_dates=True)
    df["forecast"] = existing_data["temp"]
    plt.figure(figsize=(12, 6))
    plt.plot(df[["mean", "forecast"]], color=["blue", "red"])
    plt.title("Forecast of Temperature On Existing Data")
    plt.xlabel("Time")
    plt.ylabel("Mean Temperature (Â°F)")
    plt.savefig("plots/predict_existing_values_plot.png", dpi=200)
    plt.savefig("plots/predict_existing_values_plot.svg", dpi=200)
    plt.close()
def forecast_future_data(df, results, period):
    future_dates = pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=period)
    future_df = pd.DataFrame(index=future_dates, columns=df.columns)
    unknown_data_1y = pd.read_csv("forecasted_unknown_1y.csv", index_col="Dates", parse_dates=True)
    future_df["forecast"] = unknown_data_1y["temp"]
    plt.figure(figsize=(12, 6))
    plt.plot(df["mean"], color="green", label="Original Data")
    plt.plot(future_df["forecast"], color="red", label="Forecasted Data")
    plt.title(f"Forecast of Temperature For Next {period} Days")
    plt.xlabel("Time")
    plt.ylabel("Mean Temperature (Â°F)")
    plt.legend()
    plt.savefig("plots/predict_unknown_values_plot.png", dpi=200)
    plt.savefig("plots/predict_unknown_values_plot.svg", dpi=200)
    plt.close()
def main():
    try:
        df = pd.read_csv("temp_data_cleaned.csv", index_col="Time", parse_dates=True)
    except FileNotFoundError:
        print("Please run `scrape_data.py` and `clean_data.py` in that order to generate the necessary data first.")
        sys.exit(0)
    initial_temperature_plot(df)
    df = check_stationarity(df)
    plot_acf_pacf(df)
    period = 365
    results = build_sarimax_model(df, period)
    plot_residuals(results)
    validate_existing_data(df, results, period)
    forecast_future_data(df, results, period)
    print("~ COMPLETION ~")
    print("All plots saved to `plots` folder")
if __name__ == "__main__":
    main()