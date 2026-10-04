
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
    return [random.randint(1, house_data[column_name].max()) for b15 in range(k)]
b4 = fonk1(b3, 5, 'zestimate')
def fonk2(b13, house_data, column_name):
    b5 = house_data[column_name].values
    b6 = []
    house_data['cluster'] = -1
    for centroid in b13:
        b7 = [
            math.sqrt((home - centroid)**2) for home in b5
        ]
        house_data.loc[house_data[column_name].apply(lambda x: math.sqrt((x - centroid)**2)).idxmin(), 'cluster'] = centroid
        b6.append(sum(b7))
    b8 = [dist / len(b5) for dist in b6]
    return house_data, b8
b3, b9 = fonk2(b4, b3, 'zestimate')
def fonk3(b14, current_centroids, b10 = 1.0):
    for old, new in zip(b14, current_centroids):
        if abs(old - new) > b10:
            return False
    return True
def fonk4(house_data, column_name):
    b11 = house_data.groupby('cluster')[column_name].mean().tolist()
    return b11
def fonk5(house_data, k, column_name, b12 = 100):
    b13 = fonk1(house_data, k, column_name)
    for b15 in range(b12):
        b14 = b13
        house_data, b15 = fonk2(b13, house_data, column_name)
        b13 = fonk4(house_data, column_name)
        if fonk3(b14, b13):
            break
    return b13
b16 = fonk5(b3, 5, 'zestimate')
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.0f' % x)
print("Final b13:", b16)
print("Clustered Data:")
print(b3)