import glob
files_with_single_digit = glob.glob('./[0-9].*')
gif_files_in_current_dir = glob.glob('*.gif')
single_char_gif_files = glob.glob('?.gif')
all_txt_files_recursive = glob.glob('**/*.txt', recursive=True)
all_directories_recursive = glob.glob('./**/', recursive=True)