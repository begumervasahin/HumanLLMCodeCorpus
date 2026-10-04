import os
import time
from tqdm import tqdm
from decomp_lib import *
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    clear_console()
    hepia_print()
    print("\n")
    bar_format = '{l_bar}{bar}| {n_fmt}/{total_fmt}'
    tasks = [
        ('Open File  ', read_user_input),
        ('File->Array', lambda: bytes_2_array(filenames[0])),
        ('Json Read  ', lambda: json_2_dict(filenames[1])),
        ('Strip Zeros', lambda: strip_zeros(byte_array)),
        ('Retranslate', lambda: retranslate(byte_string_no_zeros, dictionary)),
        ('Done       ', lambda: write_2_binary(retranslated_byte_array, filenames[2]))
    ]
    with tqdm(total=len(tasks), ncols=80, bar_format=bar_format) as pbar:
        filenames = tasks[0][1]()
        pbar.set_description(tasks[0][0])
        pbar.update(1)
        byte_array = tasks[1][1]()
        pbar.set_description(tasks[1][0])
        pbar.update(1)
        dictionary = tasks[2][1]()
        pbar.set_description(tasks[2][0])
        pbar.update(1)
        byte_string_no_zeros = tasks[3][1]()
        pbar.set_description(tasks[3][0])
        pbar.update(1)
        retranslated_byte_array = tasks[4][1]()
        pbar.set_description(tasks[4][0])
        pbar.update(1)
        tasks[5][1]()
        pbar.set_description(tasks[5][0])
        pbar.update(1)
        time.sleep(0.1)
    decompressor_display(filenames[2])
if __name__ == "__main__":
    main()