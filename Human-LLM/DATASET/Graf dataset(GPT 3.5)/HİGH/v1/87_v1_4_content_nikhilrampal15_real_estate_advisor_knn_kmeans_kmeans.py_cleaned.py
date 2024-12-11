import pandas as pd
import numpy as np
import random
import math
def fonk1(b3):
    return pd.read_csv(b3)
def fonk2(house_data, k, column_name):
    b1 = []
    for b12 in range(k):
        b1.append(random.randint(1, house_data[column_name].max()))
    return b1
b2 = "san-francisco-ca"
b3 = "b4/propertyInfo/{}.csv".format(b2)
b4 = fonk1(b3)
b4["cluster"] = -1
b5 = fonk2(b4, 5, 'zestimate')
def fonk3(centroids, house_data, column_name):
    b6 = house_data[column_name]
    for b12 in range(len(centroids)):
        b1 = centroids[b12]
        for idx, y in enumerate(b6):
            b7 = len(b6) * b12
            b8 = b6[idx]
            b9 = np.asscalar(b8.astype(int))
            house_data.loc[idx + b7, 'cluster'] = b1
def fonk4(param1, param2):
    b10 = list(map(int, param1))
    b11 = list(map(int, param2))
    for old in b10:
        for new in b11:
            if abs(b10[old] - b11[new]) > 1:
                fonk2(b4, 5, 'zestimate')
                fonk3(b5, b4, 'zestimate')
            else:
                return param2
pd.set_option('display.max_rows', len(b4['zestimate']))
b12 = b4['zestimate']
pd.set_option('display.float_format', lambda b12: '%.0f' % b12)
fonk3(b5, b4, 'zestimate')
print(fonk4(b4['cluster'], b5))