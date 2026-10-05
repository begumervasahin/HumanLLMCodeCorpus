import getopt
import os
import time
import shutil
import sys
def sort_files(directory_path, separator):
    for (dirpath, _, filenames) in os.walk(directory_path):
        for filename in filenames:
            if filename.lower().endswith((".jpg", ".mp4", ".mts", ".mov")):
                parse_file(dirpath, filename, separator)
def parse_file(directory_path, filename, separator):
    full_file_path = os.path.join(directory_path, filename)
    print(full_file_path)
    new_path = get_destination_path(full_file_path, separator)
    new_path = os.path.join(directory_path, new_path)
    print(new_path)
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    print(new_path + separator + filename)
    os.rename(full_file_path, os.path.join(new_path, filename))
def get_destination_path(full_file_path, separator):
    epoch_sec = os.path.getmtime(full_file_path)
    converted_date = time.ctime(epoch_sec)
    new_path = time.strftime('%Y' + separator + '%Y %m %d', time.localtime(epoch_sec))
    return new_path
def main(argv):
    separator = "\\"
    path = ""
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["separator=", "path="])
    except getopt.GetoptError:
        print('SortFiles.py --separator <value> --path <path>')
        print('Number of arguments:', len(sys.argv), 'arguments.')
        print('Argument List:', str(sys.argv))
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help':
            print('SortFiles.py --separator <value> --path <path>')
            sys.exit()
        elif opt == "--separator":
            separator = arg
        elif opt == "--path":
            path = arg
    print('Separator = ', separator)
    print('Path = ', path)
    sort_files(path, separator)
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "runtests":
        print('Running tests')
    else:
        main(sys.argv[1:])