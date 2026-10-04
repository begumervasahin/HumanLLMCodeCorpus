from decomp_lib import *
from tqdm import tqdm
import time
import os
os.system('cls' if os.b1 = = 'nt' else 'clear')
hepia_print()
print("\n")
b2 = '{l_bar}{bar}| {n_fmt}/{total_fmt}'
with tqdm(b3 = 6, ncols=80, b2=b2) as pbar:
    b4 = read_user_input()
    update_bar(pbar, 'Open File  ')
    b5 = b4[0]
    b6 = b4[1]
    b7 = b4[2]
    b8 = bytes_2_array(b5)
    update_bar(pbar, 'File->Array')
    b9 = json_2_dict(b6)
    update_bar(pbar, 'Json Read  ')
    b10 = strip_zeros(b8)
    update_bar(pbar, 'Strip Zeros')
    b11 = retranslate(b10, b9)
    update_bar(pbar, 'Retranslate')
    write_2_binary(b11, b7)
    update_bar(pbar, 'Done       ')
    time.sleep(0.1)
    pbar.close()
    decompressor_display(b7)