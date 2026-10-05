from IDAPICourseworkLibrary import ImportData, Discretise
import numpy as np
def calculate_prior(the_data, root_index, num_states):
    prior = np.zeros((num_states[root_index]), dtype=float)
    data_amount = len(the_data[:, 0])
    for i in range(data_amount):
        prior[the_data[i, root_index]] += 1
    prior /= data_amount
    return prior
def calculate_cpt(the_data, parent_index, child_index, num_states):
    data_amount = len(the_data[:, 0])
    cpt = np.zeros((num_states[parent_index], num_states[child_index]), dtype=float)
    for row in range(data_amount):
        cpt[the_data[row, parent_index]][the_data[row, child_index]] += 1
    for i in range(num_states[child_index]):
        alpha = (np.sum(the_data[:, child_index] == i))
        if alpha != 0:
            cpt[:, i] /= (np.sum(the_data[:, child_index] == i))
    return cpt
def calculate_jpt(the_data, row_index, col_index, num_states):
    jpt = np.zeros((num_states[row_index], num_states[col_index]), dtype=float)
    data_amount = len(the_data[:, 0])
    for row in range(data_amount):
        jpt[the_data[row, row_index]][the_data[row, col_index]] += 1
    jpt /= data_amount
    return jpt
def convert_jpt_to_cpt(jpt):
    for i in range(len(jpt[0, :])):
        alpha = (np.sum(jpt[:, i]))
        if alpha != 0:
            jpt[:, i] *= 1 / alpha
    return jpt
def query_naive_bayes(the_query, naive_bayes):
    root_pdf = np.zeros((naive_bayes[0].shape[0]), dtype=float)
    for i in range(len(root_pdf)):
        root_pdf[i] = naive_bayes[0][i]
        for j in range(len(the_query)):
            root_pdf[i] *= naive_bayes[j + 1][the_query[j], i]
    if np.sum(root_pdf) != 0:
        root_pdf *= 1 / np.sum(root_pdf)
    else:
        root_pdf = np.ones((naive_bayes[0].shape[0]), dtype=float) / naive_bayes[0].shape[0]
    return root_pdf
def calculate_mutual_information(jpt):
    mi = 0.0
    num_cols = len(jpt[0, :])
    num_rows = len(jpt[:, 0])
    col_sum = np.zeros(num_cols, dtype=float)
    for j in range(num_cols):
        col_sum[j] = np.sum(jpt[:, j])
    for i in range(num_rows):
        row_sum = np.sum(jpt[i, :])
        for j in range(num_cols):
            if jpt[i][j] != 0:
                mi += jpt[i][j] * np.log2(jpt[i][j] / (row_sum * col_sum[j]))
    return mi
the_data = ImportData("IDAPICourseworkData.csv", ",")
the_data = Discretise(the_data, [5, 5, 5, 5, 5, 5, 5], ["s", "s", "s", "s", "s", "s", "c"])
num_states = [5, 5, 5, 5, 5, 5, 5]
prior_a = calculate_prior(the_data, 0, num_states)
prior_b = calculate_prior(the_data, 1, num_states)
prior_c = calculate_prior(the_data, 2, num_states)
prior_d = calculate_prior(the_data, 3, num_states)
prior_e = calculate_prior(the_data, 4, num_states)
prior_f = calculate_prior(the_data, 5, num_states)
prior_g = calculate_prior(the_data, 6, num_states)
cpt_ab = calculate_cpt(the_data, 0, 1, num_states)
cpt_bc = calculate_cpt(the_data, 1, 2, num_states)
cpt_cd = calculate_cpt(the_data, 2, 3, num_states)
cpt_de = calculate_cpt(the_data, 3, 4, num_states)
cpt_ef = calculate_cpt(the_data, 4, 5, num_states)
cpt_fg = calculate_cpt(the_data, 5, 6, num_states)
jpt_ab = calculate_jpt(the_data, 0, 1, num_states)
jpt_bc = calculate_jpt(the_data, 1, 2, num_states)
jpt_cd = calculate_jpt(the_data, 2, 3, num_states)
jpt_de = calculate_jpt(the_data, 3, 4, num_states)
jpt_ef = calculate_jpt(the_data, 4, 5, num_states)
jpt_fg = calculate_jpt(the_data, 5, 6, num_states)
cpt_ab2 = convert_jpt_to_cpt(jpt_ab)
cpt_bc2 = convert_jpt_to_cpt(jpt_bc)
cpt_cd2 = convert_jpt_to_cpt(jpt_cd)
cpt_de2 = convert_jpt_to_cpt(jpt_de)
cpt_ef2 = convert_jpt_to_cpt(jpt_ef)
cpt_fg2 = convert_jpt_to_cpt(jpt_fg)
naive_bayes_model = [prior_a, cpt_ab2, cpt_bc2, cpt_cd2, cpt_de2, cpt_ef2, cpt_fg2]
query = [1, 3, 2, 4, 2, 1]
query_result = query_naive_bayes(query, naive_bayes_model)
print("Result of query:", query_result)
mi_ab = calculate_mutual_information(jpt_ab)
mi_bc = calculate_mutual_information(jpt_bc)
mi_cd = calculate_mutual_information(jpt_cd)
mi_de = calculate_mutual_information(jpt_de)
mi_ef = calculate_mutual_information(jpt_ef)
mi_fg = calculate_mutual_information(jpt_fg)
print("Mutual Information between A and B:", mi_ab)
print("Mutual Information between B and C:", mi_bc)
print("Mutual Information between C and D:", mi_cd)
print("Mutual Information between D and E:", mi_de)
print("Mutual Information between E and F:", mi_ef)
print("Mutual Information between F and G:", mi_fg)