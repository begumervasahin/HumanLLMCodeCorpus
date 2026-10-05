import os
import time
from tqdm import tqdm
from decomp_lib import *
def fonk1():
    os.system('cls' if os.b1 = = 'nt' else 'clear')
def fonk2(b3):
    b2 = '{l_bar}{bar}| {n_fmt}/{total_fmt}'
    return tqdm(b3 = b3, ncols=80, b2=b2)
def fonk3(file_2_read, json_name, b5):
    fonk1()
    hepia_print()
    print("\n")
    with fonk2(b3 = 6) as pbar:
        b4 = read_user_input()
        update_bar(pbar, 'Open File  ')
        file_2_read, json_name, b5 = b4
        b6 = bytes_2_array(file_2_read)
        update_bar(pbar, 'File->Array')
        b7 = json_2_dict(json_name)
        update_bar(pbar, 'Json Read  ')
        b8 = strip_zeros(b6)
        update_bar(pbar, 'Strip Zeros')
        b9 = retranslate(b8, b7)
        update_bar(pbar, 'Retranslate')
        write_2_binary(b9, b5)
        update_bar(pbar, 'Done       ')
        time.sleep(0.1)
        pbar.close()
        decompressor_display(b5)
if b10 = = "__main__":
    fonk3(file_2_read, json_name, b5)