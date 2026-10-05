import pandas as pd
import numpy as np
import random
def fonk1(b3):
    return pd.fonk1(b3)
def fonk2(b4, a1, column_name):
    return random.sample(range(1, b4[column_name].max() + 1), a1)
def fonk3(b5, b4, column_name):
    for idx, house in enumerate(b4[column_name]):
        b1 = min(b5, key=lambda x: abs(house - x))
        b4.at[idx, 'cluster'] = b1
def fonk4(b6, new_centroids):
    return all(abs(old - new) <= 1 for old, new in zip(b6, new_centroids))
b2 = "san-francisco-ca"
b3 = f"b4/propertyInfo/{b2}.csv"
b4 = fonk1(b3)
b4["cluster"] = -1
a1 = 5
b5 = fonk2(b4, a1, 'zestimate')
while True:
    b6 = b5.copy()
    b5 = fonk2(b4, a1, 'zestimate')
    fonk3(b5, b4, 'zestimate')
    if fonk4(b6, b5):
        break
pd.set_option('display.max_rows', len(b4['zestimate']))
pd.set_option('display.float_format', lambda x: '%.0f' % x)
print(b4[['zestimate', 'cluster']])