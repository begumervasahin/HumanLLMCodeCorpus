import glob
def print_files_matching_pattern(pattern, description):
    matched_files = glob.glob(pattern)
    print(f"{description}:", matched_files)
def main():
    digit_prefixed_pattern = './[0-9].*'
    print_files_matching_pattern(digit_prefixed_pattern, "Files starting with a digit in the current directory")
    gif_files_pattern = '*.gif'
    print_files_matching_pattern(gif_files_pattern, "GIF files in the current directory")
    single_char_gif_pattern = '?.gif'
    print_files_matching_pattern(single_char_gif_pattern, "Single character named GIF files in the current directory")
    recursive_text_files_pattern = '**/*.txt'
    print_files_matching_pattern(recursive_text_files_pattern, "Text files in the current directory and subdirectories", True)
    recursive_directories_pattern = './**/'
    print_files_matching_pattern(recursive_directories_pattern, "Directories in the current directory and subdirectories", True)
if __name__ == '__main__':
    main()