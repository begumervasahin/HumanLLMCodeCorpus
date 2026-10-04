import numpy as np
from numpy.linalg import eig
from scipy.stats import chi2
def gsis(snp_mat, qr_smy_mat, proj_mat):
    zx_mat = np.dot(proj_mat, snp_mat).T
    q_zx = np.sum(zx_mat * zx_mat, axis=1)
    q_zx[q_zx == 0] += 1e-6
    inv_q_zx = q_zx ** -1
    w, v = eig(qr_smy_mat)
    w = np.real(w)
    w[w < 0] = 0
    w_diag = np.diag(w ** 0.5)
    sq_qr_smy_mat = np.dot(np.dot(v, w_diag), v.T)
    sq_qr_smy_mat = np.real(sq_qr_smy_mat)
    g_stat = np.sum(np.dot(zx_mat, sq_qr_smy_mat) ** 2, axis=1) * inv_q_zx
    k1 = np.mean(g_stat)
    k2 = np.var(g_stat)
    k3 = np.mean((g_stat - k1) ** 3)
    a = k3 / (4 * k2)
    b = k1 - 2 * k2 ** 2 / k3
    d = 8 * k2 ** 3 / k3 ** 2
    g_pv = 1 - chi2.cdf((g_stat - b) / a, d)
    g_pv_log10 = -np.log10(g_pv)
    return g_pv_log10, g_stat
if __name__ == "__main__":
    n = 100
    g = 10
    snp_mat = np.random.rand(n, g)
    qr_smy_mat = np.random.rand(n, n)
    proj_mat = np.random.rand(n, n)
    g_pv_log10, g_stat = gsis(snp_mat, qr_smy_mat, proj_mat)
    print("g_pv_log10:", g_pv_log10)
    print("g_stat:", g_stat)