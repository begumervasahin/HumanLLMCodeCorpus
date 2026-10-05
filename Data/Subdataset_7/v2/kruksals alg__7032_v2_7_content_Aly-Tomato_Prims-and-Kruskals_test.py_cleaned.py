from tqdm import tqdm
import os
import time
from huffman_module import *
from comp_lib import *
def fonk1():
    clear_console()
    print_university_name()
    print("\n")
    b1 = '{l_bar}{bar}| {n_fmt}/{total_fmt}'
    with tqdm(b2 = 9, ncols=80, bar_format=b1) as progress_bar:
        b3 = read_user_input()
        update_progress_bar(progress_bar, 'Opening File  ')
        b4 = b3[0]
        b5 = b3[1]
        b6 = convert_to_byte_array(b4)
        update_progress_bar(progress_bar, 'File to Array')
        b7 = calculate_hash(b4)
        update_progress_bar(progress_bar, 'Hashing       ')
        b8 = determine_byte_frequencies(b6)
        update_progress_bar(progress_bar, 'Frequencies   ')
        b9 = perform_huffman_encoding(b8)
        update_progress_bar(progress_bar, 'Huffman Coding')
        b10 = translate_byte_array(b6, b9)
        update_progress_bar(progress_bar, 'Translation   ')
        b11 = finalize_byte_string(b10)
        update_progress_bar(progress_bar, 'Array to File ')
        write_huffman_dictionary_to_json(b9, "dict.json")
        update_progress_bar(progress_bar, 'Write to JSON ')
        write_compressed_binary_data_to_file(b11, b5)
        update_progress_bar(progress_bar, 'Done          ')
        time.sleep(0.1)
        progress_bar.close()
        display_compression_information(b8, b9, b4, b5, b6, b7)
if b12 = = "__main__":
    fonk1()