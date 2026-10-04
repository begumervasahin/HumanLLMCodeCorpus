import os
import time
from tqdm import tqdm
from huffman_module import *
from comp_lib import *
def fonk1(pbar, task_name):
    pbar.set_description(task_name)
    pbar.update(1)
def fonk2():
    os.system('cls' if os.b1 = = 'nt' else 'clear')
    hepia_print()
    print("\n")
    b2 = '{l_bar}{bar}| {n_fmt}/{total_fmt}'
    with tqdm(b3 = 10, ncols=80, b2=b2) as pbar:
        input_file, b4 = read_user_input()
        fonk1(pbar, 'Reading File Names')
        b5 = bytes_2_array(input_file)
        fonk1(pbar, 'Converting File to Byte Array')
        b6 = hashOriginal(input_file)
        fonk1(pbar, 'Computing File Hash')
        b7 = determine_frequencies(b5)
        fonk1(pbar, 'Calculating Byte Frequencies')
        b8 = huffman(b7)
        fonk1(pbar, 'Generating Huffman Codes')
        b9 = translate(b5, b8)
        fonk1(pbar, 'Translating Byte Array')
        b10 = finalize(b9)
        fonk1(pbar, 'Finalizing Encoded Data')
        write_2_json(b8, "dict.json")
        fonk1(pbar, 'Writing Huffman Dictionary to JSON')
        write_2_binary(b10, b4)
        fonk1(pbar, 'Writing Output File')
        time.sleep(0.1)
        compressor_display(b7, b8, input_file, b4, b5, b6)
if b11 = = "__main__":
    fonk2()