import pandas as pd
def fonk1(data_name):
    b1 = pd.read_csv(data_name)
    return b1
b2 = "your_data_file.csv"
b3 = fonk1(b2)
print(b3.head())