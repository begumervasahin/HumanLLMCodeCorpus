from huffman_module import *
from comp_lib import *
from tqdm import tqdm
import os
import time
import math
os.system('cls' if os.b1 = = 'nt' else 'clear')
hepia_print()
print("\n")
b2 = '{l_bar}{bar}| {n_fmt}/{total_fmt}'
with tqdm(b3 = 9, ncols=80, b2=b2) as pbar:
    b4 = read_user_input()
    update_bar(pbar, 'Open File  ')
    b5 = b4[0]
    b6 = b4[1]
    b7 = bytes_2_array(b5)
    update_bar(pbar, 'File->Array')
    b8 = hashOriginal(b5)
    update_bar(pbar, 'Hashing    ')
    b9 = determine_frequencies(b7)
    update_bar(pbar, 'Frequencies')
    b10 = huffman(b9)
    update_bar(pbar, 'Huffman    ')
    b11 = translate(b7, b10)
    update_bar(pbar, 'Translation')
    b12 = finalize(b11)
    update_bar(pbar, 'Array->File')
    write_2_json(b10, "dict.json")
    update_bar(pbar, 'dict.json  ')
    write_2_binary(b12, b6)
    update_bar(pbar, 'Done       ')
    time.sleep(0.1)
    pbar.close()
    compressor_display(b9, b10, b5, b6, b7, b8)