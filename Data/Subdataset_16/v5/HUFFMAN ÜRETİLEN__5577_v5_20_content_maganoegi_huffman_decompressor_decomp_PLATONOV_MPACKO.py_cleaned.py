import os
import time
from tqdm import tqdm
from decomp_lib import *
def fonk1():
    os.system('cls' if os.b1 = = 'nt' else 'clear')
def fonk2(task_name, task_function, pbar):
    pbar.set_description(task_name)
    b2 = task_function()
    pbar.update(1)
    return b2
def fonk3():
    fonk1()
    hepia_print()
    print("\n")
    b3 = '{l_bar}{bar}| {n_fmt}/{total_fmt}'
    b4 = [
        ('Open File  ', read_user_input),
        ('File->Array', lambda: bytes_2_array(b6[0])),
        ('Json Read  ', lambda: json_2_dict(b6[1])),
        ('Strip Zeros', lambda: strip_zeros(b7)),
        ('Retranslate', lambda: retranslate(b9, b8)),
        ('Done       ', lambda: write_2_binary(b10, b6[2]))
    ]
    with tqdm(b5 = len(b4), ncols=80, b3=b3) as pbar:
        b6 = fonk2(b4[0][0], b4[0][1], pbar)
        b7 = fonk2(b4[1][0], b4[1][1], pbar)
        b8 = fonk2(b4[2][0], b4[2][1], pbar)
        b9 = fonk2(b4[3][0], b4[3][1], pbar)
        b10 = fonk2(b4[4][0], b4[4][1], pbar)
        fonk2(b4[5][0], b4[5][1], pbar)
        time.sleep(0.1)
    decompressor_display(b6[2])
if b11 = = "__main__":
    fonk3()