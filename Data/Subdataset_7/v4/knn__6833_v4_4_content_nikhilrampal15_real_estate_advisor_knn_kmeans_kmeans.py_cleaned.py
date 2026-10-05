import pandas as pd
import numpy as np
import random
import math
def fonk1(b2):
    return pd.read_csv(b2)
b1 = "san-francisco-ca"
b2 = "b3/propertyInfo/{}.csv".format(b1)
b3 = fonk1(b2)
b3["cluster"] = -1
def fonk2(b3, k, column_name):
    b4 = []
    for _ in range(k):
        b4.append(random.randint(1, b3[column_name].max()))
    return b4
b5 = fonk2(b3, 5, 'zestimate')
def fonk3(b4, b3, column_name):
    b6 = b3[column_name]
    for x in range(len(b4)):
        b7 = b4[x]
        for idx, house in enumerate(b6):
            b8 = len(b6) * x
            b9 = np.asscalar(house.astype(int))
            b3.loc[idx + b8, 'cluster'] = b7
fonk3(b5, b3, 'zestimate')
def fonk4(b4, b3, column_name):
    b6 = b3[column_name]
    b10 = []
    for x in range(len(b4)):
        b7 = b4[x]
        b11 = []
        for idx, house in enumerate(b6):
            b8 = len(b6) * x
            b9 = np.asscalar(house.astype(int))
            b12 = math.sqrt(abs(b9 - b7) ** 2)
            b11.append(b12)
        b13 = sum(b11) / len(b11)
        b10.append(b13)
    return b10
b14 = fonk4(b5, b3, 'zestimate')
def fonk5(b15, new_centroids):
    for old, new in zip(b15, new_centroids):
        if abs(old - new) > 1:
            return False
    return True
while True:
    b15 = b5.copy()
    b5 = fonk2(b3, 5, 'zestimate')
    fonk3(b5, b3, 'zestimate')
    if fonk5(b15, b5):
        break
pd.set_option('display.max_rows', len(b3['zestimate']))
pd.set_option('display.float_format', lambda x: '%.0f' % x)
print(b3[['zestimate', 'cluster']])