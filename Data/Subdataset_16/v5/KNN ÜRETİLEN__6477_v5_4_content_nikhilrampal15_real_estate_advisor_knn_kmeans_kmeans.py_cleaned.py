
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
def fonk2(b11, house_data, column_name):
    b5 = []
    for centroid in b11:
        b6 = []
        for idx, house_value in house_data[column_name].items():
            b7 = math.sqrt(abs(house_value - centroid) ** 2)
            b6.append(b7)
            house_data.at[idx, 'cluster'] = centroid
        b5.append(sum(b6) / len(house_data))
    return b5
b8 = fonk2(b4, b3, 'zestimate')
def fonk3(b12, new_centroids, b9 = 1):
    return all(abs(old - new) <= b9 for old, new in zip(b12, new_centroids))
def fonk4(house_data, k, column_name, b10 = 100):
    b11 = fonk1(house_data, k, column_name)
    for _ in range(b10):
        b12 = b11
        b8 = fonk2(b11, house_data, column_name)
        b11 = [np.mean(house_data[house_data['cluster'] == centroid][column_name]) for centroid in b11]
        if fonk3(b12, b11):
            break
    return house_data
b13 = fonk4(b3, 5, 'zestimate')
print(b13)
pd.set_option('display.max_rows', len(b3['zestimate']))
pd.set_option('display.float_format', lambda x: '%.0f' % x)