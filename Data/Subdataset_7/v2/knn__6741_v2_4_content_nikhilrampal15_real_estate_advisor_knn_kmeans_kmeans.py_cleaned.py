import pandas as pd
import numpy as np
import random
def fonk1(b6):
    return pd.fonk1(b6)
def fonk2(b7, a1, column_name):
    b1 = []
    for _ in range(a1):
        b1.append(random.randint(1, b7[column_name].max()))
    return b1
def fonk3(b1, b7, column_name):
    for x in range(len(b1)):
        b2 = b1[x]
        for idx, house in enumerate(b7[column_name]):
            b3 = len(b7) * x
            b4 = np.asscalar(house.astype(int))
            b7.loc[idx + b3, 'cluster'] = b2
def fonk4(b9, new_centroids):
    for old, new in zip(b9, new_centroids):
        if abs(old - new) > 1:
            return False
    return True
b5 = "san-francisco-ca"
b6 = "b7/propertyInfo/{}.csv".format(b5)
b7 = fonk1(b6)
b7["cluster"] = -1
a1 = 5
b8 = fonk2(b7, a1, 'zestimate')
fonk3(b8, b7, 'zestimate')
while True:
    b9 = b8.copy()
    b8 = fonk2(b7, a1, 'zestimate')
    fonk3(b8, b7, 'zestimate')
    if fonk4(b9, b8):
        break
pd.set_option('display.max_rows', len(b7['zestimate']))
pd.set_option('display.float_format', lambda x: '%.0f' % x)
print(b7[['zestimate', 'cluster']])