import pandas as pd
def load_data(file_name):
    try:
        data = pd.read_csv(file_name)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_name}' is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: The file '{file_name}' could not be parsed.")
        return None
if __name__ == "__main__":
    data_file_name = "your_data_file.csv"
    loaded_data = load_data(data_file_name)
    if loaded_data is not None:
        print("Preview of the loaded data:")
        print(loaded_data.head())