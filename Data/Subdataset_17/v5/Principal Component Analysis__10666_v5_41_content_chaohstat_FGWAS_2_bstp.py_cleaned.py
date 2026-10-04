import sys
import pickle
import time
import numpy as np
from S3_BSTP import wild_bstp
from scipy.io import loadmat
def load_data(input_dir, LorR, interm_dir):
    y_design = loadmat(f'{input_dir}img_data_{LorR}.mat')['img_data']
    if y_design.ndim == 2:
        y_design = y_design[np.newaxis, :, :]
    with open(f'{interm_dir}proj_mat.dat', 'rb') as f:
        proj_mat = pickle.load(f)
    img_size = np.loadtxt(f'{input_dir}img_size.txt').astype(int)
    img_idx = (np.loadtxt(f'{input_dir}img_idx.txt') - 1).astype(int)
    snp = np.loadtxt(f'{input_dir}snp_data.txt')
    with open(f'{interm_dir}efit_eta.dat', 'rb') as f:
        efit_eta = pickle.load(f)
    with open(f'{interm_dir}coord_data.dat', 'rb') as f:
        coord_data = pickle.load(f)
    with open(f'{interm_dir}h_opt.dat', 'rb') as f:
        h_opt = pickle.load(f)
    return y_design, proj_mat, img_size, img_idx, snp, efit_eta, coord_data, h_opt
def project_image_data(y_design, proj_mat):
    m = y_design.shape[0]
    proj_y_design = np.zeros_like(y_design)
    for mii in range(m):
        proj_y_design[mii, :, :] = np.dot(proj_mat, np.squeeze(y_design[mii, :, :]))
    return proj_y_design
def save_results(bstp_dir, i, max_gstat_bstp, max_lstat_bstp, max_area_bstp):
    np.savetxt(f'{bstp_dir}max_gstat_bstp_{i}', max_gstat_bstp)
    np.savetxt(f'{bstp_dir}max_lstat_bstp_{i}', max_lstat_bstp)
    np.savetxt(f'{bstp_dir}max_area_bstp_{i}', max_area_bstp)
def main(LorR, i):
    input_dir = 'data/'
    interm_dir = f'res/{LorR}vars/'
    bstp_dir = f'res/{LorR}bstp/'
    y_design, proj_mat, img_size, img_idx, snp, efit_eta, coord_data, h_opt = load_data(input_dir, LorR, interm_dir)
    proj_y_design = project_image_data(y_design, proj_mat)
    print(f'The matrix dimension of image data is {y_design.shape}')
    alpha = 0.005
    alpha_log10 = -np.log10(alpha)
    b_num = 25
    g_num = 2000
    start_time = time.time()
    max_gstat_bstp, max_lstat_bstp, max_area_bstp = wild_bstp(
        snp, proj_y_design, efit_eta, proj_mat, coord_data, h_opt,
        img_size, img_idx, alpha_log10, g_num, b_num
    )
    end_time = time.time()
    print(f'Elapsed time in wild_bstp is {end_time - start_time}')
    save_results(bstp_dir, i, max_gstat_bstp, max_lstat_bstp, max_area_bstp)
if __name__ == "__main__":
    LorR = sys.argv[1]
    i = sys.argv[2]
    main(LorR, i)