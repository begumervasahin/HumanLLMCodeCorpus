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
def update_progress_bar(pbar, task_name):
    pbar.set_description(f'{task_name}')
    pbar.update(1)
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    hepia_print()
    print("\n")
    bar_format = '{l_bar}{bar}| {n_fmt}/{total_fmt}'
    with tqdm(total=6, ncols=80, bar_format=bar_format) as pbar:
        filenames = read_user_input()
        update_progress_bar(pbar, 'Reading Input Files')
        input_filename, json_filename, output_filename = filenames
        byte_array = bytes_2_array(input_filename)
        update_progress_bar(pbar, 'Converting File to Array')
        dictionary = json_2_dict(json_filename)
        update_progress_bar(pbar, 'Reading JSON Dictionary')
        byte_string_no_zeros = strip_zeros(byte_array)
        update_progress_bar(pbar, 'Stripping Zeros')
        retranslated_byte_array = retranslate(byte_string_no_zeros, dictionary)
        update_progress_bar(pbar, 'Retranslating Byte Array')
        write_2_binary(retranslated_byte_array, output_filename)
        update_progress_bar(pbar, 'Writing Output File')
        time.sleep(0.1)
        decompressor_display(output_filename)
if __name__ == "__main__":
    main()