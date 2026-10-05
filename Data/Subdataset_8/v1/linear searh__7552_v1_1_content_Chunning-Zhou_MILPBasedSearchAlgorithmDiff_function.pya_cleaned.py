import os
import re
from itertools import combinations
import shutil
class Cipher:
    def __init__(self, name, nibble, round_of_first_region2, var_and_num_AS, var_and_num_DC):
    def gen_input_state(self, goal=None):
    def get_state_through_sbox(self, round_num, goal=None):
    def get_state_through_per(self, state, goal=None):
    def get_state_through_xor(self, round_num, goal=None):
def gen_filefolder(cipher_name, goal):
def remove_file(filename):
def diff_propagation_of_sbox_LBAS_bit(sbox_size, branch_num_of_sbox, model_filename, var):
if __name__ == "__main__":
    cipher = Cipher(...)
    gen_filefolder("example_cipher", "AS")
    remove_file("example_file.txt")
    get_trail_sp(cipher, "AS", 5)
    get_trail_feistel(cipher, "DC", 5)
