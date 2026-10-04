import os
import time
from tqdm import tqdm
from decomp_lib import *
def fonk1():
    os.system('cls' if os.b1 = = 'nt' else 'clear')
def fonk2():
    fonk1()
    hepia_print()
    print("\n")
    b2 = '{l_bar}{bar}| {n_fmt}/{total_fmt}'
    b3 = [
        ('Open File  ', read_user_input),
        ('File->Array', lambda: bytes_2_array(b5[0])),
        ('Json Read  ', lambda: json_2_dict(b5[1])),
        ('Strip Zeros', lambda: strip_zeros(b6)),
        ('Retranslate', lambda: retranslate(b8, b7)),
        ('Done       ', lambda: write_2_binary(b9, b5[2]))
    ]
    with tqdm(b4 = len(b3), ncols=80, b2=b2) as pbar:
        b5 = b3[0][1]()
        pbar.set_description(b3[0][0])
        pbar.update(1)
        b6 = b3[1][1]()
        pbar.set_description(b3[1][0])
        pbar.update(1)
        b7 = b3[2][1]()
        pbar.set_description(b3[2][0])
        pbar.update(1)
        b8 = b3[3][1]()
        pbar.set_description(b3[3][0])
        pbar.update(1)
        b9 = b3[4][1]()
        pbar.set_description(b3[4][0])
        pbar.update(1)
        b3[5][1]()
        pbar.set_description(b3[5][0])
        pbar.update(1)
        time.sleep(0.1)
    decompressor_display(b5[2])
if b10 = = "__main__":
    fonk2()