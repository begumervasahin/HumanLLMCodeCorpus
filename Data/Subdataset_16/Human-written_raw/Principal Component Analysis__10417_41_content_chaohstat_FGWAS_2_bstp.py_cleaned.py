import sys
import pickle
import time
import numpy as np
from S3_BSTP import wild_bstp
from scipy.io import loadmat
b1 = sys.argv[1]
b2 = sys.argv[2]
b3 = 'data/'
b4 = 'res/' + b1 + 'vars/'
b5 = 'res/' + b1 + 'bstp/'
b6 = loadmat(b3 + "img_data_"+b1+".mat")['img_data']
if b6.b7 = =2:
  b6 = b6[np.newaxis,:, :]
b8 = 0*b6
b9 = b6.shape[0]
b10 = pickle.load(open(b4+'b10.dat','rb'))
for mii in range(b9):
      b8[mii, :, :] = np.dot(b10, np.squeeze(b6[mii, :, :]))
print('The matrix dimension of image data is ' + str(b6.shape))
b11 = np.loadtxt(b3 + 'b11.txt')
b11 = b11.astype(int)
b12 = np.loadtxt(b3 + 'b12.txt')
b12 = (b12-1).astype(int)
b13 = np.loadtxt(b3 + 'snp_data.txt')
b14 = pickle.load(open(b4+'b14.dat','rb'))
b15 = pickle.load(open(b4+'b15.dat','rb'))
b16 = pickle.load(open(b4+'b16.dat','rb'))
a1 = 0.005
b17 = -np.log10(a1)
a2 = 25
a3 = 2000
b18 = time.time()
max_gstat_bstp, max_lstat_bstp, b19 = wild_bstp(b13, b8, b14, b10, \
                                                b15, b16, b11, b12, b17, a3, a2)
b20 = time.time()
print('Elapsed time in wild_bstp is ', b20 - b18)
np.savetxt(b5 + 'max_gstat_bstp_' + str(b2), max_gstat_bstp)
np.savetxt(b5 + 'max_lstat_bstp_' + str(b2), max_lstat_bstp)
np.savetxt(b5 + 'max_area_bstp_'  + str(b2), b19)