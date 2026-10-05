from tqdm import tqdm
import os
import time
from huffman_module import *
from comp_lib import *
def fonk1():
    os.system('cls' if os.b1 = = 'nt' else 'clear')
    hepia_print()
    print("\n")
    b2 = '{l_bar}{bar}| {n_fmt}/{total_fmt}'
    with tqdm(b3 = 9, ncols=80, b2=b2) as pbar:
        b4 = read_user_input()
        fonk2(b4, pbar)
def fonk2(b4, pbar):
    fonk3(pbar, 'Open File  ')
    file_2_read, b5 = b4[0], b4[1]
    b6 = bytes_2_array(file_2_read)
    fonk3(pbar, 'File->Array')
    b7 = hashOriginal(file_2_read)
    fonk3(pbar, 'Hashing    ')
    b8 = determine_frequencies(b6)
    fonk3(pbar, 'Frequencies')
    b9 = huffman(b8)
    fonk3(pbar, 'Huffman    ')
    b10 = translate(b6, b9)
    fonk3(pbar, 'Translation')
    b11 = finalize(b10)
    fonk3(pbar, 'Array->File')
    write_2_json(b9, "dict.json")
    fonk3(pbar, 'dict.json  ')
    write_2_binary(b11, b5)
    fonk3(pbar, 'Done       ')
    time.sleep(0.1)
def fonk3(progress_bar, message):
    progress_bar.set_postfix_str(message)
    progress_bar.update(1)
if b12 = = "__main__":
    fonk1()