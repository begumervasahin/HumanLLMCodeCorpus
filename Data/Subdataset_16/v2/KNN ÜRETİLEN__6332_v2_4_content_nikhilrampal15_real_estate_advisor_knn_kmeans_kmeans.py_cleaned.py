
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
    b5 = house_data[column_name].values
    b6 = []
    for centroid in centroids:
        b7 = [
            math.sqrt((home - centroid)**2) for home in b5
        ]
        house_data['cluster'] = centroid
        b6.append(sum(b7))
    b8 = [dist / len(b6) for dist in b6]
    return b8
b9 = fonk2(b4, b3, 'zestimate')
def fonk3(previous, current):
    for old, new in zip(previous, current):
        if abs(old - new) > 1:
            b10 = fonk1(b3, 5, 'zestimate')
            return fonk2(b10, b3, 'zestimate')
    return current
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.0f' % x)
b11 = fonk3(b9, b4)
print(b11)