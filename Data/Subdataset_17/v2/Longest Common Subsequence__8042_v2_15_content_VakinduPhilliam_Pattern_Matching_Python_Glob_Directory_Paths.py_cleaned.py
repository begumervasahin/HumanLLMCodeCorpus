import glob
def find_files_and_directories():
    digit_files = glob.glob('./[0-9].*')
    print("Files starting with a digit followed by any character(s):", digit_files)
    gif_files = glob.glob('*.gif')
    print("All .gif files in the current directory:", gif_files)
    single_char_gif_files = glob.glob('?.gif')
    print("Single-character .gif files in the current directory:", single_char_gif_files)
    txt_files_recursive = glob.glob('**/*.txt', recursive=True)
    print("All .txt files in the current directory and subdirectories:", txt_files_recursive)
    directories_recursive = glob.glob('./**/', recursive=True)
    print("All directories in the current directory and subdirectories:", directories_recursive)
if __name__ == "__main__":
    find_files_and_directories()