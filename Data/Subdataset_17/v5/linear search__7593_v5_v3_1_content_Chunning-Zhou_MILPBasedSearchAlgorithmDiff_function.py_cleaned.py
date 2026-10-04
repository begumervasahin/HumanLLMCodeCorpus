import os
import shutil
from itertools import combinations
class Cipher:
    def __init__(self, name, nibble, round_of_first_region2, var_and_num_AS, var_and_num_DC):
        self.name = name
        self.nibble = nibble
        self.round_of_first_region2 = round_of_first_region2
        self.var_and_num_AS = var_and_num_AS
        self.var_and_num_DC = var_and_num_DC
    def gen_input_state(self, goal=None):
        pass
    def get_state_through_sbox(self, round_num, goal=None):
        pass
    def get_state_through_per(self, state, goal=None):
        pass
    def get_state_through_xor(self, round_num, goal=None):
        pass
def gen_filefolder(cipher_name, goal):
    folder_path = f"{cipher_name}_{goal}"
    os.makedirs(folder_path, exist_ok=True)
def remove_file(filename):
    if os.path.isfile(filename):
        os.remove(filename)
def diff_propagation_of_sbox_LBAS_bit(sbox_size, branch_num_of_sbox, model_filename, var):
    pass
if __name__ == "__main__":
    cipher = Cipher(
        name="example_cipher",
        nibble=16,
        round_of_first_region2=8,
        var_and_num_AS={},
        var_and_num_DC={}
    )
    gen_filefolder(cipher_name="example_cipher", goal="AS")
    remove_file("example_file.txt")
