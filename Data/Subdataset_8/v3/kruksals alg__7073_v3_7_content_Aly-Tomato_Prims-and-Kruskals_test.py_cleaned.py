from tqdm import tqdm
import os
import time
from huffman_module import *
from comp_lib import *
def main():
    clear_console()
    print_university_name()
    print("\n")
    progress_bar_format = '{l_bar}{bar}| {n_fmt}/{total_fmt}'
    with tqdm(total=9, ncols=80, bar_format=progress_bar_format) as progress_bar:
        input_filenames = read_user_input()
        update_progress_bar(progress_bar, 'Opening File  ')
        file_to_read = input_filenames[0]
        file_to_write = input_filenames[1]
        byte_array = convert_to_byte_array(file_to_read)
        update_progress_bar(progress_bar, 'File to Array')
        hash_value = calculate_hash(file_to_read)
        update_progress_bar(progress_bar, 'Hashing       ')
        byte_frequencies = determine_byte_frequencies(byte_array)
        update_progress_bar(progress_bar, 'Frequencies   ')
        huffman_encoding_result = perform_huffman_encoding(byte_frequencies)
        update_progress_bar(progress_bar, 'Huffman Coding')
        translated_byte_string = translate_byte_array(byte_array, huffman_encoding_result)
        update_progress_bar(progress_bar, 'Translation   ')
        finalized_byte_array = finalize_byte_string(translated_byte_string)
        update_progress_bar(progress_bar, 'Array to File ')
        write_huffman_dictionary_to_json(huffman_encoding_result, "dict.json")
        update_progress_bar(progress_bar, 'Write to JSON ')
        write_compressed_binary_data_to_file(finalized_byte_array, file_to_write)
        update_progress_bar(progress_bar, 'Done          ')
        time.sleep(0.1)
        progress_bar.close()
        display_compression_information(byte_frequencies, huffman_encoding_result, file_to_read, file_to_write, byte_array, hash_value)
if __name__ == "__main__":
    main()