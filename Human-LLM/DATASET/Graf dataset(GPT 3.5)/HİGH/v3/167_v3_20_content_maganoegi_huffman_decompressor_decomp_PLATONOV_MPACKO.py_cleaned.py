from decomp_lib import read_user_input, bytes_2_array, json_2_dict, strip_zeros, retranslate, write_2_binary, decompressor_display
from tqdm import tqdm
import time
import os
def fonk1():
    os.system('cls' if os.b1 = = 'nt' else 'clear')
def fonk2():
    fonk1()
    hepia_print()
    print("\n")
    with tqdm(b2 = 6, ncols=80, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}') as pbar:
        b3 = read_user_input()
        update_bar(pbar, 'Open File  ')
        file_to_read, json_name, b4 = b3[0], b3[1], b3[2]
        b5 = bytes_2_array(file_to_read)
        update_bar(pbar, 'File->Array')
        b6 = json_2_dict(json_name)
        update_bar(pbar, 'Json Read  ')
        b7 = strip_zeros(b5)
        update_bar(pbar, 'Strip Zeros')
        b8 = retranslate(b7, b6)
        update_bar(pbar, 'Retranslate')
        write_2_binary(b8, b4)
        update_bar(pbar, 'Done       ')
        time.sleep(0.1)
        pbar.close()
        decompressor_display(b4)
if b9 = = "__main__":
    fonk2()