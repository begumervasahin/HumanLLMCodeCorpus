import os
import numpy as np
import matplotlib.pyplot as plt
def fonk1():
    b1 = range(1, 5)
    Dest, Pval, b2 = 1, 1, 0
    b3 = range(25)
    b4 = float(len(b3))
    b5 = np.arange(0, 1.01, 0.1)
    plt.close('all')
    fonk2(13, 16, 3, 0.1, b6 = 1, v_='', optn='(a)', lgnd=1, data_type='Dest')
    fonk2(13, 16, 3, 0.1, b6 = 1, v_='', optn='(b)', lgnd=1, data_type='Pval')
def fonk2(p1, p2, p3, p4, b7 = 0, v_='', optn=0, lgnd=0, data_type='Dest'):
    b8 = [1, 2, 3, 4]
    for param in b8:
        grp_N, b9 = p1, p2
        b10 = p3
        b11 = param
        b12 = p4
    b13 = np.zeros((len(b8), len(b5), 6))
    for g_seed in b3:
        b13 += np.load('%s%s(%dx%d)x%d_D%ds%d_%d.npy' % (
            data_type, v_, grp_N, b9, b10, b11, b12*100, g_seed))
    b14 = b13 / b4
    b15 = np.zeros((len(b8), len(b5), 6))
    for g_seed in b3:
        b16 = np.load('%s%s(%dx%d)x%d_D%ds%d_%d.npy' % (
            data_type, v_, grp_N, b9, b10, b11, b12*100, g_seed))
        b15 += (b16 - b14) ** 2
    b17 = b15 / b4
    for i in range(6):
        print('\t'.join(list(np.around(np.mean(b14[:, :, i], b18 = 0), 2).astype(str))))
    plt.figure()
    plt.subplot(1, 1, 1)
    for i, color in enumerate(['c', 'b', 'r', 'g', 'k']):
        plt.plot(b5, np.mean(b14[:, :, i], b18 = 0), color + '*', ms=12)
        plt.errorbar(b5, np.mean(b14[:, :, i], b18 = 0),
                     b19 = np.sqrt(np.mean(b17[:, :, i], b18=0)) / np.sqrt(b4), color=color, ms=12)
        plt.plot(b5, np.mean(b14[:, :, i], b18 = 0), color + '--', ms=12)
    plt.xlabel(r'$\alpha$', b20 = 16)
    plt.ylim(-0.1, 1.1)
    if lgnd:
        b21 = ['gPCA', 'JIVE', 'LP', 'BIC', 'KG', 'KN'] if data_type == 'Dest' else [r'$\alpha$', r'$p_{\alpha 1}$',  r'$p_{\alpha 2}$']
        plt.legend(b21, b22 = 'upper left', b20=16)
    plt.title('%s: Proportion of correct rank selections' % optn, b20 = 16)
    if b7:
        plt.savefig('%s%s(%dx%d)x%d_D%ds%d_all%d.png' % (data_type, v_, grp_N, b9,
            b10, b11, b12*100, b3[-1]), b23 = 'png', bbox_inches='tight')
    plt.show()
if b24 = = "__main__":
    fonk1()