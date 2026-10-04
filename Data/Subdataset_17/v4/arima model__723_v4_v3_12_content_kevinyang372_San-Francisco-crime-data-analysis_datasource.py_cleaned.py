import pandas as pd
def load_data(file_name):
    data = pd.read_csv(file_name)
    return data
data_file_name = "your_data_file.csv"
loaded_data = load_data(data_file_name)
print("Preview of the loaded data:")
print(loaded_data.head())