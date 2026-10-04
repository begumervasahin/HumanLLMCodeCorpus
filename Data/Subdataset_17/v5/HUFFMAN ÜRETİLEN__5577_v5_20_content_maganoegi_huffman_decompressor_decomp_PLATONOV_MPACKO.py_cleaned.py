import os
import time
from tqdm import tqdm
from decomp_lib import *
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
def process_task(task_name, task_function, pbar):
    pbar.set_description(task_name)
    result = task_function()
    pbar.update(1)
    return result
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
        filenames = process_task(tasks[0][0], tasks[0][1], pbar)
        byte_array = process_task(tasks[1][0], tasks[1][1], pbar)
        dictionary = process_task(tasks[2][0], tasks[2][1], pbar)
        byte_string_no_zeros = process_task(tasks[3][0], tasks[3][1], pbar)
        retranslated_byte_array = process_task(tasks[4][0], tasks[4][1], pbar)
        process_task(tasks[5][0], tasks[5][1], pbar)
        time.sleep(0.1)
    decompressor_display(filenames[2])
if __name__ == "__main__":
    main()