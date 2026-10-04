import glob
def main():
    digit_files = glob.glob('./[0-9].*')
    print("Files starting with a digit:", digit_files)
    gif_files = glob.glob('*.gif')
    print("All .gif files:", gif_files)
    single_char_gif_files = glob.glob('?.gif')
    print("Single-character .gif files:", single_char_gif_files)
    txt_files_recursive = glob.glob('**/*.txt', recursive=True)
    print("All .txt files (recursive):", txt_files_recursive)
    directories_recursive = glob.glob('./**/', recursive=True)
    print("All directories (recursive):", directories_recursive)
if __name__ == "__main__":
    main()