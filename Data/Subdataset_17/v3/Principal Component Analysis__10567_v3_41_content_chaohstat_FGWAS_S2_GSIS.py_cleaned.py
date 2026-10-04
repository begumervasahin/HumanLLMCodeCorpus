import numpy as np
from numpy.linalg import eig
from scipy.stats import chi2
def gsis(snp_mat, qr_smy_mat, proj_mat):
    zx_mat = np.dot(proj_mat, snp_mat).T
    q_zx = np.sum(zx_mat * zx_mat, axis=1)
    q_zx[q_zx == 0] += 1e-6
    inv_q_zx = 1.0 / q_zx
    eigenvalues, eigenvectors = eig(qr_smy_mat)
    eigenvalues = np.real(eigenvalues)
    eigenvalues[eigenvalues < 0] = 0
    sqrt_eigenvalues = np.sqrt(eigenvalues)
    sqrt_qr_smy_mat = np.dot(np.dot(eigenvectors, np.diag(sqrt_eigenvalues)), eigenvectors.T)
    sqrt_qr_smy_mat = np.real(sqrt_qr_smy_mat)
    g_stat = np.sum(np.dot(zx_mat, sqrt_qr_smy_mat) ** 2, axis=1) * inv_q_zx
    mean_g_stat = np.mean(g_stat)
    var_g_stat = np.var(g_stat)
    skew_g_stat = np.mean((g_stat - mean_g_stat) ** 3)
    a = skew_g_stat / (4 * var_g_stat)
    b = mean_g_stat - (2 * var_g_stat ** 2 / skew_g_stat)
    d = (8 * var_g_stat ** 3) / (skew_g_stat ** 2)
    g_pv = 1 - chi2.cdf((g_stat - b) / a, d)
    g_pv_log10 = -np.log10(g_pv)
    return g_pv_log10, g_stat
def main():
    n = 100
    g = 10
    snp_mat = np.random.rand(n, g)
    qr_smy_mat = np.random.rand(n, n)
    proj_mat = np.random.rand(n, n)
    g_pv_log10, g_stat = gsis(snp_mat, qr_smy_mat, proj_mat)
    print("g_pv_log10:", g_pv_log10)
    print("g_stat:", g_stat)
if __name__ == "__main__":
    main()