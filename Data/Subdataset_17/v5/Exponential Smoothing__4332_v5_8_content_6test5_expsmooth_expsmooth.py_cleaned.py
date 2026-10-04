
import numpy as np
import xlwings as xw
@xw.func
def expsmooth(data):
    data = list(data)
    def calculate_sigma(alpha):
        eps = 0
        smoothed_value = data[0]
        for i in range(1, len(data)):
            smoothed_value = alpha * data[i] + (1 - alpha) * smoothed_value
            eps += (smoothed_value - data[i]) ** 2
        return eps / len(data)
    def find_optimal_alpha(alpha_range, step=0.001):
        alphas = np.arange(alpha_range[0], alpha_range[1], step)
        sigmas = [calculate_sigma(alpha) for alpha in alphas]
        min_sigma_index = np.argmin(sigmas)
        return alphas[min_sigma_index]
    coarse_alphas = np.arange(0.1, 2.0, 0.1)
    coarse_sigmas = [calculate_sigma(alpha) for alpha in coarse_alphas]
    best_coarse_alpha = coarse_alphas[np.argmin(coarse_sigmas)]
    fine_alpha_range = (max(0, best_coarse_alpha - 0.2), best_coarse_alpha + 0.2)
    best_alpha = find_optimal_alpha(fine_alpha_range)
    smoothed_value = data[0]
    for i in range(1, len(data)):
        smoothed_value = best_alpha * data[i] + (1 - best_alpha) * smoothed_value
    return smoothed_value
if __name__ == '__main__':
    xw.Book().set_mock_caller()
    expsmooth()