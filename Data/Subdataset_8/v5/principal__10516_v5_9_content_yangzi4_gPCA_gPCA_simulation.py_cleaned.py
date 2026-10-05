import os
import random
import numpy as np
import matplotlib.pyplot as plt
D_range = range(1, 5)
Dest, Pval, save_data = 1, 1, 0
grp_N, M = 13, 16
K = 3
sigma = 0.1
n_vars = 1
alpha_range = np.arange(0, 1.01, 0.1)
def generate_group_data(dims_d, D_t, sigma, H):
    pass
def gPCA_selection(X_cd, D_range, version):
    pass
for gen_seed in range(25):
    Dest_listlist = []
    Pval_listlist = []
    for param in [1, 2, 3, 4]:
        D_t = param
        dims_c = [grp_N * K, M]
        dims_d = [[grp_N] * K, M]
        d_weight = np.diag([1] * D_t)
        signal = np.hstack([np.eye(D_t)[:, d:(d + 1)] for d in range(D_t)] * n_vars)
        w_c = d_weight.dot(np.hstack((signal, np.zeros((D_t, M - D_t * n_vars)))) / np.sqrt(n_vars))
        w_d = [d_weight.dot(np.hstack([np.zeros((D_t, D_t * n_vars))] * (k + 1) + [signal] +
                                      [np.zeros((D_t, M - D_t * n_vars * (k + 2)))]) / np.sqrt(n_vars)) for k in
               range(K)]
        Dest_list = []
        Pval_list = []
        print('___', grp_N, K, M, D_t, sigma, n_vars, '___')
        for alpha in alpha_range:
            if not (Dest or Pval):
                continue
            random.seed(gen_seed)
            w_cd = [alpha * w_c + np.sqrt(1 - alpha ** 2) * w_d[k] for k in range(K)]
            X_cd_ = generate_group_data(dims_d, D_t, sigma, H_=w_cd)
            X_cd, X_cd_ne, X_cd_e = X_cd_[0], [X_cd_[1][k].dot(X_cd_[2][k]) for k in range(K)], X_cd_[3]
            if save_data:
                for k in range(K):
                    np.savetxt('data/data(%dx%d)x%d_a%dD%ds%d_%d.txt' %
                               (grp_N, M, k, int(alpha * 100), D_t, int(sigma * 100), gen_seed), X_cd[k])
            random.seed(1)
            res_gPCA = gPCA_selection(X_cd, D_range=D_range, version=1)
            Dest_list.append([
                D_t == D_range[res_gPCA[3]],
                D_range[res_gPCA[3]],
            ])
            if Dest:
                print('Dest:', Dest_list[-1])
            Pval_list.append([
                res_gPCA[1][res_gPCA[3]],
                calc_alpha_pval(res_gPCA[1][res_gPCA[3]], M, D_range[res_gPCA[3]]),
                calc_alpha_pval2(res_gPCA[1][res_gPCA[3]], X_cd, D_range[res_gPCA[3]])[0]
            ] * 2)
            if Pval:
                print('Pval:', np.around(np.array(Pval_list[-1]), 3))
        Dest_listlist.append(Dest_list)
        Pval_listlist.append(Pval_list)
    if Dest:
        np.save('Dest(%dx%d)x%d_D%ds%d_%d' % (grp_N, M, K, D_t, int(sigma * 100), gen_seed),
                np.array(Dest_listlist))
    if Pval:
        np.save('Pval(%dx%d)x%d_D%ds%d_%d' % (grp_N, M, K, D_t, int(sigma * 100), gen_seed),
                np.array(Pval_listlist))
def plot_dest(p1, p2, p3, p4, svfg=0, v_='', optn=0, lgnd=0):
    pass
def plot_pval(p1, p2, p3, p4, svfg=0, v_='', optn=0, lgnd=0):
    pass
gen_seed_list = np.array(range(25))
n_s = float(len(gen_seed_list))
if 1:
    plt.close('all')
    svfg = 1
    plot_dest(13, 16, 3, 0.1, svfg, '', '(a)', 1)
    plot_pval(13, 16, 3, 0.1, svfg, '', '(b)', 1)