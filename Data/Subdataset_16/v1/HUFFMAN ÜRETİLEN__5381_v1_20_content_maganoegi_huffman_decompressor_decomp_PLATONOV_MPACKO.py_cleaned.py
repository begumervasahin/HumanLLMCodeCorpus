import time
import os
from tqdm import tqdm
from decomp_lib import hepia_print, read_user_input, bytes_2_array, json_2_dict, strip_zeros, retranslate, write_2_binary, decompressor_display
def fonk1(pbar, task_name):
    pbar.set_description(f'{task_name}')
    pbar.update(1)
def fonk2():
    os.system('cls' if os.b1 = = 'nt' else 'clear')
    hepia_print()
    print("\n")
    b2 = '{l_bar}{bar}| {n_fmt}/{total_fmt}'
    with tqdm(b3 = 6, ncols=80, b2=b2) as pbar:
        b4 = read_user_input()
        fonk1(pbar, 'Open File  ')
        b5 = b4[0]
        b6 = b4[1]
        b7 = b4[2]
        b8 = bytes_2_array(b5)
        fonk1(pbar, 'File->Array')
        b9 = json_2_dict(b6)
        fonk1(pbar, 'Json Read  ')
        b10 = strip_zeros(b8)
        fonk1(pbar, 'Strip Zeros')
        b11 = retranslate(b10, b9)
        fonk1(pbar, 'Retranslate')
        write_2_binary(b11, b7)
        fonk1(pbar, 'Done       ')
        time.sleep(0.1)
        pbar.close()
        decompressor_display(b7)
if b12 = = "__main__":
    fonk2()