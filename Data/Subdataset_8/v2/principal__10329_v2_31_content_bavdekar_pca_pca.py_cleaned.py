import numpy as np
import scipy as sp
def lpca(data, cv=None, normalize=False):
    if normalize:
        mean_vector = np.mean(data, axis=0)
        var_vector = np.var(data, axis=0, ddof=1)
        data_zm_uv = (data - np.matmul(np.ones((data.shape[0], data.shape[1])), np.diag(mean_vector))) / (var_vector.T)
    else:
        data_zm_uv = data
    U, S, Vt = np.linalg.svd(data_zm_uv)
    cumulative_variance_explained = np.cumsum(100 * S / np.sum(S))
    if cv is None:
        cv = 95
    num_components = np.argmax(cumulative_variance_explained >= cv)
    return Vt[0:num_components, :]
def scpa(data, cv=None, normalize=False):
    if normalize:
        normalize = False
    W = sp.linalg.expm(np.corrcoef(data, rowvar=False) / 0.1)
    D = np.diag(np.sum(W, axis=0))
    scaled_data = np.matmul(sp.linalg.inv(sp.linalg.sqrtm(D)), np.matmul(W, sp.linalg.inv(sp.linalg.sqrtm(D))))
    U, S, Vt = np.linalg.svd(scaled_data)
    cumulative_variance_explained = np.cumsum(100 * S / np.sum(S))
    if cv is None:
        cv = 95
    num_components = np.argmax(cumulative_variance_explained >= cv)
    return np.matmul(sp.linalg.inv(sp.linalg.sqrtm(D)), Vt.T)[:, 0:num_components].T
if __name__ == "__main__":
    data = np.random.rand(100, 10)
    lpca_result = lpca(data)
    print("LPCA Result Shape:", lpca_result.shape)
    scpa_result = scpa(data)
    print("SCPA Result Shape:", scpa_result.shape)