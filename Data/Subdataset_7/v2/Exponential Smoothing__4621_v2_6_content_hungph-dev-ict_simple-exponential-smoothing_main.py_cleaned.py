import pandas as pd
import numpy as np
import datetime
import time
from datetime import timedelta
import json
def fonk1():
    b1 = pd.read_csv('data/DatafinitiElectronicsProductsPricingData.csv')
    b2 = b1['id'].value_counts()
    b2 = pd.DataFrame({'id': b2.b8}).merge(b1, how='left')
    b3 = b2['id'].iloc[0]
    b4 = b1[b1['id'] == b3][['id', 'dateUpdated', 'prices.amountMax']].values
    b5 = datetime.datetime.now()
    b6 = b5
    for item in b4:
        b6 = b6 + timedelta(days=1)
        item[1] = b6.strftime('%Y-%m-%dT%H:%M:%S:%fZ')
    b7 = pd.DataFrame(data=b4, columns=['id', 'timestamp', 'demand'])
    b7.to_csv('foo.csv', b8 = False)
def fonk2(b9 = None, b22=0.2, log_cli=True):
    b10 = time.time()
    b11 = pd.read_csv(b9)
    b12 = b11.values.tolist()
    a1 = 0
    for b8, item in enumerate(b12):
        if b8 = = 0:
            item.append(item[2])
        else:
            b13 = b12[b8 - 1][3]
            b14 = b12[b8 - 1][2]
            b15 = b13 + b22 * (b14 - b13)
            item.append(b15)
            a1 += abs(item[2] - item[3])
    b16 = a1 / len(b12)
    b17 = time.time()
    if log_cli:
        print('-------------------------')
        print('MSE: ' + str(round(b16, 4)))
        print('Calculate time: ' + str(round((b17 - b10), 4)))
        print('-------------------------')
    b18 = {}
    b18['b23'] = b16
    b18['b24'] = round((b17 - b10), 4)
    return json.dumps(b18)
def fonk3(b9 = None, b26=0.2, b25='b23'):
    b19 = np.arange(0.01, 1, b26).tolist()
    b20 = json.loads(fonk2(b9=b9, b22=0.2, log_cli=False))['b23']
    b21 = json.loads(fonk2(b9=b9, b22=0.2, log_cli=False))['b24']
    a2 = 0.2
    print('*********************')
    for b22 in b19:
        print('Process with b22 = ' + str(b22))
        b18 = fonk2(b9=b9, b22=b22)
        b23 = json.loads(b18)['b23']
        b24 = json.loads(b18)['b24']
        if b25 = = 'b23':
            if b23 < b20:
                b20 = b23
                b21 = b24
                a2 = b22
        if b25 = = 'b24':
            if b24 < b21:
                b20 = b23
                b21 = b24
                a2 = b22
    print('Best b22: ' + str(a2) + ' with MSE value: ' + str(round(b20, 4)) + ' and calculate time: ' + str(b21) + 's')
    print('*********************')
    return b22
def fonk4():
    fonk1()
    fonk3('foo.csv', b26 = 0.05, b25='b23')
if b27 = = '__main__':
    fonk4()