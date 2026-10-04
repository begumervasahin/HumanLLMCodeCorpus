import os
import time
from tqdm import tqdm
from huffman_module import *
from comp_lib import *
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    clear_console()
    hepia_print()
    print("\n")
    bar_format = '{l_bar}{bar}| {n_fmt}/{total_fmt}'
    total_steps = 9
    with tqdm(total=total_steps, ncols=80, bar_format=bar_format) as pbar:
        filenames = read_user_input()
        pbar.set_description('Open File  ')
        pbar.update(1)
        file_to_read = filenames[0]
        file_to_write = filenames[1]
        byte_array = bytes_2_array(file_to_read)
        pbar.set_description('File->Array')
        pbar.update(1)
        hash_value = hashOriginal(file_to_read)
        pbar.set_description('Hashing    ')
        pbar.update(1)
        freq_dict = determine_frequencies(byte_array)
        pbar.set_description('Frequencies')
        pbar.update(1)
        compressed_list = huffman(freq_dict)
        pbar.set_description('Huffman    ')
        pbar.update(1)
        byte_string = translate(byte_array, compressed_list)
        pbar.set_description('Translation')
        pbar.update(1)
        final_byte_array = finalize(byte_string)
        pbar.set_description('Array->File')
        pbar.update(1)
        write_2_json(compressed_list, "dict.json")
        pbar.set_description('dict.json  ')
        pbar.update(1)
        write_2_binary(final_byte_array, file_to_write)
        pbar.set_description('Done       ')
        pbar.update(1)
        time.sleep(0.1)
    compressor_display(freq_dict, compressed_list, file_to_read, file_to_write, byte_array, hash_value)
if __name__ == "__main__":
    main()