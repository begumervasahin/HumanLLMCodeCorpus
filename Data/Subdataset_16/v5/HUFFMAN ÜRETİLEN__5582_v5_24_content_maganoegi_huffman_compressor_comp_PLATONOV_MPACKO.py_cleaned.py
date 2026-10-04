import os
import time
from tqdm import tqdm
from huffman_module import *
from comp_lib import *
def fonk1():
    os.system('cls' if os.b1 = = 'nt' else 'clear')
def fonk2(description, task, pbar):
    pbar.set_description(description)
    b2 = task()
    pbar.update(1)
    return b2
def fonk3():
    fonk1()
    hepia_print()
    print("\n")
    b3 = '{l_bar}{bar}| {n_fmt}/{total_fmt}'
    a1 = 9
    with tqdm(b4 = a1, ncols=80, b3=b3) as pbar:
        b5 = fonk2('Open File  ', read_user_input, pbar)
        file_to_read, b6 = b5
        b7 = fonk2('File->Array', lambda: bytes_2_array(file_to_read), pbar)
        b8 = fonk2('Hashing    ', lambda: hashOriginal(file_to_read), pbar)
        b9 = fonk2('Frequencies', lambda: determine_frequencies(b7), pbar)
        b10 = fonk2('Huffman    ', lambda: huffman(b9), pbar)
        b11 = fonk2('Translation', lambda: translate(b7, b10), pbar)
        b12 = fonk2('Array->File', lambda: finalize(b11), pbar)
        fonk2('dict.json  ', lambda: write_2_json(b10, "dict.json"), pbar)
        fonk2('Done       ', lambda: write_2_binary(b12, b6), pbar)
        time.sleep(0.1)
    compressor_display(b9, b10, file_to_read, b6, b7, b8)
if b13 = = "__main__":
    fonk3()