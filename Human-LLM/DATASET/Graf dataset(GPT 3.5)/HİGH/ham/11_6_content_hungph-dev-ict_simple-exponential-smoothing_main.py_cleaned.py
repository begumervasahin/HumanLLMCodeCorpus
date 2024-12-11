import pandas as pd
import numpy as np
import datetime
import time
from datetime import timedelta
import json
b1 = pd.read_csv('data/DatafinitiElectronicsProductsPricingData.csv')
b2 = b1['id'].value_counts()
b2 = pd.DataFrame({'id':b2.b8}).merge(b1, how='left')
b3 = b2['id'].iloc[0]
b4 = b1[b1['id'] == b3][['id', 'dateUpdated', 'prices.amountMax']].values
b5 = datetime.datetime.now()
b6 = b5
a1 = 0
for item in b4:
    b6 = b6 + timedelta(days=1)
    item[1] = b6.strftime('%Y-%m-%dT%H:%M:%S:%fZ')
b7 = pd.DataFrame(data=b4, columns=['id', 'timestamp', 'demand'])
b7.to_csv('foo.csv', b8 = False)
def fonk1(b9 = None, b23=0.2, b18=True):
    b10 = time.time()
    b11 = pd.read_csv(b9)
    b12 = b11.values.tolist()
    a2 = 0
    for b8, item in enumerate(b12):
        if b8 = = 0:
            item.append(item[2])
        else:
            b13 = b12[b8 - 1][3]
            b14 = b12[b8 - 1][2]
            b15 = b13 + b23*(b14 - b13)
            item.append(b15)
            a2 += abs(item[2] - item[3])
    b16 = a2/len(b12)
    b17 = time.time()
    if b18 = = True:
        print('-------------------------')
        print('MSE: ' + str(round(b16,4)))
        print('Calculate time: ' + str(round((b17 - b10), 4)))
        print('-------------------------')
    b19 = {}
    b19['b24'] = b16
    b19['b25'] = round((b17 - b10), 4)
    return json.dumps(b19)
def fonk2(b9 = None, b27=0.2, b26='b24'):
    b20 = np.arange(0.01, 1, b27).tolist()
    b21 = json.loads(fonk1(b9=b9, b23=0.2, b18=False))['b24']
    b22 = json.loads(fonk1(b9=b9, b23=0.2, b18=False))['b25']
    a3 = 0.2
    print('*********************')
    for b23 in b20:
        print('Process with b23 = ' + str(b23))
        b19 = fonk1(b9=b9, b23=b23)
        b24 = json.loads(b19)['b24']
        b25 = json.loads(b19)['b25']
        if b26 = = 'b24':
            if b24 < b21:
                b21 = b24
                b22 = b25
                a3 = b23
        if b26 = = 'b25':
            if b25 < b22:
                b21 = b24
                b22 = b25
                a3 = b23
    print('Best b23: ' + str(a3) + ' with MSE value: ' + str(round(b21,4)) + ' and calculate time: ' + str(b22) + 's')
    print('*********************')
    return b23
fonk2('foo.csv', b27 = 0.05, b26='b24')