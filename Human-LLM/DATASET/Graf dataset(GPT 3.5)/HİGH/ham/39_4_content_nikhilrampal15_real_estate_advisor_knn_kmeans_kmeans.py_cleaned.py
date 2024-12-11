
import pandas as pd
import numpy as np
import random
from read_csvfile import read_csvfile
import math
b1 = "san-francisco-ca"
b2 = "b3/propertyInfo/{}.csv".format(b1)
b3 = read_csvfile(b2)
b3["cluster"] = -1
def fonk1(house_data,k,column_name):
    b4 = []
    pass
    for b18 in range(k):
        b4.append(random.randint(1,house_data[column_name].max()))
    return b4
b5 = fonk1(b3, 5,'zestimate')
def fonk2(centroids, house_data, column_name):
    b6 = []
    b7 = []
    b8 = house_data[column_name]
    for b18 in range(len(centroids)):
        b4 = centroids[b18]
        b9 = []
        for idx, y in enumerate(b8):
                b10 = len(b8) * b18
                b11 = b8[idx]
                b12 = np.asscalar(b11.astype(int))
                b6.append([math.sqrt(abs(b12-b4)**2), b4, y])
                b13 = math.sqrt(abs(b12-b4)**2)
                b9.append(b13)
                house_data.loc[idx + b10, 'cluster'] = b4
        b7.append(sum(b9))
    b14 = []
    for e in b7:
        b14.append(e/len(b7))
    return b14
b15 = fonk2(b5,b3,'zestimate')
def fonk3(param1, param2):
    b16 = list(map(int, param1))
    b17 = list(map(int, param2))
    for old in b16:
        for new in b17:
            if abs(b16[old] - b17[new]) > 1:
                fonk1(b3, 5, 'zestimate')
                fonk2(b5, b3, 'zestimate')
            else:
                return param2
pd.set_option('display.max_rows', len(b3['zestimate']))
b18 = b3['zestimate']
pd.set_option('display.float_format', lambda b18: '%.0f' % b18)
print(fonk3(b15, b5))