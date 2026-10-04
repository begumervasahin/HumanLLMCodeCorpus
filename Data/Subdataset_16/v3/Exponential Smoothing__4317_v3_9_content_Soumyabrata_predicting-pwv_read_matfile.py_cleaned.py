import numpy as np
import scipy.io
import math
import datetime
def fonk1(b7):
    b1 = scipy.io.loadmat(b7)
    b2 = b1.get("DATA", [])
    doy, hour, minute, b3 = b2[:, 0], b2[:, 1], b2[:, 2], b2[:, 12]
    b4 = np.union1d(
        np.where(np.isnan(b3))[0],
        np.where(minute % 5 != 0)[0]
    )
    doy, hour, minute, b3 = map(lambda x: np.delete(x, b4), [doy, hour, minute, b3])
    a1 = 2010
    b5 = [
        datetime.datetime(a1, 1, 1) + datetime.timedelta(b6 = int(day) - 1, hours=int(h), minutes=int(m))
        for day, h, m in zip(doy, hour, minute)
    ]
    print(f'Processed {len(b3)} valid PWV entries.')
    return b5, b3
def fonk2():
    b7 = './data/PWV_2010from_WS_2_withGradient.b1'
    b5, b3 = fonk1(b7)
    for ts, value in zip(b5[:5], b3[:5]):
        print(f'Timestamp: {ts}, PWV: {value}')
if b8 = = '__main__':
    fonk2()