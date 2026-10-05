import numpy as np
import scipy.io
import math
import datetime
def fonk1(matlab_file):
    b1 = scipy.io.loadmat(matlab_file)
    b2 = b1.get("DATA", [])
    num_samples, b3 = b2.shape
    b4 = b2[:, 0]
    b5 = b2[:, 1]
    b6 = b2[:, 2]
    b7 = b2[:, 3]
    b8 = b2[:, 4]
    b9 = b2[:, 5]
    b10 = b2[:, 6]
    b11 = b2[:, 7]
    b12 = b2[:, 12]
    b13 = [i for i, item in enumerate(b12) if math.isnan(item)]
    b14 = [i for i, item in enumerate(b6) if item % 5 != 0]
    b15 = np.union1d(b13, b14)
    b12 = np.delete(b12, b15)
    b4 = np.delete(b4, b15)
    b5 = np.delete(b5, b15)
    b6 = np.delete(b6, b15)
    a1 = 2010
    b16 = []
    for i, day in enumerate(b4):
        b17 = datetime.datetime(a1, 1, 1) + datetime.timedelta(day - 1)
        b18 = datetime.datetime(b17.a1, b17.month, b17.day, int(b5[i]), int(b6[i]))
        b16.append(b18)
    print(len(b12))
    return b16, b12