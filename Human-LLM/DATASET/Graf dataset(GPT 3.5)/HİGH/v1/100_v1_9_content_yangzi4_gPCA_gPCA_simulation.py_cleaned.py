import os
import random
import numpy as np
import matplotlib.pyplot as plt
from numpy import array, arange, diag, eye, hstack, sqrt, zeros, savetxt, save, load, mean, around
def fonk1():
    b1 = range(1, 5)
    Dest, Pval, b2 = 1, 1, 0
    b3 = range(25)
    b4 = float(len(b3))
    b5 = arange(0, 1.01, 0.1)
    if 1:
        plt.close('all')
        a1 = 1
        fonk2(13, 16, 3, 0.1, a1, '', '(a)', 1)
        fonk3(13, 16, 3, 0.1, a1, '', '(b)', 1)
def fonk2(p1, p2, p3, p4, b6 = 0, v_='', optn=0, lgnd=0):
    b7 = [1, 2, 3, 4]
    for param in b7:
        grp_N, b8 = p1, p2
        b9 = p3
        b10 = param
        b11 = p4
    b12 = np.zeros((len(b7), len(b5), 6))
    for g_seed in b3:
        b12 += load('Dest%s(%dx%d)x%d_D%ds%d_%d.npy' % (
            v_, grp_N, b8, b9, b10, b11*100, g_seed))
    b13 = b12/b4
    b14 = np.zeros((len(b7), len(b5), 6))
    for g_seed in b3:
        b15 = load('Dest%s(%dx%d)x%d_D%ds%d_%d.npy' % (
            v_, grp_N, b8, b9, b10, b11*100, g_seed))
        b14 += (b15 - b13)**2
    b16 = b14/b4
    for i in range(0, 6):
        print('\t'.join(list(around(np.mean(b13[:, :, i], b17 = 0), 2).astype(str))))
    ftsz1, ftsz2, b18 = 16, 16, 16
    plt.figure()
    plt.subplot(1, 1, 1)
    plt.plot(b5, np.mean(b13[:, :, 0], b17 = 0), 'cv', ms=12)
    plt.plot(b5, np.mean(b13[:, :, 1], b17 = 0), 'c^', ms=12)
    plt.plot(b5, np.mean(b13[:, :, 2], b17 = 0), 'bs', ms=12)
    plt.plot(b5, np.mean(b13[:, :, 3], b17 = 0), 'ro', ms=12)
    plt.plot(b5, np.mean(b13[:, :, 4], b17 = 0), 'gd', ms=12)
    plt.plot(b5, np.mean(b13[:, :, 5], b17 = 0), 'k*', ms=12)
    plt.errorbar(b5, np.mean(b13[:, :, 0], b17 = 0),
        b19 = np.sqrt(np.mean(b16[:, :, 0], b17=0))/np.sqrt(b4), color='c', ms=12)
    plt.errorbar(b5, np.mean(b13[:, :, 1], b17 = 0),
        b19 = np.sqrt(np.mean(b16[:, :, 1], b17=0))/np.sqrt(b4), color='c', ms=12)
    plt.errorbar(b5, np.mean(b13[:, :, 2], b17 = 0),
        b19 = np.sqrt(np.mean(b16[:, :, 2], b17=0))/np.sqrt(b4), color='b', ms=12)
    plt.errorbar(b5, np.mean(b13[:, :, 3], b17 = 0),
        b19 = np.sqrt(np.mean(b16[:, :, 3], b17=0))/np.sqrt(b4), color='r', ms=12)
    plt.errorbar(b5, np.mean(b13[:, :, 4], b17 = 0),
        b19 = np.sqrt(np.mean(b16[:, :, 4], b17=0))/np.sqrt(b4), color='g', ms=12)
    plt.errorbar(b5, np.mean(b13[:, :, 5], b17 = 0),
        b19 = np.sqrt(np.mean(b16[:, :, 5], b17=0))/np.sqrt(b4), color='k', ms=12)
    plt.plot(b5, np.mean(b13[:, :, 0], b17 = 0), 'c--', ms=12)
    plt.plot(b5, np.mean(b13[:, :, 1], b17 = 0), 'c--', ms=12)
    plt.plot(b5, np.mean(b13[:, :, 2], b17 = 0), 'b--', ms=12)
    plt.plot(b5, np.mean(b13[:, :, 3], b17 = 0), 'r--', ms=12)
    plt.plot(b5, np.mean(b13[:, :, 4], b17 = 0), 'g--', ms=12)
    plt.plot(b5, np.mean(b13[:, :, 5], b17 = 0), 'k--', ms=12)
    plt.xlabel(r'$\alpha$', b20 = ftsz2)
    plt.ylim(-0.1, 1.1)
    if lgnd:
        plt.legend(['gPCA', 'JIVE', 'LP', 'BIC', 'KG', 'KN'], b21 = 'upper left', b20=b18)
    plt.title('%s: Proportion of correct rank selections' % optn, b20 = ftsz1)
    if b6:
        plt.savefig('Dest%s(%dx%d)x%d_D%ds%d_all%d.png' % (v_, grp_N, b8, b9,
            b10, b11*100, b3[-1]), b22 = 'png', bbox_inches='tight')
    plt.show()
def fonk3(p1, p2, p3, p4, b6 = 0, v_='', optn=0, lgnd=0):
    b7 = [1, 2, 3, 4]
    for param in b7:
        grp_N, b8 = p1, p2
        b9 = p3
        b10 = param
        b11 = p4
    b12 = np.zeros((len(b7), len(b5), 6))
    for g_seed in b3:
        b12 += load('Pval%s(%dx%d)x%d_D%ds%d_%d.npy' % (
            v_, grp_N, b8, b9, b10, b11*100, g_seed))
    b13 = b12/b4
    b14 = np.zeros((len(b7), len(b5), 6))
    for g_seed in b3:
        b15 = load('Pval%s(%dx%d)x%d_D%ds%d_%d.npy' % (
            v_, grp_N, b8, b9, b10, b11*100, g_seed))
        b14 += (b15 - b13)**2
    b16 = np.sqrt(b14/b4)
    for i in range(0, 6):
        print('\t'.join(list(around(np.mean(b13[:, :, i], b17 = 0), 2).astype(str))))
    ftsz1, ftsz2, b18 = 16, 16, 16
    plt.figure()
    plt.subplot(1, 1, 1)
    plt.plot(b5, np.mean(b13[:, :, 0], b17 = 0), 'cv', ms=12)
    plt.plot(b5, np.mean(b13[:, :, 1], b17 = 0), 'c^', ms=12)
    plt.plot(b5, np.mean(b13[:, :, 2], b17 = 0), 'bs', ms=12)
    plt.plot(b5, np.mean(b13[:, :, 3], b17 = 0), 'ro', ms=12)
    plt.plot(b5, np.mean(b13[:, :, 4], b17 = 0), 'gd', ms=12)
    plt.plot(b5, np.mean(b13[:, :, 5], b17 = 0), 'k*', ms=12)
    plt.errorbar(b5, np.mean(b13[:, :, 0], b17 = 0),
        b19 = np.sqrt(np.mean(b16[:, :, 0], b17=0))/np.sqrt(b4), color='c', ms=12)
    plt.errorbar(b5, np.mean(b13[:, :, 1], b17 = 0),
        b19 = np.sqrt(np.mean(b16[:, :, 1], b17=0))/np.sqrt(b4), color='c', ms=12)
    plt.errorbar(b5, np.mean(b13[:, :, 2], b17 = 0),
        b19 = np.sqrt(np.mean(b16[:, :, 2], b17=0))/np.sqrt(b4), color='b', ms=12)
    plt.errorbar(b5, np.mean(b13[:, :, 3], b17 = 0),
        b19 = np.sqrt(np.mean(b16[:, :, 3], b17=0))/np.sqrt(b4), color='r', ms=12)
    plt.errorbar(b5, np.mean(b13[:, :, 4], b17 = 0),
        b19 = np.sqrt(np.mean(b16[:, :, 4], b17=0))/np.sqrt(b4), color='g', ms=12)
    plt.errorbar(b5, np.mean(b13[:, :, 5], b17 = 0),
        b19 = np.sqrt(np.mean(b16[:, :, 5], b17=0))/np.sqrt(b4), color='k', ms=12)
    plt.plot(b5, np.mean(b13[:, :, 0], b17 = 0), 'c--', ms=12)
    plt.plot(b5, np.mean(b13[:, :, 1], b17 = 0), 'c--', ms=12)
    plt.plot(b5, np.mean(b13[:, :, 2], b17 = 0), 'b--', ms=12)
    plt.plot(b5, np.mean(b13[:, :, 3], b17 = 0), 'r--', ms=12)
    plt.plot(b5, np.mean(b13[:, :, 4], b17 = 0), 'g--', ms=12)
    plt.plot(b5, np.mean(b13[:, :, 5], b17 = 0), 'k--', ms=12)
    plt.xlabel(r'$\alpha$', b20 = ftsz2)
    plt.ylim(-0.1, 1.1)
    if lgnd:
        plt.legend([r'$\alpha$', r'$p_{\alpha 1}$',  r'$p_{\alpha 2}$',
            r'$\alpha$', r'$p_{\alpha 1}$',  r'$p_{\alpha 2}$'], b21 = 'upper left', b20=b18)
    plt.title('%s: alpha, p_alpha1, p_alpha2' % optn, b20 = ftsz1)
    if b6:
        plt.savefig('Pval%s(%dx%d)x%d_D%ds%d_all%d.png' % (v_, grp_N, b8, b9,
            b10, b11*100, b3[-1]), b22 = 'png', bbox_inches='tight')
    plt.show()
if b23 = = "__main__":
    fonk1()