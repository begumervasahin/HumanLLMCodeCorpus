import os
import re
import shutil
from itertools import combinations
import copy
import numpy as np
def generate_file_folders(cipher_name, goal):
    folders = ["LBAS", goal, f"{goal}/optimal_solution_of_submodel"]
    for folder in folders:
        file_folder = f"model/{cipher_name}/{folder}/"
        if not os.path.isdir(file_folder):
            os.makedirs(file_folder)
        file_folder = f"result/{cipher_name}/{folder}/"
        if not os.path.isdir(file_folder):
            os.makedirs(file_folder)
def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
def diff_propagation_sbox_LBAS_bit(sbox_size, branch_num_of_sbox, model_filename, var):
def diff_propagation_sbox_AS(sbox_size, model_filename, var, ine):
def diff_propagation_sbox_DC(sbox_size, num_of_p_var, model_filename, var, ine):
def diff_propagation_xor_word(model_filename, var):
def diff_propagation_xor_bit(model_filename, var):
def get_order_of_Na(cipher, r):
def get_value(r, value):
def get_search_round(r):
def transform_diff_pattern(cipher, Na):
def read_txt(filename):
def get_vars_from_two_submodels(cipher, goal, r, Na, i, diff):
def get_trail_sp(cipher, goal, r):
def get_trail_feistel(cipher, goal, r):
