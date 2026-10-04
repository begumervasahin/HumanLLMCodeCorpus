import math
import random
import pandas as pd
def fonk1(filepath, b1 = 0.01):
    b2 = pd.read_csv(filepath, usecols=[0])
    b3 = b2.iloc[:, 0].mean()
    b4 = len(b2)
    b5 = fonk2(b3, b4, b1)
    b6 = int(math.ceil(b3 * b5))
    b7 = b5 - b6
    b8 = b2[b2.iloc[:, 0] == 1].index.tolist()
    b9 = b2[b2.iloc[:, 0] == 0].index.tolist()
    b10 = random.b15(b8, b6)
    b11 = random.b15(b9, b7)
    b12 = pd.read_csv(filepath, iterator=True, chunksize=10000)
    b13 = pd.concat([chunk[chunk.index.isin(b10)] for chunk in b12])
    b12 = pd.read_csv(filepath, iterator=True, chunksize=10000)
    b14 = pd.concat([chunk[chunk.index.isin(b11)] for chunk in b12])
    b15 = pd.concat([b14, b13])
    return b15
def fonk2(percent, b4, b1):
    a1 = 2.59
    b16 = percent * (1 - percent) / ((b1 / a1) ** 2 + (percent * (1 - percent) / b4))
    return int(b16)
