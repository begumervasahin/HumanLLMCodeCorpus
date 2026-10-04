
import numpy as np
def prototype_sharpness_ratio(X, som):
    size = int(np.sqrt(X.shape[-1]))
    X = X.reshape(-1, size, size, 1)
    som = som.reshape(-1, size, size, 1)
    data_sharpness = 0.0
    for x in X:
        gx, gy = np.gradient(x[:, :, 0])
        gnorm = np.sqrt(gx ** 2 + gy ** 2)
        data_sharpness += np.mean(gnorm)
    data_sharpness /= X.shape[0]
    som_sharpness = 0.0
    for prototype in som:
        gx, gy = np.gradient(prototype[:, :, 0])
        gnorm = np.sqrt(gx ** 2 + gy ** 2)
        som_sharpness += np.mean(gnorm)
    som_sharpness /= som.shape[0]
    return som_sharpness / data_sharpness