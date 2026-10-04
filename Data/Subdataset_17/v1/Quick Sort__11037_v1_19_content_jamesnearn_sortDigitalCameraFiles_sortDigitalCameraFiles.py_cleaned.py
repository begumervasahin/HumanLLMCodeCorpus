import getopt
import os
import time
import sys
def sort_files(given_dir, separator):
    for dirpath, dirnames, filenames in os.walk(given_dir):
        for filename in filenames:
            if filename.lower().endswith((".jpg", ".mp4", ".mts", ".mov")):
                parse_file(dirpath, filename, separator)
def parse_file(given_directory_path, given_filename, separator):
    given_full_filepath = os.path.join(given_directory_path, given_filename)
    print(given_full_filepath)
    new_path = get_destination_path(given_full_filepath, separator)
    new_path = os.path.join(given_directory_path, new_path)
    print(new_path)
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    new_file_path = os.path.join(new_path, given_filename)
    print(new_file_path)
    os.rename(given_full_filepath, new_file_path)
def get_destination_path(given_full_filepath, separator):
    epoch_sec = os.path.getmtime(given_full_filepath)
    new_path = time.strftime(f'%Y{separator}%Y %m %d', time.localtime(epoch_sec))
    return new_path
def main(argv):
    separator = "\\"
    path = ""
    try:
        opts, args = getopt.getopt(argv, "h", ["separator=", "path="])
    except getopt.GetoptError:
        print('SortFiles.py --separator <value> --path <path>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('SortFiles.py --separator <value> --path <path>')
            sys.exit()
        elif opt == "--separator":
            separator = arg
        elif opt == "--path":
            path = arg
    if not path:
        print("Error: Path is required")
        print('SortFiles.py --separator <value> --path <path>')
        sys.exit(2)
    print('Separator =', separator)
    print('Path =', path)
    sort_files(path, separator)
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "runtests":
        print('Running tests')
    else:
        main(sys.argv[1:])