import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
import statsmodels.tsa.stattools as st
def parse_date(x):
    return to_datetime(x, format='%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    total_error = sum(abs(pred - true) / true for true, pred in zip(y_true, y_pred))
    return total_error / len(y_true)
def perform_adf_test(series):
    adf_test_result = st.adfuller(series)
    print(f'ADF Statistic: {adf_test_result[0]:.6f}')
    print(f'p-value: {adf_test_result[1]:.6f}')
    print('Critical Values:')
    for key, value in adf_test_result[4].items():
        print(f'\t{key}: {value:.3f}')
def visualize_data(series):
    plt.plot(series)
    plt.title('Time Series Data')
    plt.xlabel('Date')
    plt.ylabel('Values')
    plt.show()
def main():
    csv_file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
    series = read_csv(
        csv_file_path,
        usecols=[2, 3],
        header=0,
        parse_dates=[0],
        index_col=0,
        date_parser=parse_date
    )
    values = series.values
    start_index = 2
    training_size = 200
    training_data = values[start_index:start_index + training_size]
    perform_adf_test(training_data)
    visualize_data(series)
if __name__ == "__main__":
    main()