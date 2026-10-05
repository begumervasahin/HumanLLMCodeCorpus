
from huffman_module import *
from comp_lib import *
from tqdm import tqdm
import os
import time
os.system('cls' if os.name == 'nt' else 'clear')
hepia_print()
print("\n")
bar_format = '{l_bar}{bar}| {n_fmt}/{total_fmt}'
with tqdm(total=9, ncols=80, bar_format=bar_format) as pbar:
    filenames = read_user_input()
    update_bar(pbar, 'Open File  ')
    file_2_read = filenames[0]
    file_2_write = filenames[1]
    byte_array = bytes_2_array(file_2_read)
    update_bar(pbar, 'File->Array')
    HashVal = hashOriginal(file_2_read)
    update_bar(pbar, 'Hashing    ')
    freq_dict = determine_frequencies(byte_array)
    update_bar(pbar, 'Frequencies')
    compressed_list = huffman(freq_dict)
    update_bar(pbar, 'Huffman    ')
    byte_string = translate(byte_array, compressed_list)
    update_bar(pbar, 'Translation')
    final_byte_array = finalize(byte_string)
    update_bar(pbar, 'Array->File')
    write_2_json(compressed_list, "dict.json")
    update_bar(pbar, 'dict.json  ')
    write_2_binary(final_byte_array, file_2_write)
    update_bar(pbar, 'Done       ')
    time.sleep(0.1)
    pbar.close()
    compressor_display(freq_dict, compressed_list, file_2_read, file_2_write, byte_array, HashVal)