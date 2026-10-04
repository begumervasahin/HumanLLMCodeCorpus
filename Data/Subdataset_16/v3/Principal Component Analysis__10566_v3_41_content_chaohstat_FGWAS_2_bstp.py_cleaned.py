import sys
import pickle
import time
import numpy as np
from scipy.io import loadmat
from S3_BSTP import wild_bstp
def fonk1(b11, b12):
    b1 = loadmat(b11 + "img_data_" + b19 + ".mat")['img_data']
    if b1.b2 = = 2:
        b1 = b1[np.newaxis, :, :]
    b3 = pickle.load(open(b12 + 'b3.dat', 'rb'))
    b4 = pickle.load(open(b12 + 'b4.dat', 'rb'))
    b5 = pickle.load(open(b12 + 'b5.dat', 'rb'))
    b6 = pickle.load(open(b12 + 'b6.dat', 'rb'))
    b7 = np.loadtxt(b11 + 'b7.txt').astype(int)
    b8 = (np.loadtxt(b11 + 'b8.txt').astype(int) - 1).astype(int)
    b9 = np.loadtxt(b11 + 'snp_data.txt')
    return b1, b3, b4, b5, b6, b7, b8, b9
def fonk2(b1, b3):
    b10 = np.zeros_like(b1)
    for mii in range(b1.shape[0]):
        b10[mii, :, :] = np.dot(b3, np.squeeze(b1[mii, :, :]))
    return b10
def fonk3(b13, b20, max_gstat_bstp, max_lstat_bstp, b16):
    np.savetxt(b13 + f'max_gstat_bstp_{b20}', max_gstat_bstp)
    np.savetxt(b13 + f'max_lstat_bstp_{b20}', max_lstat_bstp)
    np.savetxt(b13 + f'max_area_bstp_{b20}', b16)
def fonk4(b19, b20):
    b11 = 'data/'
    b12 = f'res/{b19}vars/'
    b13 = f'res/{b19}bstp/'
    b1, b3, b4, b5, b6, b7, b8, b9 = fonk1(b11, b12)
    b10 = fonk2(b1, b3)
    print(f'The matrix dimension of image data is {b1.shape}')
    a1 = 0.005
    b14 = -np.log10(a1)
    a2 = 25
    a3 = 2000
    b15 = time.time()
    max_gstat_bstp, max_lstat_bstp, b16 = wild_bstp(
        b9, b10, b4, b3, b5, b6, b7, b8, b14, a3, a2
    )
    b17 = time.time()
    print(f'Elapsed time in wild_bstp is {b17 - b15} seconds')
    fonk3(b13, b20, max_gstat_bstp, max_lstat_bstp, b16)
if b18 = = "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <b19> <b20>")
    else:
        b19 = sys.argv[1]
        b20 = sys.argv[2]
        fonk4(b19, b20)