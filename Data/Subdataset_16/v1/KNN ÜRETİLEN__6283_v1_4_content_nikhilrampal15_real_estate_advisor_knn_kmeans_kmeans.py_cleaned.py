
import pandas as pd
import numpy as np
import random
import math
from read_csvfile import read_csvfile
b1 = "san-francisco-ca"
b2 = f"b3/propertyInfo/{b1}.csv"
b3 = read_csvfile(b2)
b3["cluster"] = -1
def fonk1(house_data, k, column_name):
    return [random.randint(1, house_data[column_name].max()) for _ in range(k)]
b4 = fonk1(b3, 5, 'zestimate')
def fonk2(centroids, house_data, column_name):
    b5 = []
    b6 = []
    b7 = house_data[column_name].values
    for x, centroid in enumerate(centroids):
        b8 = []
        for idx, home in enumerate(b7):
            b9 = int(home)
            b10 = math.sqrt(abs(b9 - centroid)**2)
            b8.append(b10)
            house_data.loc[idx, 'cluster'] = centroid
        b6.append(sum(b8))
    b11 = [e / len(b6) for e in b6]
    return b11
b12 = fonk2(b4, b3, 'zestimate')
def fonk3(param1, param2):
    b13 = list(map(int, param1))
    b14 = list(map(int, param2))
    for old, new in zip(b13, b14):
        if abs(old - new) > 1:
            b15 = fonk1(b3, 5, 'zestimate')
            return fonk2(b15, b3, 'zestimate')
    return param2
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.0f' % x)
print(fonk3(b12, b4))