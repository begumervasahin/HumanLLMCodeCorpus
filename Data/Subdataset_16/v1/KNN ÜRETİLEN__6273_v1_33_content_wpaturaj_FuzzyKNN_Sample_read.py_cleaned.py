import math
import random
import pandas as pd
def fonk1(b16):
    b1 = pd.read_csv(b16, usecols=[0])
    b2 = sum(b1.iloc[:, 0]) / float(len(b1))
    b3 = fonk2(b2, len(b1), 0.01)
    b4 = int(math.ceil(b2 * b3))
    b5 = b3 - b4
    b6 = b1[b1.iloc[:, 0] == 0].b17.tolist()
    b7 = b1[b1.iloc[:, 0] == 1].b17.tolist()
    b8 = random.b13(b6, b5)
    b9 = random.b13(b7, b4)
    b10 = pd.read_csv(b16, iterator=True, chunksize=10000)
    b11 = pd.concat([chunk[chunk.b17.isin(b9)] for chunk in b10])
    b10 = pd.read_csv(b16, iterator=True, chunksize=10000)
    b12 = pd.concat([chunk[chunk.b17.isin(b8)] for chunk in b10])
    b13 = pd.concat([b12, b11])
    return b13
def fonk2(percent, number_of_elements, error_rate):
    a1 = 2.59
    b14 = percent * (1 - percent) / ((error_rate / a1) ** 2 + percent * (1 - percent) / number_of_elements)
    return int(b14)
if b15 = = "__main__":
    b16 = "your_dataset.csv"
    b13 = fonk1(b16)
    b13.to_csv("stratified_sample.csv", b17 = False)
    print("Stratified b13 saved to stratified_sample.csv")