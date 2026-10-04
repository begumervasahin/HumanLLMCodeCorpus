import sys
import pickle
import time
import numpy as np
from S3_BSTP import wild_bstp
from scipy.io import loadmat
LorR = sys.argv[1]
i = sys.argv[2]
input_dir  = 'data/'
interm_dir = 'res/' + LorR + 'vars/'
bstp_dir   = 'res/' + LorR + 'bstp/'
y_design = loadmat(input_dir + "img_data_"+LorR+".mat")['img_data']
if y_design.ndim==2:
  y_design = y_design[np.newaxis,:, :]
proj_y_design = 0*y_design
m = y_design.shape[0]
proj_mat = pickle.load(open(interm_dir+'proj_mat.dat','rb'))
for mii in range(m):
      proj_y_design[mii, :, :] = np.dot(proj_mat, np.squeeze(y_design[mii, :, :]))
print('The matrix dimension of image data is ' + str(y_design.shape))
img_size = np.loadtxt(input_dir + 'img_size.txt')
img_size = img_size.astype(int)
img_idx = np.loadtxt(input_dir + 'img_idx.txt')
img_idx = (img_idx-1).astype(int)
snp = np.loadtxt(input_dir + 'snp_data.txt')
efit_eta = pickle.load(open(interm_dir+'efit_eta.dat','rb'))
coord_data = pickle.load(open(interm_dir+'coord_data.dat','rb'))
h_opt = pickle.load(open(interm_dir+'h_opt.dat','rb'))
alpha = 0.005
alpha_log10 = -np.log10(alpha)
b_num = 25
g_num = 2000
start_3 = time.time()
max_gstat_bstp, max_lstat_bstp, max_area_bstp = wild_bstp(snp, proj_y_design, efit_eta, proj_mat, \
                                                coord_data, h_opt, img_size, img_idx, alpha_log10, g_num, b_num)
end_3 = time.time()
print('Elapsed time in wild_bstp is ', end_3 - start_3)
np.savetxt(bstp_dir + 'max_gstat_bstp_' + str(i), max_gstat_bstp)
np.savetxt(bstp_dir + 'max_lstat_bstp_' + str(i), max_lstat_bstp)
np.savetxt(bstp_dir + 'max_area_bstp_'  + str(i), max_area_bstp)