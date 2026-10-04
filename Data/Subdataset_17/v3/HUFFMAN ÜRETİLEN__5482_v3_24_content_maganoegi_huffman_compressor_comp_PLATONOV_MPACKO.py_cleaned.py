import os
import time
from tqdm import tqdm
from huffman_module import *
from comp_lib import *
def update_progress_bar(pbar, task_name):
    pbar.set_description(task_name)
    pbar.update(1)
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    hepia_print()
    print("\n")
    bar_format = '{l_bar}{bar}| {n_fmt}/{total_fmt}'
    with tqdm(total=10, ncols=80, bar_format=bar_format) as pbar:
        input_file, output_file = read_user_input()
        update_progress_bar(pbar, 'Reading File Names')
        byte_array = bytes_2_array(input_file)
        update_progress_bar(pbar, 'Converting File to Byte Array')
        original_hash = hashOriginal(input_file)
        update_progress_bar(pbar, 'Computing File Hash')
        frequency_dict = determine_frequencies(byte_array)
        update_progress_bar(pbar, 'Calculating Byte Frequencies')
        huffman_dict = huffman(frequency_dict)
        update_progress_bar(pbar, 'Generating Huffman Codes')
        encoded_string = translate(byte_array, huffman_dict)
        update_progress_bar(pbar, 'Translating Byte Array')
        final_byte_array = finalize(encoded_string)
        update_progress_bar(pbar, 'Finalizing Encoded Data')
        write_2_json(huffman_dict, "dict.json")
        update_progress_bar(pbar, 'Writing Huffman Dictionary to JSON')
        write_2_binary(final_byte_array, output_file)
        update_progress_bar(pbar, 'Writing Output File')
        time.sleep(0.1)
        compressor_display(frequency_dict, huffman_dict, input_file, output_file, byte_array, original_hash)
if __name__ == "__main__":
    main()