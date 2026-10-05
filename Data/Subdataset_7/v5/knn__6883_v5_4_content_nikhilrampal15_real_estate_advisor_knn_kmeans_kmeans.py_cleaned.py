import pandas as pd
import numpy as np
import random
import math
def fonk1(b2):
    return pd.read_csv(b2)
b1 = "san-francisco-ca"
b2 = f"b3/propertyInfo/{b1}.csv"
b3 = fonk1(b2)
b3["cluster"] = -1
def fonk2(b3, k, column_name):
    return [random.randint(1, b3[column_name].max()) for _ in range(k)]
b4 = fonk2(b3, 5, 'zestimate')
def fonk3(centroids, b3, column_name):
    b5 = b3[column_name]
    for x, centroid in enumerate(centroids):
        for idx, house in enumerate(b5):
            b6 = len(b5) * x
            b7 = np.asscalar(house.astype(int))
            b3.loc[idx + b6, 'cluster'] = centroid
fonk3(b4, b3, 'zestimate')
def fonk4(centroids, b3, column_name):
    b5 = b3[column_name]
    b8 = []
    for x, centroid in enumerate(centroids):
        b9 = []
        for idx, house in enumerate(b5):
            b6 = len(b5) * x
            b7 = np.asscalar(house.astype(int))
            b10 = math.sqrt(abs(b7 - centroid) ** 2)
            b9.append(b10)
        b11 = sum(b9) / len(b9)
        b8.append(b11)
    return b8
b12 = fonk4(b4, b3, 'zestimate')
def fonk5(b13, new_centroids):
    return all(abs(old - new) <= 1 for old, new in zip(b13, new_centroids))
while True:
    b13 = b4.copy()
    b4 = fonk2(b3, 5, 'zestimate')
    fonk3(b4, b3, 'zestimate')
    if fonk5(b13, b4):
        break
pd.set_option('display.max_rows', len(b3['zestimate']))
pd.set_option('display.float_format', lambda x: '%.0f' % x)
print(b3[['zestimate', 'cluster']])