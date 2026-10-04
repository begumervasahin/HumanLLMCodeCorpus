import os
import shutil
from itertools import combinations
class Cipher:
    def __init__(self, name, nibble, rounds, var_num_as, var_num_dc):
        self.name = name
        self.nibble = nibble
        self.rounds = rounds
        self.var_num_as = var_num_as
        self.var_num_dc = var_num_dc
    def generate_input_state(self, goal=None):
        pass
    def state_through_sbox(self, round_num, goal=None):
        pass
    def state_through_permutation(self, state, goal=None):
        pass
    def state_through_xor(self, round_num, goal=None):
        pass
def create_file_folder(cipher_name, goal):
    folder_name = f"{cipher_name}_{goal}_files"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
def differential_propagation_of_sbox_lbas_bit(sbox_size, branch_num, model_filename, var):
    pass
def get_sp_trail(cipher, goal, round_num):
    pass
def get_feistel_trail(cipher, goal, round_num):
    pass
if __name__ == "__main__":
    cipher = Cipher(
        name="example_cipher",
        nibble=16,
        rounds=8,
        var_num_as={},
        var_num_dc={}
    )
    create_file_folder(cipher_name="example_cipher", goal="AS")
    delete_file("example_file.txt")
    get_sp_trail(cipher, goal="AS", round_num=5)
    get_feistel_trail(cipher, goal="DC", round_num=5)