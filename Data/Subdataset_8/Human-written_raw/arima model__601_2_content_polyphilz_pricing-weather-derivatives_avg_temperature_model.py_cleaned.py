import sys
import pandas as pd
from pandas.tseries.offsets import DateOffset
import matplotlib.pyplot as plt
import matplotlib
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
def initial_plot(df):
    initial_plot = plt.figure(num=1, figsize=(12, 6))
    plt.plot(df["mean"], color="
    plt.title("Mean Temperature in Fahrenheit from 2010-2018", figure=initial_plot)
    plt.xlabel("Time", figure=initial_plot)
    plt.ylabel("Mean Temperature (ËF)", figure=initial_plot)
    plt.savefig("plots/initial_plot.svg", dpi=200, figure=initial_plot)
    plt.savefig("plots/initial_plot.png", dpi=200, figure=initial_plot)
def stationarity_check(df):
    def adf_check(time_series):
        result = adfuller(time_series)
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Augmented Dickey-Fuller Unit Root Test:")
        labels = [
            "ADF Test Statistic",
            "p-value",
            "
            "Number of Observations Used",
        ]
        for value, label in zip(result, labels):
            print(label + " : " + str(value))
        if result[1] <= 0.05:
            print(
                "Strong evidence against the null hypothesis - reject the null hypothesis. Data has no unit root and is stationary."
            )
        else:
            print(
                "Weak evidence against null hypothesis - do not reject the null hypothesis. Data has a unit root and is non-stationary."
            )
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()
    adf_check(df["mean"])
    df["Temp. First Difference"] = df["mean"] - df["mean"].shift(1)
    df["Seasonal Difference"] = df["mean"] - df["mean"].shift(365)
    df["Seasonal First Difference"] = df["Temp. First Difference"] - df[
        "Temp. First Difference"
    ].shift(365)
    adf_check(df["Seasonal First Difference"].dropna())
    return df
def acf_pacf_plot(df):
    acf_pacf_plot = plt.figure(figsize=(12, 6))
    ax1 = acf_pacf_plot.add_subplot(211)
    acf_pacf_plot = plot_acf(df["mean"].dropna(), lags=30, color="
    ax2 = acf_pacf_plot.add_subplot(212)
    acf_pacf_plot = plot_pacf(df["mean"].dropna(), lags=30, color="
    plt.savefig("plots/acf_pacf_plot.svg", dpi=200, figure=acf_pacf_plot)
    plt.savefig("plots/acf_pacf_plot.png", dpi=200, figure=acf_pacf_plot)
def model(df, period):
    model = sm.tsa.statespace.SARIMAX(
        df["mean"], order=(1, 1, 2), seasonal_order=(0, 1, 0, period)
    )
    results = model.fit()
    print(results.summary())
    return results
def resids_plot(results):
    resids_plot1 = plt.figure(figsize=(12, 6))
    plt.plot(results.resid, color="
    plt.title("Residuals", figure=resids_plot1)
    plt.xlabel("Time", figure=resids_plot1)
    plt.ylabel("Residual", figure=resids_plot1)
    plt.savefig("plots/resids_plot1.png", dpi=200, figure=resids_plot1)
    plt.savefig("plots/resids_plot1.svg", dpi=200, figure=resids_plot1)
    resids_plot2 = plt.figure(figsize=(12, 6))
    ax = resids_plot2.add_subplot(111)
    plt.title("Residuals (Kernel Density Estimation)", figure=resids_plot2)
    plt.xlabel("Time", figure=resids_plot2)
    results.resid.plot(kind="kde", color="
    resids_plot2.savefig("plots/resids_plot2.png", dpi=200)
    resids_plot2.savefig("plots/resids_plot2.svg", dpi=200)
def validate_model(df, results, period):
    """
    Input(s): The pandas DataFrame, the SARIMAX results wrapper object and the period variable (365)
    Output: A graph plotting the original data next to the forecasted data for the same time period
    NOTES
    `df["forecast"] = results.predict(start=1, end=len(df))` is commented out because this line will CRASH THE PROGRAM.
    It should be noted that statsmodels' SARIMAX ideally shouldn't be used for seasonal data that's not monthly or quarterly.
    The period passed in, 365, simply creates too many dense arrays and as a result, the computer used to test this ran out of RAM.
    The forecasted data for the existing time period was generated in R and outputted to a csv file: `forecasted_existing.csv`.
    This has exactly 2923 observations of data; the same as the 8 years used here. It is concatenated to df["forecast"].
    """
    existing_data = pd.read_csv(
        "forecasted_existing.csv", index_col="Dates", parse_dates=True
    )
    df["forecast"] = existing_data["temp"]
    predict_existing_values_plot = plt.figure(figsize=(12, 6))
    ax = predict_existing_values_plot.add_subplot(111)
    plt.title(
        f"Forecast of Temperature On Existing Data", figure=predict_existing_values_plot
    )
    plt.xlabel("Time", figure=predict_existing_values_plot)
    plt.ylabel("Mean Temperature (ËF)", figure=predict_existing_values_plot)
    df[["mean", "forecast"]].plot(color=["
    predict_existing_values_plot.savefig(
        "plots/predict_existing_values_plot.png", dpi=200
    )
    predict_existing_values_plot.savefig(
        "plots/predict_existing_values_plot.svg", dpi=200
    )
def forecast(df, results, period):
    """
    Input(s): The pandas DataFrame, the SARIMAX results wrapper object and the period variable (365)
    Output: A graph plotting the original data in green and the predicted data for one year out in red
    NOTES
    `future_df["forecast"] = results.predict(start=len(df), end=len(future_df), dynamic=True)` is commented out.
    This is because this line will CRASH THE PROGRAM. Please see the justification as to why in the Docstring underneath
    the `validate_model` function. The forecasted data for the future time period was generated in R and outputted to a
    csv file: `forecasted_unknown_1y.csv`. This has exactly 365 observations of data, or 1 year into the future. It is
    concatenated to future_df["forecast"].
    """
    future_dates = [df.index[-1] + DateOffset(days=x) for x in range(0, period)]
    future_dates_df = pd.DataFrame(index=future_dates[1:], columns=df.columns)
    future_df = pd.concat([df, future_dates_df])
    unknown_data_1y = pd.read_csv(
        "forecasted_unknown_1y.csv", index_col="Dates", parse_dates=True
    )
    future_df["forecast"] = unknown_data_1y["temp"]
    predict_unknown_values_plot = plt.figure(figsize=(12, 6))
    ax = predict_unknown_values_plot.add_subplot(111)
    plt.title(
        f"Forecast of Temperature For Next {period} Days",
        figure=predict_unknown_values_plot,
    )
    plt.xlabel("Time", figure=predict_unknown_values_plot)
    plt.ylabel("Mean Temperature (ËF)", figure=predict_unknown_values_plot)
    future_df[["mean", "forecast"]].plot(
        color=["
    )
    predict_unknown_values_plot.savefig(
        "plots/predict_unknown_values_plot.png", dpi=200
    )
    predict_unknown_values_plot.savefig(
        "plots/predict_unknown_values_plot.svg", dpi=200
    )
def main():
    try:
        df = pd.read_csv("temp_data_cleaned.csv", index_col="Time", parse_dates=True)
    except:
        print(
            "Please run `scrape_data.py` and `clean_data.py` in that order to generate the necessary data first."
        )
        sys.exit(0)
    initial_plot(df)
    df = stationarity_check(df)
    acf_pacf_plot(df)
    period = 365
    results = model(df, period)
    resids_plot(results)
    validate_model(df, results, period)
    forecast(df, results, period)
    print("~ COMPLETION ~")
    print("All plots saved to `plots` folder")
if __name__ == "__main__":
    main()