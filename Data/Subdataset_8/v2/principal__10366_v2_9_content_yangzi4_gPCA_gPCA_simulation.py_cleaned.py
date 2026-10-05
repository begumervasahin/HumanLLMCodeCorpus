import os
import random
import numpy as np
import matplotlib.pyplot as plt
def main():
    D_range = range(1, 5)
    Dest, Pval, save_data = 1, 1, 0
    gen_seed_list = range(25)
    n_s = float(len(gen_seed_list))
    alpha_range = np.arange(0, 1.01, 0.1)
    plt.close('all')
    plot_Dest(13, 16, 3, 0.1, svfg=1, v_='', optn='(a)', lgnd=1)
    plot_Pval(13, 16, 3, 0.1, svfg=1, v_='', optn='(b)', lgnd=1)
def plot_Dest(p1, p2, p3, p4, svfg_=0, v_='', optn=0, lgnd=0):
    param_list = [1, 2, 3, 4]
    for param in param_list:
        grp_N, M = p1, p2
        K = p3
        D_t = param
        sigma_ = p4
    vals_m = np.zeros((len(param_list), len(alpha_range), 6))
    for g_seed in gen_seed_list:
        vals_m += np.load('Dest%s(%dx%d)x%d_D%ds%d_%d.npy' % (
            v_, grp_N, M, K, D_t, sigma_*100, g_seed))
    vals = vals_m / n_s
    vals_sd = np.zeros((len(param_list), len(alpha_range), 6))
    for g_seed in gen_seed_list:
        load_ = np.load('Dest%s(%dx%d)x%d_D%ds%d_%d.npy' % (
            v_, grp_N, M, K, D_t, sigma_*100, g_seed))
        vals_sd += (load_ - vals) ** 2
    vals2 = vals_sd / n_s
    for i in range(6):
        print('\t'.join(list(np.around(np.mean(vals[:, :, i], axis=0), 2).astype(str))))
    plt.figure()
    plt.subplot(1, 1, 1)
    for i, color in enumerate(['c', 'b', 'r', 'g', 'k']):
        plt.plot(alpha_range, np.mean(vals[:, :, i], axis=0), color + '*', ms=12)
        plt.errorbar(alpha_range, np.mean(vals[:, :, i], axis=0),
                     yerr=np.sqrt(np.mean(vals2[:, :, i], axis=0)) / np.sqrt(n_s), color=color, ms=12)
        plt.plot(alpha_range, np.mean(vals[:, :, i], axis=0), color + '--', ms=12)
    plt.xlabel(r'$\alpha$', fontsize=16)
    plt.ylim(-0.1, 1.1)
    if lgnd:
        plt.legend(['gPCA', 'JIVE', 'LP', 'BIC', 'KG', 'KN'], loc='upper left', fontsize=16)
    plt.title('%s: Proportion of correct rank selections' % optn, fontsize=16)
    if svfg_:
        plt.savefig('Dest%s(%dx%d)x%d_D%ds%d_all%d.png' % (v_, grp_N, M, K,
            D_t, sigma_*100, gen_seed_list[-1]), format='png', bbox_inches='tight')
    plt.show()
def plot_Pval(p1, p2, p3, p4, svfg_=0, v_='', optn=0, lgnd=0):
    param_list = [1, 2, 3, 4]
    for param in param_list:
        grp_N, M = p1, p2
        K = p3
        D_t = param
        sigma_ = p4
    vals_m = np.zeros((len(param_list), len(alpha_range), 6))
    for g_seed in gen_seed_list:
        vals_m += np.load('Pval%s(%dx%d)x%d_D%ds%d_%d.npy' % (
            v_, grp_N, M, K, D_t, sigma_*100, g_seed))
    vals = vals_m / n_s
    vals_sd = np.zeros((len(param_list), len(alpha_range), 6))
    for g_seed in gen_seed_list:
        load_ = np.load('Pval%s(%dx%d)x%d_D%ds%d_%d.npy' % (
            v_, grp_N, M, K, D_t, sigma_*100, g_seed))
        vals_sd += (load_ - vals) ** 2
    vals2 = np.sqrt(vals_sd / n_s)
    for i in range(6):
        print('\t'.join(list(np.around(np.mean(vals[:, :, i], axis=0), 2).astype(str))))
    plt.figure()
    plt.subplot(1, 1, 1)
    for i, color in enumerate(['c', 'b', 'r', 'g', 'k']):
        plt.plot(alpha_range, np.mean(vals[:, :, i], axis=0), color + '*', ms=12)
        plt.errorbar(alpha_range, np.mean(vals[:, :, i], axis=0),
                     yerr=np.sqrt(np.mean(vals2[:, :, i], axis=0)) / np.sqrt(n_s), color=color, ms=12)
        plt.plot(alpha_range, np.mean(vals[:, :, i], axis=0), color + '--', ms=12)
    plt.xlabel(r'$\alpha$', fontsize=16)
    plt.ylim(-0.1, 1.1)
    if lgnd:
        plt.legend([r'$\alpha$', r'$p_{\alpha 1}$',  r'$p_{\alpha 2}$',
                    r'$\alpha$', r'$p_{\alpha 1}$',  r'$p_{\alpha 2}$'],
                   loc='upper left', fontsize=16)
    plt.title('%s: alpha, p_alpha1, p_alpha2' % optn, fontsize=16)
    if svfg_:
        plt.savefig('Pval%s(%dx%d)x%d_D%ds%d_all%d.png' % (v_, grp_N, M, K,
            D_t, sigma_*100, gen_seed_list[-1]), format='png', bbox_inches='tight')
    plt.show()
if __name__ == "__main__":
    main()