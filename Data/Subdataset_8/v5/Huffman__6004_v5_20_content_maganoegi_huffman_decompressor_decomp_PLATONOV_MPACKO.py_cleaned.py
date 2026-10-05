import os
import time
from tqdm import tqdm
from decomp_lib import *
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
def initialize_progress_bar(total):
    bar_format = '{l_bar}{bar}| {n_fmt}/{total_fmt}'
    return tqdm(total=total, ncols=80, bar_format=bar_format)
def process_decompression(file_2_read, json_name, file_2_write):
    clear_console()
    hepia_print()
    print("\n")
    with initialize_progress_bar(total=6) as pbar:
        filenames = read_user_input()
        update_bar(pbar, 'Open File  ')
        file_2_read, json_name, file_2_write = filenames
        byte_array = bytes_2_array(file_2_read)
        update_bar(pbar, 'File->Array')
        dictionary = json_2_dict(json_name)
        update_bar(pbar, 'Json Read  ')
        byte_string_no_zeros = strip_zeros(byte_array)
        update_bar(pbar, 'Strip Zeros')
        retranslated_byte_array = retranslate(byte_string_no_zeros, dictionary)
        update_bar(pbar, 'Retranslate')
        write_2_binary(retranslated_byte_array, file_2_write)
        update_bar(pbar, 'Done       ')
        time.sleep(0.1)
        pbar.close()
        decompressor_display(file_2_write)
if __name__ == "__main__":
    process_decompression(file_2_read, json_name, file_2_write)