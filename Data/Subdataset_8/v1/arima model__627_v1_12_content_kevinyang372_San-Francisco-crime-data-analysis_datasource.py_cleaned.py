import pandas as pd
def load_data(data_name):
    file = pd.read_csv(data_name)
    return file
data_file_name = "your_data_file.csv"
loaded_data = load_data(data_file_name)
print(loaded_data.head())