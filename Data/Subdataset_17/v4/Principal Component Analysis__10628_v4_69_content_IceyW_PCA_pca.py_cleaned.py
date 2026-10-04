import numpy as np
def zero_mean(data_mat):
    mean = np.mean(data_mat, axis=0)
    new_data = data_mat - mean
    return new_data, mean
def pca(data_mat):
    new_data, mean = zero_mean(data_mat)
    cov_mat = np.cov(new_data, rowvar=False)
    eig_vals, eig_vects = np.linalg.eig(cov_mat)
    eig_vals_sorted_indices = np.argsort(eig_vals)[::-1]
    eig_vals_sorted = eig_vals[eig_vals_sorted_indices]
    eig_vects_sorted = eig_vects[:, eig_vals_sorted_indices]
    return eig_vals_sorted, eig_vects_sorted
def percent_percentage(eig_vals, percentage):
    total_sum = np.sum(eig_vals)
    temp_sum = 0
    num = 0
    for val in eig_vals:
        temp_sum += val
        num += 1
        if temp_sum >= total_sum * percentage:
            break
    result_percent = eig_vals[:num] / total_sum
    return num, result_percent
def percent_all(eig_vals):
    _, percent = percent_percentage(eig_vals, 1)
    return percent
def percent_over_10(eig_vals):
    _, percent = percent_percentage(eig_vals, 1)
    count = np.sum(percent > 0.1)
    return count, percent[:count]
def project_data(data_mat, eig_vects, num_components):
    eig_vects_selected = eig_vects[:, :num_components]
    low_dim_data = np.dot(data_mat, eig_vects_selected)
    return low_dim_data