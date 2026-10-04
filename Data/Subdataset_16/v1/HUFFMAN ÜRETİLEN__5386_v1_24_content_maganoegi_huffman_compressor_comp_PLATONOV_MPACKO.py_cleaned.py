import os
import time
from tqdm import tqdm
from huffman_module import *
from comp_lib import *
def fonk1(pbar, task_name):
    pbar.set_description(f'{task_name}')
    pbar.update(1)
def fonk2():
    os.system('cls' if os.b1 = = 'nt' else 'clear')
    hepia_print()
    print("\n")
    b2 = '{l_bar}{bar}| {n_fmt}/{total_fmt}'
    with tqdm(b3 = 9, ncols=80, b2=b2) as pbar:
        b4 = read_user_input()
        fonk1(pbar, 'Open File  ')
        b5 = b4[0]
        b6 = b4[1]
        b7 = bytes_2_array(b5)
        fonk1(pbar, 'File->Array')
        b8 = hashOriginal(b5)
        fonk1(pbar, 'Hashing    ')
        b9 = determine_frequencies(b7)
        fonk1(pbar, 'Frequencies')
        b10 = huffman(b9)
        fonk1(pbar, 'Huffman    ')
        b11 = translate(b7, b10)
        fonk1(pbar, 'Translation')
        b12 = finalize(b11)
        fonk1(pbar, 'Array->File')
        write_2_json(b10, "dict.json")
        fonk1(pbar, 'dict.json  ')
        write_2_binary(b12, b6)
        fonk1(pbar, 'Done       ')
        time.sleep(0.1)
        pbar.close()
        compressor_display(b9, b10, b5, b6, b7, b8)
if b13 = = "__main__":
    fonk2()