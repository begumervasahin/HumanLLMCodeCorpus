import numpy as np
from numpy.linalg import eig
from scipy.stats import chi2
def gsis(snp_mat, qr_smy_mat, proj_mat):
    def calculate_q_zx(zx_mat):
        q_zx = np.sum(zx_mat * zx_mat, axis=1)
        q_zx[q_zx == 0] += 1e-6
        return q_zx
    def eigen_decomposition(matrix):
        eigenvalues, eigenvectors = eig(matrix)
        eigenvalues = np.real(eigenvalues)
        eigenvalues[eigenvalues < 0] = 0
        return eigenvalues, eigenvectors
    def sqrt_matrix(eigenvalues, eigenvectors):
        w_diag = np.diag(np.sqrt(eigenvalues))
        return np.real(np.dot(np.dot(eigenvectors, w_diag), eigenvectors.T))
    def calculate_global_test_statistics(zx_mat, sq_qr_smy_mat, inv_q_zx):
        return np.sum(np.dot(zx_mat, sq_qr_smy_mat) ** 2, axis=1) * inv_q_zx
    def calculate_moments(g_stat):
        k1 = np.mean(g_stat)
        k2 = np.var(g_stat)
        k3 = np.mean((g_stat - k1) ** 3)
        return k1, k2, k3
    def chi_squared_params(k1, k2, k3):
        a = k3 / (4 * k2)
        b = k1 - (2 * k2 ** 2) / k3
        d = 8 * (k2 ** 3) / (k3 ** 2)
        return a, b, d
    def calculate_p_values(g_stat, a, b, d):
        g_pv = 1 - chi2.cdf((g_stat - b) / a, d)
        return -np.log10(g_pv)
    n, g = snp_mat.shape
    zx_mat = np.dot(proj_mat, snp_mat).T
    q_zx = calculate_q_zx(zx_mat)
    inv_q_zx = q_zx ** (-1)
    eigenvalues, eigenvectors = eigen_decomposition(qr_smy_mat)
    sq_qr_smy_mat = sqrt_matrix(eigenvalues, eigenvectors)
    g_stat = calculate_global_test_statistics(zx_mat, sq_qr_smy_mat, inv_q_zx)
    k1, k2, k3 = calculate_moments(g_stat)
    a, b, d = chi_squared_params(k1, k2, k3)
    g_pv_log10 = calculate_p_values(g_stat, a, b, d)
    return g_pv_log10, g_stat