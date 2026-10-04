import os
import shutil
import numpy as np
def generate_file_folders(cipher_name, goal):
    folders = ["LBAS", goal, f"{goal}/optimal_solution_of_submodel"]
    for folder in folders:
        for base in ["model", "result"]:
            file_folder = f"{base}/{cipher_name}/{folder}/"
            if not os.path.isdir(file_folder):
                os.makedirs(file_folder)
def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
def diff_propagation_sbox_LBAS_bit(sbox_size, branch_num_of_sbox, model_filename, var):
    pass
def diff_propagation_sbox_AS(sbox_size, model_filename, var, ine):
    pass
def diff_propagation_sbox_DC(sbox_size, num_of_p_var, model_filename, var, ine):
    pass
def diff_propagation_xor_word(model_filename, var):
    pass
def diff_propagation_xor_bit(model_filename, var):
    pass
def get_order_of_Na(cipher, r):
    pass
def get_value(r, value):
    pass
def get_search_round(r):
    pass
def transform_diff_pattern(cipher, Na):
    pass
def read_txt(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content
def get_vars_from_two_submodels(cipher, goal, r, Na, i, diff):
    pass
def get_trail_sp(cipher, goal, r):
    pass
def get_trail_feistel(cipher, goal, r):
    pass
if __name__ == "__main__":
    cipher_name = "example_cipher"
    goal = "AS"
    r = 10
    generate_file_folders(cipher_name, goal)
    remove_file("example_file.txt")
    diff_propagation_sbox_AS(4, "example_model.txt", {"x": [1, 2], "A": 3}, np.array([[1, -1, 0], [0, 1, -1]]))
    get_order_of_Na(cipher_name, r)
    get_search_round(r)
    transform_diff_pattern(cipher_name, 2)
    read_txt("example_file.txt")
    get_vars_from_two_submodels(cipher_name, goal, r, 2, 1, "diff_pattern")
    get_trail_sp(cipher_name, goal, r)
    get_trail_feistel(cipher_name, goal, r)