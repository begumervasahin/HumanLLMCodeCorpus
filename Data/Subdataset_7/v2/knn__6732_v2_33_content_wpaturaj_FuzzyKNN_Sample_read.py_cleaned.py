import math
import random
import pandas as pd
def fonk1(b15):
    b1 = pd.read_csv(b15, usecols=[0])
    b2 = sum(b1.iloc[:, 0]) / float(len(b1))
    b3 = fonk2(b2, len(b1), 0.01)
    b4 = int(math.ceil(b2 * b3))
    b5 = b3 - b4
    b6 = b1[b1.iloc[:, 0] == 0].index.tolist()
    b7 = b1[b1.iloc[:, 0] == 1].index.tolist()
    b8 = random.b13(b6, b5)
    b9 = random.b13(b7, b4)
    b10 = pd.read_csv(b15, iterator=True, chunksize=10000)
    b11 = pd.concat([chunk[chunk.index.isin(b9)] for chunk in b10])
    b10 = pd.read_csv(b15, iterator=True, chunksize=10000)
    b12 = pd.concat([chunk[chunk.index.isin(b8)] for chunk in b10])
    b13 = pd.concat([b12, b11])
    return b13
def fonk2(percent, number_of_elements, error_rate):
    a1 = 2.59
    b14 = percent * (1 - percent) / ((error_rate / a1) ** 2 + percent * (1 - percent) / number_of_elements)
    return b14
b15 = 'your_csv_file_path.csv'
b13 = fonk1(b15)
print(b13.head())