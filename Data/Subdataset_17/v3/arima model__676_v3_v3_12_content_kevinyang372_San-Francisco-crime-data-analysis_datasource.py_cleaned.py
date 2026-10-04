import pandas as pd
def load_data(file_path):
    return pd.read_csv(file_path)
if __name__ == "__main__":
    csv_file_path = "your_data_file.csv"
    data_frame = load_data(csv_file_path)
    print("Preview of the loaded data:")
    print(data_frame.head())