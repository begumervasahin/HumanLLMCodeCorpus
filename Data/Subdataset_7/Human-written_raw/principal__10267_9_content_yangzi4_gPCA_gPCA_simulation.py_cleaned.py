import os
b1 = range(1, 5)
Dest, Pval, b2 = 1, 1, 0
for gen_seed in range(0, 25)[:]:
    b3 = []
    b4 = []
    for param in [1, 2, 3, 4]:
        grp_N, b5 = 13, 16
        a1 = 3
        b6 = param
        a2 = 0.1
        a3 = 1
        b7 = [grp_N*a1, b5]
        b8 = [[grp_N]*a1, b5]
        b9 = diag([1]*b6)
        b10 = hstack([hstack([eye(b6)[:, d:(d+1)]]*a3) for d in range(b6)])
        b11 = b9.dot(hstack((b10, zeros((b6, b5 - b6*a3))))/sqrt(a3))
        b12 = [b9.dot(hstack([zeros((b6, b6*a3))]*(k + 1) + [b10] +
            [zeros((b6, b5 - b6*a3*(k + 2)))])/sqrt(a3)) for k in range(a1)]
        b13 = []
        b14 = []
        b15 = arange(0, 1.01, 0.1)
        print '___', grp_N, a1, b5, b6, a2, a3, '___'
        for alpha in b15:
            if (Dest or Pval) == 0: continue
            random.seed(gen_seed)
            b16 = [alpha*b11 + sqrt(1 - alpha**2)*b12[k] for k in range(a1)]
            b17 = group_data_gen(b8, b6, a2, H_=b16)
            X_cd, X_cd_ne, b18 = b17[0], [b17[1][k].dot(b17[2][k]) for k in range(a1)], b17[3]
            if b2:
                for k in range(a1): savetxt('data/data(%dx%d)x%d_a%dD%ds%d_%d.txt' %
                    (grp_N, b5, k, alpha*100, b6, a2*100, gen_seed), X_cd[k])
            random.seed(1)
            b19 = gPCA_select(X_cd, D_range=b1, vers=1)
            b13.append([
                b6 = = b1[b19[3]]
                b1[b19[3]],
                ])
            if Dest: print 'Dest:', b13[-1]
            b14.append([
                b19[1][b19[3]],
                calc_alpha_pval(b19[1][b19[3]], b5, b1[b19[3]]),
                calc_alpha_pval2(b19[1][b19[3]], X_cd, b1[b19[3]])[0]
            ]*2)
            if Pval: print 'Pval:', around(array(b14[-1]), 3)
        b3.append(b13)
        b4.append(b14)
    if Dest: save('Dest(%dx%d)x%d_D%ds%d_%d' % (grp_N, b5, a1, b6, a2*100, gen_seed),
        array(b3))
    if Pval: save('Pval(%dx%d)x%d_D%ds%d_%d' % (grp_N, b5, a1, b6, a2*100, gen_seed),
        array(b4))
def fonk1(p1, p2, p3, p4, b20 = 0, v_='', optn=0, lgnd=0):
    b21 = [1, 2, 3, 4]
    for param in b21:
        grp_N, b5 = p1, p2
        a1 = p3
        b6 = param
        a2 = p4
    b22 = zeros((len(b21), len(b15), 6))
    for g_seed in b33:
        b22 += load('Dest%s(%dx%d)x%d_D%ds%d_%d.npy' % (
            v_, grp_N, b5, a1, b6, a2*100, g_seed))
    b23 = b22/b34
    b24 = zeros((len(b21), len(b15), 6))
    for g_seed in b33:
        b25 = load('Dest%s(%dx%d)x%d_D%ds%d_%d.npy' % (
            v_, grp_N, b5, a1, b6, a2*100, g_seed))
        b24 += (b25 - b23)**2
    b26 = b24/b34
    for i in range(0, 6): print '\t'.join(list(around(mean(b23[:, :, i], b27 = 0), 2).astype(str)))
    ftsz1, ftsz2, b28 = 16, 16, 16
    plt.figure()
    plt.subplot(1, 1, 1)
    plt.plot(b15, mean(b23[:, :, 0], b27 = 0), 'cv', ms=12)
    plt.plot(b15, mean(b23[:, :, 1], b27 = 0), 'c^', ms=12)
    plt.plot(b15, mean(b23[:, :, 2], b27 = 0), 'bs', ms=12)
    plt.plot(b15, mean(b23[:, :, 3], b27 = 0), 'ro', ms=12)
    plt.plot(b15, mean(b23[:, :, 4], b27 = 0), 'gd', ms=12)
    plt.plot(b15, mean(b23[:, :, 5], b27 = 0), 'k*', ms=12)
    plt.errorbar(b15, mean(b23[:, :, 0], b27 = 0),
        b29 = sqrt(mean(b26[:, :, 0], b27=0))/sqrt(b34), color='c', ms=12)
    plt.errorbar(b15, mean(b23[:, :, 1], b27 = 0),
        b29 = sqrt(mean(b26[:, :, 1], b27=0))/sqrt(b34), color='c', ms=12)
    plt.errorbar(b15, mean(b23[:, :, 2], b27 = 0),
        b29 = sqrt(mean(b26[:, :, 2], b27=0))/sqrt(b34), color='b', ms=12)
    plt.errorbar(b15, mean(b23[:, :, 3], b27 = 0),
        b29 = sqrt(mean(b26[:, :, 3], b27=0))/sqrt(b34), color='r', ms=12)
    plt.errorbar(b15, mean(b23[:, :, 4], b27 = 0),
        b29 = sqrt(mean(b26[:, :, 4], b27=0))/sqrt(b34), color='g', ms=12)
    plt.errorbar(b15, mean(b23[:, :, 5], b27 = 0),
        b29 = sqrt(mean(b26[:, :, 5], b27=0))/sqrt(b34), color='k', ms=12)
    plt.plot(b15, mean(b23[:, :, 0], b27 = 0), 'c--', ms=12)
    plt.plot(b15, mean(b23[:, :, 1], b27 = 0), 'c--', ms=12)
    plt.plot(b15, mean(b23[:, :, 2], b27 = 0), 'b--', ms=12)
    plt.plot(b15, mean(b23[:, :, 3], b27 = 0), 'r--', ms=12)
    plt.plot(b15, mean(b23[:, :, 4], b27 = 0), 'g--', ms=12)
    plt.plot(b15, mean(b23[:, :, 5], b27 = 0), 'k--', ms=12)
    plt.xlabel(r'$\alpha$', b30 = ftsz2)
    plt.ylim(-0.1, 1.1)
    if lgnd: plt.legend(['gPCA', 'JIVE', 'LP', 'BIC', 'KG', 'KN'], b31 = 'upper left', b30=b28)
    plt.title('%s: Proportion of correct rank selections' % optn, b30 = ftsz1)
    if b20: plt.savefig('Dest%s(%dx%d)x%d_D%ds%d_all%d.png' % (v_, grp_N, b5, a1,
        b6, a2*100, b33[-1]), b32 = 'png', bbox_inches='tight')
    return
def fonk2(p1, p2, p3, p4, b20 = 0, v_='', optn=0, lgnd=0):
    b21 = [1, 2, 3, 4]
    for param in b21:
        grp_N, b5 = p1, p2
        a1 = p3
        b6 = param
        a2 = p4
    b22 = zeros((len(b21), len(b15), 6))
    for g_seed in b33:
        b22 += load('Pval%s(%dx%d)x%d_D%ds%d_%d.npy' % (
            v_, grp_N, b5, a1, b6, a2*100, g_seed))
    b23 = b22/b34
    b24 = zeros((len(b21), len(b15), 6))
    for g_seed in b33:
        b25 = load('Pval%s(%dx%d)x%d_D%ds%d_%d.npy' % (
            v_, grp_N, b5, a1, b6, a2*100, g_seed))
        b24 += (b25 - b23)**2
    b26 = sqrt(b24/b34)
    for i in range(0, 6): print '\t'.join(list(around(mean(b23[:, :, i], b27 = 0), 2).astype(str)))
    ftsz1, ftsz2, b28 = 16, 16, 16
    plt.figure()
    plt.subplot(1, 1, 1)
    plt.plot(b15, mean(b23[:, :, 0], b27 = 0), 'cv', ms=12)
    plt.plot(b15, mean(b23[:, :, 1], b27 = 0), 'c^', ms=12)
    plt.plot(b15, mean(b23[:, :, 2], b27 = 0), 'bs', ms=12)
    plt.plot(b15, mean(b23[:, :, 3], b27 = 0), 'ro', ms=12)
    plt.plot(b15, mean(b23[:, :, 4], b27 = 0), 'gd', ms=12)
    plt.plot(b15, mean(b23[:, :, 5], b27 = 0), 'k*', ms=12)
    plt.errorbar(b15, mean(b23[:, :, 0], b27 = 0),
        b29 = sqrt(mean(b26[:, :, 0], b27=0))/sqrt(b34), color='c', ms=12)
    plt.errorbar(b15, mean(b23[:, :, 1], b27 = 0),
        b29 = sqrt(mean(b26[:, :, 1], b27=0))/sqrt(b34), color='c', ms=12)
    plt.errorbar(b15, mean(b23[:, :, 2], b27 = 0),
        b29 = sqrt(mean(b26[:, :, 2], b27=0))/sqrt(b34), color='b', ms=12)
    plt.errorbar(b15, mean(b23[:, :, 3], b27 = 0),
        b29 = sqrt(mean(b26[:, :, 3], b27=0))/sqrt(b34), color='r', ms=12)
    plt.errorbar(b15, mean(b23[:, :, 4], b27 = 0),
        b29 = sqrt(mean(b26[:, :, 4], b27=0))/sqrt(b34), color='g', ms=12)
    plt.errorbar(b15, mean(b23[:, :, 5], b27 = 0),
        b29 = sqrt(mean(b26[:, :, 5], b27=0))/sqrt(b34), color='k', ms=12)
    plt.plot(b15, mean(b23[:, :, 0], b27 = 0), 'c--', ms=12)
    plt.plot(b15, mean(b23[:, :, 1], b27 = 0), 'c--', ms=12)
    plt.plot(b15, mean(b23[:, :, 2], b27 = 0), 'b--', ms=12)
    plt.plot(b15, mean(b23[:, :, 3], b27 = 0), 'r--', ms=12)
    plt.plot(b15, mean(b23[:, :, 4], b27 = 0), 'g--', ms=12)
    plt.plot(b15, mean(b23[:, :, 5], b27 = 0), 'k--', ms=12)
    plt.xlabel(r'$\alpha$', b30 = ftsz2)
    plt.ylim(-0.1, 1.1)
    if lgnd: plt.legend([r'$\alpha$', r'$p_{\alpha 1}$',  r'$p_{\alpha 2}$',
        r'$\alpha$', r'$p_{\alpha 1}$',  r'$p_{\alpha 2}$'], b31 = 'upper left', b30=b28)
    plt.title('%s: alpha, p_alpha1, p_alpha2' % optn, b30 = ftsz1)
    if b20: plt.savefig('Pval%s(%dx%d)x%d_D%ds%d_all%d.png' % (v_, grp_N, b5, a1,
        b6, a2*100, b33[-1]), b32 = 'png', bbox_inches='tight')
    return
b33 = array(range(25))
b34 = float(len(b33))
b15 = arange(0, 1.01, 0.1)
if 1:
    plt.close('all')
    a4 = 1
    fonk1(13, 16, 3, 0.1, a4, '', '(a)', 1)
    fonk2(13, 16, 3, 0.1, a4, '', '(b)', 1)