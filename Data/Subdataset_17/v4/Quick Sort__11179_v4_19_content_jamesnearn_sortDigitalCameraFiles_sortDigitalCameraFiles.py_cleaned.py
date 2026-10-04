import getopt
import os
import time
import sys
def sort_files(directory, separator):
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.lower().endswith((".jpg", ".mp4", ".mts", ".mov")):
                parse_file(dirpath, filename, separator)
def parse_file(directory_path, filename, separator):
    full_filepath = os.path.join(directory_path, filename)
    print(full_filepath)
    new_path = get_destination_path(full_filepath, separator)
    new_directory = os.path.join(directory_path, new_path)
    print(new_directory)
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)
    new_full_filepath = os.path.join(new_directory, filename)
    print(new_full_filepath)
    os.rename(full_filepath, new_full_filepath)
def get_destination_path(filepath, separator):
    epoch_time = os.path.getmtime(filepath)
    formatted_date = time.strftime('%Y' + separator + '%Y %m %d', time.localtime(epoch_time))
    return formatted_date
def main(argv):
    separator = "\\"
    path = ""
    try:
        opts, _ = getopt.getopt(argv, "hi:o:", ["separator=", "path="])
    except getopt.GetoptError:
        print('Usage: SortFiles.py --separator <value> --path <path>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help':
            print('Usage: SortFiles.py --separator <value> --path <path>')
            sys.exit()
        elif opt == "--separator":
            separator = arg
        elif opt == "--path":
            path = arg
    print('Separator =', separator)
    print('Path =', path)
    sort_files(path, separator)
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "runtests":
        print('Running tests')
    else:
        main(sys.argv[1:])