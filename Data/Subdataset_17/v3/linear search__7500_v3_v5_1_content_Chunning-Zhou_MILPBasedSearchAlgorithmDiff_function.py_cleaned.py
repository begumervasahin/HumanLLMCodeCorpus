import os
import numpy as np
def generate_file_folders(cipher_name, goal):
    folders = ["LBAS", goal, f"{goal}/optimal_solution_of_submodel"]
    for folder in folders:
        for base in ["model", "result"]:
            path = os.path.join(base, cipher_name, folder)
            if not os.path.isdir(path):
                os.makedirs(path)
                print(f"Created directory: {path}")
def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Removed file: {filename}")
def diff_propagation_sbox_LBAS_bit(sbox_size, branch_num_of_sbox, model_filename, var):
    print(f"Called: diff_propagation_sbox_LBAS_bit with sbox_size={sbox_size}, branch_num_of_sbox={branch_num_of_sbox}, model_filename={model_filename}, var={var}")
def diff_propagation_sbox_AS(sbox_size, model_filename, var, ine):
    print(f"Called: diff_propagation_sbox_AS with sbox_size={sbox_size}, model_filename={model_filename}, var={var}, ine={ine}")
def diff_propagation_sbox_DC(sbox_size, num_of_p_var, model_filename, var, ine):
    print(f"Called: diff_propagation_sbox_DC with sbox_size={sbox_size}, num_of_p_var={num_of_p_var}, model_filename={model_filename}, var={var}, ine={ine}")
def diff_propagation_xor_word(model_filename, var):
    print(f"Called: diff_propagation_xor_word with model_filename={model_filename}, var={var}")
def diff_propagation_xor_bit(model_filename, var):
    print(f"Called: diff_propagation_xor_bit with model_filename={model_filename}, var={var}")
def get_order_of_Na(cipher, r):
    print(f"Called: get_order_of_Na with cipher={cipher}, r={r}")
def get_value(r, value):
    print(f"Called: get_value with r={r}, value={value}")
def get_search_round(r):
    print(f"Called: get_search_round with r={r}")
def transform_diff_pattern(cipher, Na):
    print(f"Called: transform_diff_pattern with cipher={cipher}, Na={Na}")
def read_txt(filename):
    print(f"Called: read_txt with filename={filename}")
def get_vars_from_two_submodels(cipher, goal, r, Na, i, diff):
    print(f"Called: get_vars_from_two_submodels with cipher={cipher}, goal={goal}, r={r}, Na={Na}, i={i}, diff={diff}")
def get_trail_sp(cipher, goal, r):
    print(f"Called: get_trail_sp with cipher={cipher}, goal={goal}, r={r}")
def get_trail_feistel(cipher, goal, r):
    print(f"Called: get_trail_feistel with cipher={cipher}, goal={goal}, r={r}")
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