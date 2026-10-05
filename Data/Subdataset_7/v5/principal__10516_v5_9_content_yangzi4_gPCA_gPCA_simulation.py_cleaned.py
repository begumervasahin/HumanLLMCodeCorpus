import os
import random
import numpy as np
import matplotlib.pyplot as plt
b1 = range(1, 5)
Dest, Pval, b2 = 1, 1, 0
grp_N, b3 = 13, 16
a1 = 3
a2 = 0.1
a3 = 1
b4 = np.arange(0, 1.01, 0.1)
def fonk1(b9, b7, a2, H):
    pass
def fonk2(X_cd, b1, version):
    pass
for gen_seed in range(25):
    b5 = []
    b6 = []
    for param in [1, 2, 3, 4]:
        b7 = param
        b8 = [grp_N * a1, b3]
        b9 = [[grp_N] * a1, b3]
        b10 = np.diag([1] * b7)
        b11 = np.hstack([np.eye(b7)[:, d:(d + 1)] for d in range(b7)] * a3)
        b12 = b10.dot(np.hstack((b11, np.zeros((b7, b3 - b7 * a3)))) / np.sqrt(a3))
        b13 = [b10.dot(np.hstack([np.zeros((b7, b7 * a3))] * (k + 1) + [b11] +
                                      [np.zeros((b7, b3 - b7 * a3 * (k + 2)))]) / np.sqrt(a3)) for k in
               range(a1)]
        b14 = []
        b15 = []
        print('___', grp_N, a1, b3, b7, a2, a3, '___')
        for alpha in b4:
            if not (Dest or Pval):
                continue
            random.seed(gen_seed)
            b16 = [alpha * b12 + np.sqrt(1 - alpha ** 2) * b13[k] for k in range(a1)]
            b17 = fonk1(b9, b7, a2, H_=b16)
            X_cd, X_cd_ne, b18 = b17[0], [b17[1][k].dot(b17[2][k]) for k in range(a1)], b17[3]
            if b2:
                for k in range(a1):
                    np.savetxt('data/data(%dx%d)x%d_a%dD%ds%d_%d.txt' %
                               (grp_N, b3, k, int(alpha * 100), b7, int(a2 * 100), gen_seed), X_cd[k])
            random.seed(1)
            b19 = fonk2(X_cd, b1=b1, version=1)
            b14.append([
                b7 = = b1[b19[3]],
                b1[b19[3]],
            ])
            if Dest:
                print('Dest:', b14[-1])
            b15.append([
                b19[1][b19[3]],
                calc_alpha_pval(b19[1][b19[3]], b3, b1[b19[3]]),
                calc_alpha_pval2(b19[1][b19[3]], X_cd, b1[b19[3]])[0]
            ] * 2)
            if Pval:
                print('Pval:', np.around(np.array(b15[-1]), 3))
        b5.append(b14)
        b6.append(b15)
    if Dest:
        np.save('Dest(%dx%d)x%d_D%ds%d_%d' % (grp_N, b3, a1, b7, int(a2 * 100), gen_seed),
                np.array(b5))
    if Pval:
        np.save('Pval(%dx%d)x%d_D%ds%d_%d' % (grp_N, b3, a1, b7, int(a2 * 100), gen_seed),
                np.array(b6))
def fonk3(p1, p2, p3, p4, b20 = 0, v_='', optn=0, lgnd=0):
    pass
def fonk4(p1, p2, p3, p4, b20 = 0, v_='', optn=0, lgnd=0):
    pass
b21 = np.array(range(25))
b22 = float(len(b21))
if 1:
    plt.close('all')
    b20 = 1
    fonk3(13, 16, 3, 0.1, b20, '', '(a)', 1)
    fonk4(13, 16, 3, 0.1, b20, '', '(b)', 1)