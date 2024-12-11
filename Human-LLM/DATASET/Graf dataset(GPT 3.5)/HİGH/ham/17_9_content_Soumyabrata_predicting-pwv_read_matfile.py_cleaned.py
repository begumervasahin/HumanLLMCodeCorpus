import numpy as np
import scipy.io
import math
import datetime
def read_matfile (matlab_file):
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
    b12 = []
    for i,item in enumerate(b11):
        if math.isnan(item):
            b12.append(i)
    b13 = []
    for i,item in enumerate(b5):
        if (item%5) !=0:
            b13.append(i)
    b14 = np.union1d(b12, b13)
    b11 = np.delete(b11, b14)
    b3 = np.delete(b3, b14)
    b4 = np.delete(b4, b14)
    b5 = np.delete(b5, b14)
    a1 = 2010
    b15 = []
    for i,item in enumerate(b3):
        b16 = datetime.datetime(a1, 1, 1) + datetime.timedelta(item - 1)
        b17 = datetime.datetime(b16.a1, b16.month, b16.day, int(b4[i]), int(b5[i]))
        b15.append(b17)
    print (len(b11))
    return (b15, b11)