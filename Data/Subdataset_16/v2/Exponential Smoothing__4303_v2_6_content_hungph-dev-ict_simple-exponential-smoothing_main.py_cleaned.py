import pandas as pd
import numpy as np
import datetime
from datetime import timedelta
import time
import json
def fonk1(file_path, b1 = 'processed_data.csv'):
    b2 = pd.read_csv(file_path)
    b3 = b2['id'].value_counts().idxmax()
    b4 = b2[b2['id'] == b3][['id', 'dateUpdated', 'prices.amountMax']].copy()
    b5 = datetime.datetime.now()
    for i in range(len(b4)):
        b4.iat[i, 1] = (b5 + timedelta(b6 = i)).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    b4.b7 = ['id', 'timestamp', 'demand']
    b4.to_csv(b1, b8 = False)
def fonk2(file_path, b9 = 0.2, log_cli=True):
    b10 = time.time()
    b11 = pd.read_csv(file_path)
    b12 = b11.values.tolist()
    a1 = 0
    for b8, item in enumerate(b12):
        if b8 = = 0:
            item.append(item[2])
        else:
            b13 = b12[b8 - 1][3]
            b14 = b12[b8 - 1][2]
            b15 = b13 + b9 * (b14 - b13)
            item.append(b15)
            a1 += abs(item[2] - item[3])
    b16 = a1 / len(b12)
    b17 = time.time()
    if log_cli:
        print('-------------------------')
        print(f'MAD: {b16:.4f}')
        print(f'Calculation time: {b17 - b10:.4f} seconds')
        print('-------------------------')
    b18 = {
        'b23': b16,
        'b24': round(b17 - b10, 4)
    }
    return json.dumps(b18)
def fonk3(file_path, b19 = 0.2, b25='b23'):
    b20 = np.arange(0.01, 1, b19)
    a2 = 0.2
    b21 = float('inf')
    b22 = float('inf')
    print('*********************')
    for b9 in b20:
        print(f'Processing with b9 = {b9}')
        b18 = json.loads(fonk2(file_path=file_path, b9=b9, log_cli=False))
        b23 = b18['b23']
        b24 = b18['b24']
        if b25 = = 'b23' and b23 < b21:
            b21 = b23
            b22 = b24
            a2 = b9
        if b25 = = 'b24' and b24 < b22:
            b21 = b23
            b22 = b24
            a2 = b9
    print(f'Best b9: {a2} with MSE value: {b21:.4f} and calculate time: {b22:.4f} seconds')
    print('*********************')
    return a2
if b26 = = '__main__':
    fonk1('data/DatafinitiElectronicsProductsPricingData.csv')
    fonk3('processed_data.csv', b19 = 0.05, b25='b23')