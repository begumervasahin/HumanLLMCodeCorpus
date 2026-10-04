import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
import statsmodels.tsa.stattools as st
def parse_datetime(x):
    return to_datetime(x, format='%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    total_error = sum(math.fabs(pred - true) / true for true, pred in zip(y_true, y_pred))
    return total_error / len(y_true)
def load_data(file_path, selected_columns, date_columns, date_parser):
    return read_csv(
        file_path,
        usecols=selected_columns,
        header=0,
        parse_dates=date_columns,
        index_col=0,
        squeeze=True,
        date_parser=date_parser
    )
def main():
    file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
    selected_columns = [2, 3]
    date_columns = [0]
    series = load_data(file_path, selected_columns, date_columns, parse_datetime)
    data_values = series.values
    start_index = 2
    training_size = 200
    arima_train_data = data_values[start_index : start_index + training_size]
    adf_test_result = st.adfuller(arima_train_data)
    print("ADF Test Result:", adf_test_result)
    plt.plot(arima_train_data)
    plt.title('Training Data')
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.show()
if __name__ == "__main__":
    main()