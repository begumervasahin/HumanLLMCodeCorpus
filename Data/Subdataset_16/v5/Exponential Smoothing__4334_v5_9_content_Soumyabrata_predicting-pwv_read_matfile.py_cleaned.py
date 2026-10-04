import numpy as np
import scipy.io
import math
import datetime
def fonk1(b12):
    b1 = scipy.io.loadmat(b12)
    b2 = b1.get("DATA", [])
    b3 = b2[:, 0]
    b4 = b2[:, 1]
    b5 = b2[:, 2]
    b6 = b2[:, 12]
    b7 = [i for i, value in enumerate(b6) if math.isnan(value)]
    b8 = [i for i, value in enumerate(b5) if value % 5 != 0]
    b9 = np.union1d(b7, b8)
    b6 = np.delete(b6, b9)
    b3 = np.delete(b3, b9)
    b4 = np.delete(b4, b9)
    b5 = np.delete(b5, b9)
    a1 = 2010
    b10 = [
        datetime.datetime(a1, 1, 1) + datetime.timedelta(b11 = int(day) - 1, hours=int(h), minutes=int(m))
        for day, h, m in zip(b3, b4, b5)
    ]
    print(f'Processed {len(b6)} valid PWV entries.')
    return b10, b6
def fonk2():
    b12 = './data/PWV_2010from_WS_2_withGradient.b1'
    b10, b6 = fonk1(b12)
    for ts, value in zip(b10[:5], b6[:5]):
        print(f'Timestamp: {ts}, PWV: {value}')
if b13 = = '__main__':
    fonk2()