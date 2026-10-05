
files_starting_with_digit = glob.glob('./[0-9].*')
gif_files = glob.glob('*.gif')
single_char_gif_files = glob.glob('?.gif')
all_txt_files_recursive = glob.glob('**/*.txt', recursive=True)
all_subdirectories_recursive = glob.glob('./**/', recursive=True)