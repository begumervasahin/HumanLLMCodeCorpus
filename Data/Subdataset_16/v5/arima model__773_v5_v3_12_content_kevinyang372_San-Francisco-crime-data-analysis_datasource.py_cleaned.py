import pandas as pd
def fonk1(file_name):
    try:
        b1 = pd.read_csv(file_name)
        return b1
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_name}' is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: The file '{file_name}' could not be parsed.")
        return None
if b2 = = "__main__":
    b3 = "your_data_file.csv"
    b4 = fonk1(b3)
    if b4 is not None:
        print("Preview of the loaded b1:")
        print(b4.head())