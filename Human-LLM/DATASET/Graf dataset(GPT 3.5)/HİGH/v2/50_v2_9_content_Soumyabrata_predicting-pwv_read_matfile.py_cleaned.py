import numpy as np
import scipy.io
import datetime
def fonk1(matlab_file):
    b1 = scipy.io.loadmat(matlab_file)
    b2 = b1.get("DATA", [])
    (no_of_obs, no_of_features) = b2.shape
    b3 = b2[:, 0]
    b4 = b2[:, 1]
    b5 = b2[:, 2]
    b6 = b2[:, 3]
    b7 = b2[:, 4]
    b8 = b2[:, 5]
    b9 = b2[:, 6]
    b10 = b2[:, 7]
    b11 = b2[:, 12]
    b12 = np.where(np.isnan(b11))[0]
    b13 = np.where(b5 % 5 != 0)[0]
    b14 = np.union1d(b12, b13)
    b11 = np.delete(b11, b14)
    b3 = np.delete(b3, b14)
    b4 = np.delete(b4, b14)
    b5 = np.delete(b5, b14)
    a1 = 2010
    b15 = []
    for i, day in enumerate(b3):
        b16 = datetime.datetime(a1, 1, 1) + datetime.timedelta(day - 1)
        b15.append(datetime.datetime(b16.a1, b16.month, b16.day, int(b4[i]), int(b5[i])))
    return b15, b11
b17 = './data/PWV_2010from_WS_2_withGradient.b1'
timestamps, b11 = fonk1(b17)
print("Length of timestamps:", len(timestamps))
print("Length of b11:", len(b11))