import numpy as np
from scipy import linalg as SLA
from math import sqrt
from copy import deepcopy
import plotting as pl
def nipals_pca(data, rawdata, number_of_components):
    P_s, Z_s, r_s = [], [], []
    Z_Eigenvalues, R_2, R_k_2, SPE, T_2 = [], [0], [], [], []
    variance_rawdata, column_variance_rawdata = calculate_raw_data_variances(rawdata)
    for i in range(number_of_components):
        first_Z, length_Z = get_first_score(data)
        Z, P, r, length_Z = nipals_iteration(data, first_Z, length_Z)
        P_s.append(P)
        Z_s.append(Z)
        r_s.append(r)
        Z_Eigenvalues.append(length_Z)
        print(f"Eigenvalue of {i + 1}. component: {Z_Eigenvalues[i]}")
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
    length_Z = np.nansum(Z**2)
    return Z, length_Z
def nipals_iteration(data, Z, length_Z):
    difference, iteration = 1, 0
    while difference > 0.000000001:
        iteration += 1
        p_s_per_column = calculate_p_s_per_column(data, Z, length_Z)
        P = np.array(p_s_per_column)
        z_s_per_row = calculate_z_s_per_row(data, P)
        new_Z = np.array(z_s_per_row)
        length_new_Z = np.nansum(new_Z**2)
        difference = abs(length_Z - length_new_Z)
        if iteration == 300:
            print("\n300 iterations have passed, please check the data for extreme outliers. "
                  "And take these out if after 300 more iterations NIPALs still doesn't converge.")
            pl.plot_scores(1, [1, 1], 'foo', range(1, (len(Z) + 1)), [Z])
        Z = new_Z
        length_Z = length_new_Z
        if iteration > 600:
            break
    r_s_per_column = calculate_r_s_per_column(data, Z, P)
    r, P, Z = np.array(r_s_per_column), np.array([P]), np.array([Z])
    print("So many iterations undertaken:", iteration)
    return Z, P, r, length_Z
def calculate_r_s_per_column(data, Z, P):
    r_s_per_column = []
    for o in range(P.shape[0]):
        upper_sum, first_lower_sum, second_lower_sum = 0, 0, 0
        modified_Z = deepcopy(Z)
        no_number_here = np.argwhere(np.isnan(data[:, o]))
        modified_Z = remove_elements(modified_Z, no_number_here)
        x_dash = np.nansum(data[:, o]) / (len(data[:, o]) - len(no_number_here))
        z_dash = np.nansum(modified_Z) / len(modified_Z)
        for i in range(len(modified_Z)):
            if np.isnan(data[:, o][i]):
                continue
            first_factor = data[:, o][i] - x_dash
            second_factor = modified_Z[i] - z_dash
            upper_sum += first_factor * second_factor
            first_lower_sum += first_factor**2
            second_lower_sum += second_factor**2
        divisor = sqrt(first_lower_sum) * sqrt(second_lower_sum)
        r = upper_sum / divisor
        r_s_per_column.append(r)
    return r_s_per_column
def remove_elements(modified_Z, no_number_here):
    this_array, i = deepcopy(modified_Z), 0
    for element in no_number_here:
        index = element[0] - i
        i += 1
        this_array = np.delete(this_array, index)
    return this_array
def calculate_p_s_per_column(data, Z, length_Z):
    p_s_per_column = []
    for m in range(data.shape[1]):
        upper_sum, lower_sum = 0, 0
        for i in range(len(Z)):
            if np.isnan(data[:, m][i]) or np.isnan(Z[i]):
                continue
            upper_sum += Z[i] * data[:, m][i]
            lower_sum += Z[i] * Z[i]
        p = upper_sum / lower_sum
        p_s_per_column.append(p)
    return p_s_per_column
def calculate_z_s_per_row(data, P):
    z_s_per_row = []
    for n in range(data.shape[0]):
        upper_sum, lower_sum = 0, 0
        for i in range(len(P)):
            if np.isnan(data[n, :][i]):
                continue
            upper_sum += P[i] * data[n, :][i]
            lower_sum += P[i] * P[i]
        z = upper_sum / lower_sum
        z_s_per_row.append(z)
    return z_s_per_row
def calculate_R_2(data, variance_rawdata):
    variance_new_data = np.nansum(data * data)
    return 1 - variance_new_data / variance_rawdata
def calculate_R_k_2(data, column_variance_rawdata):
    new_R_k_2 = [1 - np.nansum(data[:, i] * data[:, i]) / column_variance_rawdata[i] for i in range(data.shape[1])]
    return new_R_k_2
def calculate_SPE(data):
    new_SPE = [sqrt(np.dot(data[i].reshape(data[0].shape[0], 1).T, data[i].reshape(data[0].shape[0], 1)))
               if np.isnan(sqrt(np.dot(data[i].reshape(data[0].shape[0], 1).T, data[i].reshape(data[0].shape[0], 1))))
               else sqrt(np.nansum(data[i]**2)) for i in range(data.shape[0])]
    return new_SPE
def calculate_T_2(Z, T_2):
    new_T_2 = []
    if not T_2:
        s_a = np.std(Z)
        new_T_2 = [(Z[0][i] / s_a)**2 for i in range(Z.shape[1])]
    else:
        add_to_this = len(T_2) - 1
        s_a = np.std(Z)
        new_T_2 = [T_2[add_to_this][i] + (Z[0][i] / s_a)**2 for i in range(Z.shape[1])]
    return new_T_2
def create_matrices(Z_s, P_s, r_s, number_of_components):
    P_merged = np.concatenate((P_s[0], P_s[1]), axis=0)
    Z_merged = np.concatenate((Z_s[0], Z_s[1]), axis=0)
    r_merged = np.concatenate((r_s[0], r_s[1]), axis=0)
    for i in range(2, number_of_components):
        P_merged = np.concatenate((P_merged, P_s[i]), axis=0)
        Z_merged = np.concatenate((Z_merged, Z_s[i]), axis=0)
        r_merged = np.concatenate((r_merged, r_s[i]), axis=0)
    return Z_merged, P_merged, r_merged