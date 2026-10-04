import os
import time
from tqdm import tqdm
from huffman_module import *
from comp_lib import *
def fonk1():
    os.system('cls' if os.b1 = = 'nt' else 'clear')
def fonk2():
    fonk1()
    hepia_print()
    print("\n")
    b2 = '{l_bar}{bar}| {n_fmt}/{total_fmt}'
    a1 = 9
    with tqdm(b3 = a1, ncols=80, b2=b2) as pbar:
        b4 = read_user_input()
        pbar.set_description('Open File  ')
        pbar.update(1)
        b5 = b4[0]
        b6 = b4[1]
        b7 = bytes_2_array(b5)
        pbar.set_description('File->Array')
        pbar.update(1)
        b8 = hashOriginal(b5)
        pbar.set_description('Hashing    ')
        pbar.update(1)
        b9 = determine_frequencies(b7)
        pbar.set_description('Frequencies')
        pbar.update(1)
        b10 = huffman(b9)
        pbar.set_description('Huffman    ')
        pbar.update(1)
        b11 = translate(b7, b10)
        pbar.set_description('Translation')
        pbar.update(1)
        b12 = finalize(b11)
        pbar.set_description('Array->File')
        pbar.update(1)
        write_2_json(b10, "dict.json")
        pbar.set_description('dict.json  ')
        pbar.update(1)
        write_2_binary(b12, b6)
        pbar.set_description('Done       ')
        pbar.update(1)
        time.sleep(0.1)
    compressor_display(b9, b10, b5, b6, b7, b8)
if b13 = = "__main__":
    fonk2()