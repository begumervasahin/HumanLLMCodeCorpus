import getopt
import os
import time
import sys
def sort_files(directory, separator):
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.lower().endswith((".jpg", ".mp4", ".mts", ".mov")):
                move_file(dirpath, filename, separator)
def move_file(directory_path, filename, separator):
    full_filepath = os.path.join(directory_path, filename)
    print(f"Current file path: {full_filepath}")
    new_path = get_new_path(full_filepath, separator)
    new_directory = os.path.join(directory_path, new_path)
    print(f"New directory path: {new_directory}")
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)
    new_full_filepath = os.path.join(new_directory, filename)
    print(f"New file path: {new_full_filepath}")
    os.rename(full_filepath, new_full_filepath)
def get_new_path(filepath, separator):
    epoch_time = os.path.getmtime(filepath)
    formatted_date = time.strftime(f'%Y{separator}%m{separator}%d', time.localtime(epoch_time))
    return formatted_date
def main(argv):
    separator = os.sep
    path = ""
    try:
        opts, _ = getopt.getopt(argv, "h", ["help", "separator=", "path="])
    except getopt.GetoptError:
        print('Usage: SortFiles.py --separator <value> --path <path>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('Usage: SortFiles.py --separator <value> --path <path>')
            sys.exit()
        elif opt == "--separator":
            separator = arg
        elif opt == "--path":
            path = arg
    if not path:
        print('Error: Path is required.')
        print('Usage: SortFiles.py --separator <value> --path <path>')
        sys.exit(2)
    print(f'Separator = {separator}')
    print(f'Path = {path}')
    sort_files(path, separator)
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "runtests":
        print('Running tests')
    else:
        main(sys.argv[1:])