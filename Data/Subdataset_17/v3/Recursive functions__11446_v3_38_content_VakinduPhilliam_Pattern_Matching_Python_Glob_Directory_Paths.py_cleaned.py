import glob
def find_files():
    digit_files = glob.glob('./[0-9].*')
    print('Files starting with a digit:', digit_files)
    gif_files = glob.glob('*.gif')
    print('All .gif files:', gif_files)
    single_char_gif_files = glob.glob('?.gif')
    print('.gif files with a single character name:', single_char_gif_files)
    txt_files_recursive = glob.glob('**/*.txt', recursive=True)
    print('All .txt files recursively:', txt_files_recursive)
    directories_recursive = glob.glob('./**/', recursive=True)
    print('All directories recursively:', directories_recursive)
def main():
    find_files()
if __name__ == '__main__':
    main()