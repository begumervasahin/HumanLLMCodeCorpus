
from huffman_module import *
from comp_lib import *
from tqdm import tqdm
import os
import time
os.system('cls' if os.b1 = = 'nt' else 'clear')
hepia_print()
print("\n")
b2 = '{l_bar}{bar}| {n_fmt}/{total_fmt}'
def fonk1(b12):
    with tqdm(b3 = 9, ncols=80, b2=b2) as pbar:
        update_bar(pbar, 'Open File  ')
        file_2_read, b4 = b12
        b5 = bytes_2_array(file_2_read)
        update_bar(pbar, 'File->Array')
        b6 = hashOriginal(file_2_read)
        update_bar(pbar, 'Hashing    ')
        b7 = determine_frequencies(b5)
        update_bar(pbar, 'Frequencies')
        b8 = huffman(b7)
        update_bar(pbar, 'Huffman    ')
        b9 = translate(b5, b8)
        update_bar(pbar, 'Translation')
        b10 = finalize(b9)
        update_bar(pbar, 'Array->File')
        write_2_json(b8, "dict.json")
        update_bar(pbar, 'dict.json  ')
        write_2_binary(b10, b4)
        update_bar(pbar, 'Done       ')
        time.sleep(0.1)
        pbar.close()
        compressor_display(b7, b8, file_2_read, b4, b5, b6)
if b11 = = "__main__":
    b12 = read_user_input()
    fonk1(b12)