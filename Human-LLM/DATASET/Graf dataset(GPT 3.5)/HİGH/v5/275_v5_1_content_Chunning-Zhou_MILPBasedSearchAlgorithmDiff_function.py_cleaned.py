import os
import re
import shutil
from itertools import combinations
import copy
import numpy as np
def fonk1(cipher_name, goal):
    b1 = ["LBAS", goal, f"{goal}/optimal_solution_of_submodel"]
    for folder in b1:
        b2 = f"model/{cipher_name}/{folder}/"
        if not os.path.isdir(b2):
            os.makedirs(b2)
        b2 = f"result/{cipher_name}/{folder}/"
        if not os.path.isdir(b2):
            os.makedirs(b2)
def fonk2(filename):
    if os.path.exists(filename):
        os.remove(filename)
def fonk3(sbox_size, branch_num_of_sbox, model_filename, var):
def fonk4(sbox_size, model_filename, var, ine):
def fonk5(sbox_size, num_of_p_var, model_filename, var, ine):
def fonk6(model_filename, var):
def fonk7(model_filename, var):
def fonk8(cipher, r):
def fonk9(r, value):
def fonk10(r):
def fonk11(cipher, Na):
def fonk12(filename):
def fonk13(cipher, goal, r, Na, i, diff):
def fonk14(cipher, goal, r):
def fonk15(cipher, goal, r):
