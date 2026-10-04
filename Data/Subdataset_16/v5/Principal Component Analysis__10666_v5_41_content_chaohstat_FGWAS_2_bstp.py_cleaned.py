import sys
import pickle
import time
import numpy as np
from S3_BSTP import wild_bstp
from scipy.io import loadmat
def fonk1(b12, b20, b13):
    b1 = loadmat(f'{b12}img_data_{b20}.mat')['img_data']
    if b1.b2 = = 2:
        b1 = b1[np.newaxis, :, :]
    with open(f'{b13}b3.dat', 'rb') as f:
        b3 = pickle.load(f)
    b4 = np.loadtxt(f'{b12}b4.txt').astype(int)
    b5 = (np.loadtxt(f'{b12}b5.txt') - 1).astype(int)
    b6 = np.loadtxt(f'{b12}snp_data.txt')
    with open(f'{b13}b7.dat', 'rb') as f:
        b7 = pickle.load(f)
    with open(f'{b13}b8.dat', 'rb') as f:
        b8 = pickle.load(f)
    with open(f'{b13}b9.dat', 'rb') as f:
        b9 = pickle.load(f)
    return b1, b3, b4, b5, b6, b7, b8, b9
def fonk2(b1, b3):
    b10 = b1.shape[0]
    b11 = np.zeros_like(b1)
    for mii in range(b10):
        b11[mii, :, :] = np.dot(b3, np.squeeze(b1[mii, :, :]))
    return b11
def fonk3(b14, b21, max_gstat_bstp, max_lstat_bstp, b17):
    np.savetxt(f'{b14}max_gstat_bstp_{b21}', max_gstat_bstp)
    np.savetxt(f'{b14}max_lstat_bstp_{b21}', max_lstat_bstp)
    np.savetxt(f'{b14}max_area_bstp_{b21}', b17)
def fonk4(b20, b21):
    b12 = 'data/'
    b13 = f'res/{b20}vars/'
    b14 = f'res/{b20}bstp/'
    b1, b3, b4, b5, b6, b7, b8, b9 = fonk1(b12, b20, b13)
    b11 = fonk2(b1, b3)
    print(f'The matrix dimension of image data is {b1.shape}')
    a1 = 0.005
    b15 = -np.log10(a1)
    a2 = 25
    a3 = 2000
    b16 = time.time()
    max_gstat_bstp, max_lstat_bstp, b17 = wild_bstp(
        b6, b11, b7, b3, b8, b9,
        b4, b5, b15, a3, a2
    )
    b18 = time.time()
    print(f'Elapsed time in wild_bstp is {b18 - b16}')
    fonk3(b14, b21, max_gstat_bstp, max_lstat_bstp, b17)
if b19 = = "__main__":
    b20 = sys.argv[1]
    b21 = sys.argv[2]
    fonk4(b20, b21)