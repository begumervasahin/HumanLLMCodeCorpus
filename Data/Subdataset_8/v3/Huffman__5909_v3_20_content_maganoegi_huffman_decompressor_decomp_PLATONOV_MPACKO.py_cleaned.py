from decomp_lib import read_user_input, bytes_2_array, json_2_dict, strip_zeros, retranslate, write_2_binary, decompressor_display
from tqdm import tqdm
import time
import os
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    clear_console()
    hepia_print()
    print("\n")
    with tqdm(total=6, ncols=80, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}') as pbar:
        filenames = read_user_input()
        update_bar(pbar, 'Open File  ')
        file_to_read, json_name, file_to_write = filenames[0], filenames[1], filenames[2]
        byte_array = bytes_2_array(file_to_read)
        update_bar(pbar, 'File->Array')
        dict_ = json_2_dict(json_name)
        update_bar(pbar, 'Json Read  ')
        byte_string_no_zeros = strip_zeros(byte_array)
        update_bar(pbar, 'Strip Zeros')
        retranslated_byte_array = retranslate(byte_string_no_zeros, dict_)
        update_bar(pbar, 'Retranslate')
        write_2_binary(retranslated_byte_array, file_to_write)
        update_bar(pbar, 'Done       ')
        time.sleep(0.1)
        pbar.close()
        decompressor_display(file_to_write)
if __name__ == "__main__":
    main()