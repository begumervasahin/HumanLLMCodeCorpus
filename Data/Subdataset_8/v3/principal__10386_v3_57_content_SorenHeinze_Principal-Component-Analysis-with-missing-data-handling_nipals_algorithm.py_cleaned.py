import numpy as np
from math import sqrt
from copy import deepcopy
def nipals_pca(data, rawdata, number_of_components):
    P_s, Z_s, r_s, Z_Eigenvalues = [], [], [], []
    R_2, R_k_2, SPE, T_2 = [0], [], [], []
    variance_rawdata, column_variance_rawdata = calculate_raw_data_variances(rawdata)
    for i in range(number_of_components):
        first_Z, length_Z = get_first_score(data)
        Z, P, r, length_Z = nipals_iteration(data, first_Z, length_Z)
        P_s.append(P)
        Z_s.append(Z)
        r_s.append(r)
        Z_Eigenvalues.append(length_Z)
        print("Eigenvalue of {}th component: {}".format(i + 1, Z_Eigenvalues[i]))
        print("==================")
        data = data - np.dot(Z.T, P)
        R_2.append(calculate_R_2(data, variance_rawdata))
        R_k_2.append(calculate_R_k_2(data, column_variance_rawdata))
        SPE.append(calculate_SPE(data))
        T_2.append(calculate_T_2(Z, T_2))
    Z_merged, P_merged, r_merged = create_matrices(Z_s, P_s, r_s, number_of_components)
    return Z_merged, P_merged, r_merged, R_2, R_k_2, SPE, T_2
def calculate_raw_data_variances(rawdata):
    variance_rawdata = np.nansum(rawdata * rawdata)
    column_variance_rawdata = [np.nansum(rawdata[:, i] * rawdata[:, i]) for i in range(rawdata.shape[1])]
    return variance_rawdata, column_variance_rawdata
def get_first_score(data):
    squared = data * data
    summed = np.nansum(squared, axis=0)
    index = np.argmax(summed)
    Z = data[:, index]
    length_Z = np.nansum(Z ** 2)
    return Z, length_Z
def nipals_iteration(data, Z, length_Z):
    difference = 1
    iteration = 0
    while difference > 1e-9:
        iteration += 1
        P = calculate_p(data, Z, length_Z)
        Z = calculate_z(data, P)
        length_new_Z = np.nansum(Z ** 2)
        difference = abs(length_Z - length_new_Z)
        if iteration == 300:
            print("\n300 iterations have passed. Please check for extreme outliers in the data.")
        length_Z = length_new_Z
        if iteration > 600:
            break
    r = calculate_r(data, Z, P)
    P = np.array([P])
    Z = np.array([Z])
    r = np.array([r])
    print("Iterations completed:", iteration)
    return Z, P, r, length_Z
def calculate_p(data, Z, length_Z):
    p_s_per_column = []
    for m in range(data.shape[1]):
        p = np.sum(Z * data[:, m]) / length_Z
        p_s_per_column.append(p)
    return p_s_per_column
def calculate_z(data, P):
    z_s_per_row = []
    for n in range(data.shape[0]):
        z = np.sum(P * data[n, :]) / np.sum(P * P)
        z_s_per_row.append(z)
    return z_s_per_row
def calculate_r(data, Z, P):
    r_s_per_column = []
    for o in range(P.shape[0]):
        modified_Z = deepcopy(Z)
        no_number_here = np.argwhere(np.isnan(data[:, o]))
        modified_Z = np.delete(modified_Z, no_number_here)
        x_dash = np.nanmean(data[:, o])
        z_dash = np.nanmean(modified_Z)
        upper_sum = np.sum((data[:, o] - x_dash) * (modified_Z - z_dash))
        first_lower_sum = np.sum((data[:, o] - x_dash) ** 2)
        second_lower_sum = np.sum((modified_Z - z_dash) ** 2)
        divisor = sqrt(first_lower_sum) * sqrt(second_lower_sum)
        r = upper_sum / divisor
        r_s_per_column.append(r)
    return r_s_per_column
def calculate_R_2(data, variance_rawdata):
    variance_new_data = np.nansum(data * data)
    return 1 - variance_new_data / variance_rawdata
def calculate_R_k_2(data, column_variance_rawdata):
    new_R_k_2 = []
    for i in range(data.shape[1]):
        column_variance_new_data = np.nansum(data[:, i] * data[:, i])
        new_R_k_2.append(1 - column_variance_new_data / column_variance_rawdata[i])
    return new_R_k_2
def calculate_SPE(data):
    new_SPE = []
    for i in range(data.shape[0]):
        foo = sqrt(np.dot(data[i].reshape(data[0].shape[0], 1).T, data[i].reshape(data[0].shape[0], 1)))
        if np.isnan(foo):
            foo = sqrt(np.nansum(data[i] ** 2))
        new_SPE.append(foo)
    return new_SPE
def calculate_T_2(Z, T_2):
    new_T_2 = []
    if len(T_2) == 0:
        s_a = np.std(Z)
        for i in range(Z.shape[1]):
            new_T_2.append((Z[0][i] / s_a) ** 2)
    else:
        add_to_this = len(T_2) - 1
        s_a = np.std(Z)
        for i in range(Z.shape[1]):
            new_T_2.append(T_2[add_to_this][i] + (Z[0][i] / s_a) ** 2)
    return new_T_2
def create_matrices(Z_s, P_s, r_s, number_of_components):
    P_merged = np.concatenate(P_s, axis=0)
    Z_merged = np.concatenate(Z_s, axis=0)
    r_merged = np.concatenate(r_s, axis=0)
    return Z_merged, P_merged, r_merged
