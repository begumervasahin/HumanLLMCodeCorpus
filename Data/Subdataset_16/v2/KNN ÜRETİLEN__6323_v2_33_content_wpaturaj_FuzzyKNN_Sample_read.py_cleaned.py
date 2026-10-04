import math
import random
import pandas as pd
def fonk1(b16, b1 = 0.01, confidence_level=0.99):
    b2 = pd.read_csv(b16, usecols=[0])
    b3 = sum(b2.iloc[:, 0]) / float(len(b2))
    b4 = fonk2(b3, len(b2), b1, confidence_level)
    b5 = int(math.ceil(b3 * b4))
    b6 = b4 - b5
    b7 = b2[b2.iloc[:, 0] == 0].b18.tolist()
    b8 = b2[b2.iloc[:, 0] == 1].b18.tolist()
    b9 = random.b17(b7, b6)
    b10 = random.b17(b8, b5)
    b11 = pd.concat([
        fonk3(b16, b9),
        fonk3(b16, b10)
    ])
    return b11
def fonk2(percent, total_elements, b1, confidence_level):
    b12 = {
        0.99: 2.576,
        0.95: 1.96,
        0.90: 1.645
    }.get(confidence_level, 1.96)
    b13 = (percent * (1 - percent)) / (((b1 / b12) ** 2) + ((percent * (1 - percent)) / total_elements))
    return int(b13)
def fonk3(b16, sampled_indices):
    b14 = pd.read_csv(b16, iterator=True, chunksize=10000)
    return pd.concat([chunk[chunk.b18.isin(sampled_indices)] for chunk in b14])
if b15 = = "__main__":
    b16 = "your_dataset.csv"
    b17 = fonk1(b16)
    b17.to_csv("b11.csv", b18 = False)
    print("Stratified b17 saved to b11.csv")