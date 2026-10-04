import numpy as np
def zero_mean(data_mat):
    mean = np.mean(data_mat, axis=0)
    new_data = data_mat - mean
    return new_data, mean
def pca(data_mat):
    new_data, mean = zero_mean(data_mat)
    cov_mat = np.cov(new_data, rowvar=False)
    eig_vals, eig_vects = np.linalg.eig(cov_mat)
    sorted_indices = np.argsort(eig_vals)[::-1]
    sorted_eig_vals = eig_vals[sorted_indices]
    sorted_eig_vects = eig_vects[:, sorted_indices]
    return sorted_eig_vals, sorted_eig_vects
def percent_percentage(eig_vals, percentage):
    total_variance = np.sum(eig_vals)
    temp_variance = 0
    num_components = 0
    for val in eig_vals:
        temp_variance += val
        num_components += 1
        if temp_variance >= total_variance * percentage:
            break
    variance_ratio = eig_vals[:num_components] / total_variance
    return num_components, variance_ratio
def percent_all(eig_vals):
    _, variance_ratio = percent_percentage(eig_vals, 1)
    return variance_ratio
def percent_over_10(eig_vals):
    _, variance_ratio = percent_percentage(eig_vals, 1)
    num_components_over_10 = np.sum(variance_ratio > 0.1)
    return num_components_over_10, variance_ratio[:num_components_over_10]
def project_data(data_mat, eig_vects, num_components):
    selected_eig_vects = eig_vects[:, :num_components]
    low_dim_data = np.dot(data_mat, selected_eig_vects)
    return low_dim_data