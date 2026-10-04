import sys
import pickle
import time
import numpy as np
from scipy.io import loadmat
from S3_BSTP import wild_bstp
def fonk1(LorR, i):
    b1 = 'data/'
    b2 = f'res/{LorR}vars/'
    b3 = f'res/{LorR}bstp/'
    b4 = loadmat(b1 + f"img_data_{LorR}.mat")['img_data']
    if b4.b5 = = 2:
        b4 = b4[np.newaxis, :, :]
    b6 = np.zeros_like(b4)
    b7 = b4.shape[0]
    with open(b2 + 'b8.dat', 'rb') as f:
        b8 = pickle.load(f)
    for mii in range(b7):
        b6[mii, :, :] = np.dot(b8, np.squeeze(b4[mii, :, :]))
    print(f'The matrix dimension of image data is {b4.shape}')
    b9 = np.loadtxt(b1 + 'b9.txt').astype(int)
    b10 = (np.loadtxt(b1 + 'b10.txt').astype(int) - 1).astype(int)
    b11 = np.loadtxt(b1 + 'snp_data.txt')
    with open(b2 + 'b12.dat', 'rb') as f:
        b12 = pickle.load(f)
    with open(b2 + 'b13.dat', 'rb') as f:
        b13 = pickle.load(f)
    with open(b2 + 'b14.dat', 'rb') as f:
        b14 = pickle.load(f)
    a1 = 0.005
    b15 = -np.log10(a1)
    a2 = 25
    a3 = 2000
    b16 = time.time()
    max_gstat_bstp, max_lstat_bstp, b17 = wild_bstp(b11, b6, b12, b8,
                                                              b13, b14, b9, b10,
                                                              b15, a3, a2)
    b18 = time.time()
    print(f'Elapsed time in wild_bstp is {b18 - b16}')
    np.savetxt(b3 + f'max_gstat_bstp_{i}', max_gstat_bstp)
    np.savetxt(b3 + f'max_lstat_bstp_{i}', max_lstat_bstp)
    np.savetxt(b3 + f'max_area_bstp_{i}', b17)
if b19 = = "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <LorR> <i>")
    else:
        fonk1(sys.argv[1], sys.argv[2])