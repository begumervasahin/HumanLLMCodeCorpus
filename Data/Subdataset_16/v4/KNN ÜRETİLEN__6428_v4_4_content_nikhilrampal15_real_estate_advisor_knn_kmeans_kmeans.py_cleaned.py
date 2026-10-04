
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
    b4 = [random.randint(1, house_data[column_name].max()) for _ in range(k)]
    return b4
b5 = fonk1(b3, 5, 'zestimate')
def fonk2(b4, house_data, column_name):
    b6 = []
    for centroid in b4:
        b7 = []
        for idx, house_value in house_data[column_name].items():
            b8 = math.sqrt(abs(house_value - centroid) ** 2)
            b7.append(b8)
            house_data.at[idx, 'cluster'] = centroid
        b6.append(sum(b7))
    b9 = [total / len(house_data) for total in b6]
    return b9
b10 = fonk2(b5, b3, 'zestimate')
def fonk3(b11, b12):
    b11 = list(map(int, b11))
    b12 = list(map(int, b12))
    for old, new in zip(b11, b12):
        if abs(old - new) > 1:
            b12 = fonk1(b3, 5, 'zestimate')
            return fonk2(b12, b3, 'zestimate')
    return b12
pd.set_option('display.max_rows', len(b3['zestimate']))
pd.set_option('display.float_format', lambda x: '%.0f' % x)
print(fonk3(b10, b5))