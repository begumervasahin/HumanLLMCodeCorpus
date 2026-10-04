import os
import time
from tqdm import tqdm
from huffman_module import *
from comp_lib import *
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
def process_step(description, task, pbar):
    pbar.set_description(description)
    result = task()
    pbar.update(1)
    return result
def main():
    clear_console()
    hepia_print()
    print("\n")
    bar_format = '{l_bar}{bar}| {n_fmt}/{total_fmt}'
    total_steps = 9
    with tqdm(total=total_steps, ncols=80, bar_format=bar_format) as pbar:
        filenames = process_step('Open File  ', read_user_input, pbar)
        file_to_read, file_to_write = filenames
        byte_array = process_step('File->Array', lambda: bytes_2_array(file_to_read), pbar)
        hash_value = process_step('Hashing    ', lambda: hashOriginal(file_to_read), pbar)
        freq_dict = process_step('Frequencies', lambda: determine_frequencies(byte_array), pbar)
        compressed_list = process_step('Huffman    ', lambda: huffman(freq_dict), pbar)
        byte_string = process_step('Translation', lambda: translate(byte_array, compressed_list), pbar)
        final_byte_array = process_step('Array->File', lambda: finalize(byte_string), pbar)
        process_step('dict.json  ', lambda: write_2_json(compressed_list, "dict.json"), pbar)
        process_step('Done       ', lambda: write_2_binary(final_byte_array, file_to_write), pbar)
        time.sleep(0.1)
    compressor_display(freq_dict, compressed_list, file_to_read, file_to_write, byte_array, hash_value)
if __name__ == "__main__":
    main()