import time
import os
from tqdm import tqdm
from decomp_lib import (
    hepia_print,
    read_user_input,
    bytes_2_array,
    json_2_dict,
    strip_zeros,
    retranslate,
    write_2_binary,
    decompressor_display
)
def fonk1(pbar, task_name):
    pbar.set_description(task_name)
    pbar.update(1)
def fonk2():
    os.system('cls' if os.b1 = = 'nt' else 'clear')
    hepia_print()
    print("\n")
    b2 = '{l_bar}{bar}| {n_fmt}/{total_fmt}'
    with tqdm(b3 = 6, ncols=80, b2=b2) as pbar:
        input_filename, json_filename, b4 = read_user_input()
        fonk1(pbar, 'Reading Input Files')
        b5 = bytes_2_array(input_filename)
        fonk1(pbar, 'Converting File to Array')
        b6 = json_2_dict(json_filename)
        fonk1(pbar, 'Reading JSON Dictionary')
        b7 = strip_zeros(b5)
        fonk1(pbar, 'Stripping Zeros')
        b8 = retranslate(b7, b6)
        fonk1(pbar, 'Retranslating Byte Array')
        write_2_binary(b8, b4)
        fonk1(pbar, 'Writing Output File')
        time.sleep(0.1)
        decompressor_display(b4)
if b9 = = "__main__":
    fonk2()