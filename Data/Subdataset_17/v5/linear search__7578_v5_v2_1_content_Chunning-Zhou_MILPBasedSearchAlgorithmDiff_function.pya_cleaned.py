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
    def generate_input_state(self, goal=None):
        pass
    def state_through_sbox(self, round_num, goal=None):
        pass
    def state_through_permutation(self, state, goal=None):
        pass
    def state_through_xor(self, round_num, goal=None):
        pass
def generate_file_folder(cipher_name, goal):
    folder_name = f"{cipher_name}_{goal}"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created.")
    else:
        print(f"Folder '{folder_name}' already exists.")
def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File '{filename}' removed.")
    else:
        print(f"File '{filename}' does not exist.")
def diff_propagation_sbox_LBAS_bit(sbox_size, branch_num_of_sbox, model_filename, var):
    pass
if __name__ == "__main__":
    cipher = Cipher(
        name="example_cipher",
        nibble=16,
        round_of_first_region2=8,
        var_and_num_AS={},
        var_and_num_DC={}
    )
    generate_file_folder(cipher_name="example_cipher", goal="AS")
    remove_file("example_file.txt")
    cipher.generate_input_state(goal="AS")
    cipher.state_through_sbox(round_num=1, goal="AS")
    cipher.state_through_permutation(state={}, goal="AS")
    cipher.state_through_xor(round_num=1, goal="AS")
    diff_propagation_sbox_LBAS_bit(sbox_size=4, branch_num_of_sbox=2, model_filename="model.txt", var={})