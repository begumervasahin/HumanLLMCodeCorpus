import pandas as pd
import numpy as np
import datetime
import time
from datetime import timedelta
import json
def fonk1():
    b1 = pd.read_csv('data/DatafinitiElectronicsProductsPricingData.csv')
    b2 = b1['id'].value_counts().b8[0]
    b3 = b1[b1['id'] == b2][['id', 'dateUpdated', 'prices.amountMax']].values
    b4 = datetime.datetime.now()
    b5 = b4
    for item in b3:
        b5 += timedelta(b6 = 1)
        item[1] = b5.strftime('%Y-%m-%dT%H:%M:%S:%fZ')
    b7 = pd.DataFrame(data=b3, columns=['id', 'timestamp', 'demand'])
    b7.to_csv('foo.csv', b8 = False)
def fonk2(b9 = None, b23=0.2, log_cli=True):
    b10 = time.time()
    b11 = pd.read_csv(b9)
    b12 = b11.values.tolist()
    a1 = 0
    for b8, record in enumerate(b12):
        if b8 = = 0:
            record.append(record[2])
        else:
            b13 = b12[b8 - 1][3]
            b14 = b12[b8 - 1][2]
            b15 = b13 + b23 * (b14 - b13)
            record.append(b15)
            a1 += abs(record[2] - record[3])
    b16 = a1 / len(b12)
    b17 = time.time()
    if log_cli:
        print('-------------------------')
        print('MSE:', round(b16, 4))
        print('Calculate time:', round((b17 - b10), 4))
        print('-------------------------')
    b18 = {'b24': b16, 'b25': round((b17 - b10), 4)}
    return json.dumps(b18)
def fonk3(b9 = None, b27=0.2, b26='b24'):
    b19 = np.arange(0.01, 1, b27).tolist()
    b20 = json.loads(fonk2(b9=b9, b23=0.2, log_cli=False))
    b21 = b20['b24']
    b22 = b20['b25']
    a2 = 0.2
    print('*********************')
    for b23 in b19:
        print('Processing with b23 = ', b23)
        b18 = json.loads(fonk2(b9=b9, b23=b23))
        b24 = b18['b24']
        b25 = b18['b25']
        if b26 = = 'b24':
            if b24 < b21:
                b21 = b24
                b22 = b25
                a2 = b23
        if b26 = = 'b25':
            if b25 < b22:
                b21 = b24
                b22 = b25
                a2 = b23
    print('Best b23:', a2, 'with MSE value:', round(b21, 4), 'and calculate time:', b22, 's')
    print('*********************')
    return a2
def fonk4():
    fonk1()
    fonk3('foo.csv', b27 = 0.05, b26='b24')
if b28 = = '__main__':
    fonk4()