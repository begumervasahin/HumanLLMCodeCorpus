import pandas as pd
def fonk1(file_name):
    b1 = pd.read_csv(file_name)
    return b1
b2 = "your_data_file.csv"
b3 = fonk1(b2)
print("Preview of the loaded b1:")
print(b3.head())